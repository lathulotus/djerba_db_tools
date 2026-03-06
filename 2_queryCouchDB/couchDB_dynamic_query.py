"""
String-based querying (Mango) using input YAML filters for document retrieval:

Usage:
    python3 couchDB_dynamic_query.py --login_file login.txt --filters_file filters.yaml --output_dir script1_output/
"""

import couchdb
import json
import os
import argparse
import yaml
from datetime import datetime, timedelta

def read_login_file(file_path):
    """ Reads input file and returns dict with couchDB login info """
    params = {}
    with open(file_path, "r") as f:
        data = yaml.safe_load(f)
        #for line in f:
            #if ':' in line:
                #key, value = line.strip().split(':', 1)
                #params[key.strip()] = value.strip()
    # full pipeline
    if "login_file" in data:
        return data["login_file"]
    return data

def read_filters_yaml(file_path):
    """ Reads YAML file containing query filters """
    with open(file_path, "r") as f:
        return yaml.safe_load(f)

def get_couchdb_database(host, port, db_name, username=None, password=None):
    """ Connects to couchDB using login info and returns specified database object """
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
    """ Builds a CouchDB Mango query selector based on dictionary of filters & ignores null filters """
    filter_map = {
        "report_id": "_id",
        "donor": (["config/input_params_helper/donor", "config/tar_input_params_helper/donor", "report/patient_info/Patient Study ID", "plugins/pwgs.case_overview/results/donor", "config/tar.snv_indel/donor"]),
        "project": (["config/input_params_helper/project", "config/tar_input_params_helper/project", "supplementary/config/inputs/projectid", "report/patient_info/Project", "config/pwgs_provenance_helper/project", "config/wgts.snv_indel/project", "config/provenance_helper/project", "config/fusion/project"]),
        "study": (["plugins/case_overview/results/study", "report/patient_info/Study", "config/input_params_helper/study", "plugins/pwgs.case_overview/results/study_title", "plugins/pwgs.case_overview/results/study"]),
        "failed": (["config/report_title/failed", "report/failed", "config/supplement.body/failed"]),
        "report_type": (["plugins/case_overview/attributes", "config/pwgs.case_overview/attributes", "config/wgts.snv_indel/attributes", "config/tar.snv_indel/attributes", "plugins/genomic_landscape/attributes", "plugins/wgts.cnv_purple/attributes", "config/hrd/attributes"]),
        "cancer_type": (["plugins/case_overview/results/primary_cancer", "report/patient_info/Primary cancer", "config/pwgs.case_overview/primary_cancer", "plugins/pwgs.case_overview/results/primary_cancer"]),
        "oncotree_code": (["plugins/sample/results/OncoTree code", "report/sample_info_and_quality/OncoTree code", "config/wgts.snv_indel/oncotree_code", "config/tar.snv_indel/oncotree_code", "config/wgts.cnv_purple/oncotree_code", "config/fusion/oncotree_code"]),
        "assay": (["config/input_params_helper/assay", "report/assay_type", "config/supplement.body/assay", "plugins/pwgs.case_overview/results/assay", "config/tar.snv_indel/assay"]),
        "biopsy_site": (["plugins/case_overview/results/site_of_biopsy", "report/patient_info/Site of biopsy/surgery"]),
        "sample_type": (["plugins/sample/results/Sample Type", "report/sample_info_and_quality/Sample Type"]),
        "hrd_status": (["plugins/genomic_landscape/results/genomic_biomarkers/HRD/Genomic biomarker alteration", "plugins/hrd/results/HRD_short"]),
        "msi_status": (["plugins/genomic_landscape/results/genomic_biomarkers/MSI/Genomic biomarker alteration"]),
        "tmb_status": (["plugins/genomic_landscape/results/genomic_biomarkers/TMB/Genomic biomarker alteration"]),
        "ctdna_status": (["plugins/pwgs.summary/results/ctdna_detection"])
    }
    
    selector = {"$and": []}
    for key, paths in filter_map.items():
        value = filters.get(key)
        if value is None:
            continue

        # Support comma-separated strings by converting them to a list
        if isinstance(value, str) and "," in value:
            value = [v.strip() for v in value.split(",")]

        if isinstance(paths, str):
            paths = [paths]
        
        if key == "report_id":
            if isinstance(value, list):
                selector["$and"].append({"$or": [{paths[0].replace('/', '.'): {"$regex": f"^{v}"}} for v in value]})
            else:
                selector["$and"].append({paths[0].replace('/', '.'): {"$regex": f"^{value}"}})
            continue
        if key == "report_type":
            path = paths[0].replace('/', '.')
            if isinstance(value, list):
                selector["$and"].append({path: {"$all": value}})
            else:
                selector["$and"].append({path: {"$in": [value]}})
            continue
            
        if isinstance(value, list):
            selector["$and"].append({"$or": [{p.replace('/', '.'): {"$in": value}} for p in paths]})
        else:
            selector["$and"].append({"$or": [{p.replace('/', '.'): value} for p in paths]})
    return {"selector": selector}

def download_documents(db, query, output_dir, page_size=500):
    """ Extracts matching documents across each page in database """

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
