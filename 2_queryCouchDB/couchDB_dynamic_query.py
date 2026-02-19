"""
Use couchDB python library to apply specified mango queries based on input filters to ouput JSONs for reports satisfying filters (or report counts)
    1. Identify couchDB connection details based on text file containing host, port, username, and password
    2. Identify filters to apply based on YAML file containing specified query
    3. Define parameters paths to search based on non-null values in YAML

Usage:
    python3 couchdb_query.py --login_file login.txt --filters_file filters.yaml --output_dir ./query_output"""

import couchdb
import json
import os
import argparse
import yaml
from datetime import datetime, timedelta

def read_login_file(file_path):
    """
    Reads input file and returns dict with couchDB login info
    """
    params = {}
    with open(file_path, "r") as f:
        for line in f:
            if ':' in line:
                key, value = line.strip().split(':', 1)
                params[key.strip()] = value.strip()
    return params


def read_filters_yaml(file_path):
    """
    Reads YAML file containing query filters
    """
    with open(file_path, "r") as f:
        return yaml.safe_load(f)


def get_couchdb_database(host, port, db_name, username=None, password=None):
    """
    Connects to couchDB using login info and returns specified database object
    """
    try:
        url = f"http://{host}:{port}/"
        if username and password:
            from urllib.parse import urlparse, urlunparse
            scheme, netloc, path, params, query, fragment = urlparse(url)
            netloc = f"{username}:{password}@{host}:{port}"
            url = urlunparse((scheme, netloc, path, params, query, fragment))
        couch = couchdb.Server(url)

        if db_name not in couch:
            raise ValueError(f"Database '{db_name}' does not exist on the server.")
        return couch[db_name]
    except Exception as e:
        print(f"Error connecting to couchDB: {e}")
        raise


def build_mango_query(filters: dict):
    """
    Builds a CouchDB Mango query selector based on dictionary of filters
    Only filters with non-None values are added to selector
    """
    selector = {}

    # Map filter keys to document paths
    filter_map = {
        "report_id": "_id",
        "donor": "config.input_params_helper.donor",                #plugins.case_overview.results.donor
        "project": "config.input_params_helper.project",
        "study": "plugins.case_overview.results.study",
        "report_type": "plugins.case_overview.attributes",     #plugins.genomic_landscape.attributes
        "version": "core.core_version",

        "cancer_type": "plugins.case_overview.results.primary_cancer",
        "oncotree_code": "plugins.sample.results.OncoTree Code",
        "assay": "config.input_params_helper.assay",                #plugins.case_overview.results.assay
        "biopsy_site": "plugins.case_overview.results.site_of_biopsy",
        "sample_type": "plugins.sample.results.Sample Type",

        "purity": "plugins.sample.results.Estimated Cancer Cell Content (%)",
        "ploidy": "plugins.sample.results.Estimated Ploidy",
        "coverage": "plugins.sample.results.Coverage (mean)",
        "callability": "plugins.sample.results.Callability (%)",

        "hrd_status": "plugins.genomic_landscape.results.genomic_biomarkers.HRD.Genomic biomarker alteration",
        "msi_status": "plugins.genomic_landscape.results.genomic_biomarkers.MSI.Genomic biomarker alteration",
        "tmb_status": "plugins.genomic_landscape.results.genomic_biomarkers.TMB.Genomic biomarker alteration",
        "hrd_value": "plugins.genomic_landscape.results.genomic_biomarkers.HRD.Genomic biomarker value",
        "msi_value": "plugins.genomic_landscape.results.genomic_biomarkers.MSI.Genomic biomarker value",
        "tmb_value": "plugins.genomic_landscape.results.genomic_biomarkers.TMB.Genomic biomarker value",

        "fusion_total": "plugins.fusion.results.Total variants",
        "fusion_clinical": "plugins.fusion.results.Clinically relevant variants",
        "fusion_nccn": "plugins.fusion.results.nccn_relevant_variants",
    }

    # Searching numeric values
    numeric_range_fields = ["purity", "ploidy", "coverage", "callability", "hrd_value", "msi_value", "tmb_value"]
    cutoff = 0.0001
    for field in numeric_range_fields:
        value = filters.get(field)
        if value is None:
            continue
        path = filter_map[field]

        # Searching rounded value
        if isinstance(value, (int, float)):
            selector[path] = {"$gte": value - cutoff, "$lte": value + cutoff}
            continue

        # Searching ranges
        if isinstance(value, str) and "," in value:
            parts = value.split(",")
            if len(parts) == 2:
                minVal = float(parts[0].strip())
                maxVal = float(parts[1].strip())
                selector[path] = {"$gte": minVal, "$lte": maxVal}

    # Searching date
    date = filters.get("date")
    if date:
        if isinstance(date, (list, tuple)):
            date = [d for d in date if d]
        else:
            date = [date]

        if len(date) == 1:
            year, month, day = map(int, date[0].split("/"))
            day_start = datetime(year, month, day)
            day_end = day_start + timedelta(days=1)
        elif len(date) == 2:
            year0, month0, day0 = map(int, date[0].split("/"))
            year1, month1, day1 = map(int, date[1].split("/"))
            day_start = datetime(year0, month0, day0)
            day_end = datetime(year1, month1, day1) + timedelta(days=1)

        else:
            day_start = day_end = None
        if day_start and day_end:
            start = day_start.strftime("%d/%m/%Y") + "_00:00:00Z"
            end = day_end.strftime("%d/%m/%Y") + "_00:00:00Z"
            selector["last_updated"] = {"$gte": start, "$lt": end}

    # Searching fusion genes
    fusion = filters.get("fusion")
    if fusion:
        fusion_gene = []
        fusion_effect = {}

        for fusion_obj in fusion:
            if isinstance(fusion_obj, dict):
                for key, value in fusion_obj.items():
                    if key == "gene":
                        if not value:
                            continue
                        gene_list = [g.strip() for g in value.split(",")]
                        if len(gene_list) == 1:
                            fusion_gene.append({"fusion": {"$regex": gene_list[0]}})
                        elif len(gene_list) == 2:
                            gene1, gene2 = gene_list
                            fusion_gene.extend([{"fusion": f"{gene1}::{gene2}"}, {"fusion": f"{gene2}::{gene1}"}])
                    else:
                        if value:
                            fusion_effect[key] = value
            else:
                if fusion_obj:
                    fusion_gene.append({"fusion": {"$regex": fusion_obj}})

        fusion_selector = {}
        if fusion_gene:
            fusion_selector["$or"] = fusion_gene
        fusion_selector.update(fusion_effect)

        if fusion_selector:
            selector["plugins.fusion.results.body"] = {"$elemMatch": fusion_selector}

    # Searching CNVs
    cnv = filters.get("cnv")
    if cnv:
        cnv_filters = []
        for cnv_single in cnv:
            parts = cnv_single.split(" ", 1)
            gene = parts[0]
            mutation_type = parts[1] if len(parts) > 1 else None

            elem = {"Gene": gene}
            if mutation_type:
                elem["Alteration"] = mutation_type

            cnv_filters.append({
                "plugins.wgts.cnv_purple.results.body": {"$elemMatch": elem}})

        if len(cnv_filters) == 1:
            selector.update(cnv_filters[0])
        else:
            selector["$and"] = cnv_filters

    # Searching SNVs
    snv = filters.get("snv")
    if snv:
        snv_filters = []
        for snv_single in snv:
            parts = snv_single.split(" ", 1)
            gene = parts[0]
            mutation_type = parts[1] if len(parts) > 1 else None

            elem = {"Gene": gene}
            if mutation_type:
                elem["type"] = mutation_type

            snv_filters.append({
                "plugins.wgts.snv_indel.results.Body": {"$elemMatch": elem}})

        if len(snv_filters) == 1:
            selector.update(snv_filters[0])
        else:
            selector["$and"] = snv_filters

    # Assigning fields
    for key, path in filter_map.items():
        if key in numeric_range_fields:
            continue
        value = filters.get(key)
        if value is not None:
            selector[path] = value
        if key == "report_type":
            if isinstance(value, list):
                selector[path] = {"$all": value}
            else:
                selector[path] = {"$in": [value]}
            continue

    return {"selector": selector}


def download_documents(db, query, output_dir, page_size=500):
    """
    Extracts matching documents across each page in database
    """

    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    downloaded_count = 0
    skip = 0

    while True:
        paged_query = query.copy()
        paged_query["limit"] = page_size
        paged_query["skip"] = skip

        print(f"Executing query with skip={skip}, limit={page_size}")
        results = list(db.find(paged_query))
        if not results:
            break

        for doc in results:
            downloaded_count += 1

            if output_dir:
                doc_id = doc["_id"]
                file_path = os.path.join(output_dir, f"{doc_id}.json")
                try:
                    with open(file_path, "w") as f:
                        json.dump(doc, f, indent=2)
                    print(f"Downloaded document '{doc_id}' to '{file_path}'")
                except Exception as e:
                    print(f"Error saving document '{doc_id}': {e}")

        skip += len(results)
    return downloaded_count


def main():
    parser = argparse.ArgumentParser(description="Query CouchDB JSON documents using login and filter files")
    parser.add_argument("--login_file", required=True, help="Path to login.txt with CouchDB parameters")
    parser.add_argument("--filters_file", required=True, help="Path to YAML file with query filters")
    parser.add_argument("--output_dir", default="downloaded_jsons", help="Directory to save downloaded JSON files")
    parser.add_argument("--page_size", type=int, default=500, help="Number of documents to fetch per page")
    parser.add_argument("--count", action="store_true", help="Returns number of reports satisfying the filters without downloading files")
    args = parser.parse_args()

    try:
        # Read login info
        login_params = read_login_file(args.login_file)
        db = get_couchdb_database(
            host=login_params.get("host"),
            port=login_params.get("port"),
            db_name=login_params.get("db_name"),
            username=login_params.get("username"),
            password=login_params.get("password")
        )

        # Read filters from YAML
        filters = read_filters_yaml(args.filters_file)
        query = build_mango_query(filters)

        # Export downloaded documents or document count
        if args.count:
            total_count = download_documents(db, query, output_dir=None, page_size=args.page_size)
            print(f"Number of reports satisfying the filters: {total_count}")
        else:
            total_count = download_documents(db, query, args.output_dir, page_size=args.page_size)
            print(f"Successfully downloaded {total_count} documents.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
