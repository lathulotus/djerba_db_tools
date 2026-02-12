"""
1. Identify couchDB connection details: script will require the URL, username, and password
2. Define the parameters paths with the JSON for filtering: Based on the built schemas
       * project: config.input_params_helper.project
       * donor: config.input_params_helper.donor
       * assay: config.input_params_helper.assay
       * HRD: plugins.genomic_landscape.results.genomic_biomarkers.HRD.Genomic biomarker alteration
       * MSI: plugins.genomic_landscape.results.genomic_biomarkers.MSI.Genomic biomarker alteration
       * TMB: plugins.genomic_landscape.results.genomic_biomarkers.TMB.Genomic biomarker alteration
3. Develop the script:
       * It will use the couchdb Python library
       * It will construct a couchDB mango query dynamically based on the input filters
       * It will fetch documents matching the query and save them to an output directory."""

import couchdb
import json
import os
import argparse


def get_couchdb_database(url, db_name, username=None, password=None):
    try:
        if username and password:
            protocol, rest = url.split("://", 1)
            url = f"{protocol}://{username}:{password}@{rest}"
        couch = couchdb.Server(url)

        try:
            return couch[db_name]
        except couchdb.http.ResourceNotFound:
            raise ValueError(f"Database '{db_name}' does not exist on the server.")

        return couch[db_name]
    except Exception as e:
        print(f"Error connecting to CouchDB: {e}")
        raise


def read_credentials(file_path):
    """
    Reads a credentials file formatted as:
    username: <username>
    password: <password>
    """
    username = None
    password = None
    try:
        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()
                if line.startswith("username:"):
                    username = line.split(":", 1)[1].strip()
                elif line.startswith("password:"):
                    password = line.split(":", 1)[1].strip()
    except Exception as e:
        raise ValueError(f"Error reading credentials file: {e}")

    if not username or not password:
        raise ValueError("Credentials file must contain both username and password.")

    return username, password


def build_mango_query(hrd_status=None, msi_status=None, tmb_status=None, hrd_value=None, msi_value=None, tmb_value=None, cancer_type=None, cnv_genes=None, snv_genes=None, cnv_type=None, snv_type=None, assay=None, project=None, donor=None, report_type=None, report_id=None, date=None, limit=None):
    """
    Builds a CouchDB Mango query selector based on the HRD status filter.
    """
    selector = {}

    if hrd_status:
        selector["plugins.genomic_landscape.results.genomic_biomarkers.HRD.Genomic biomarker alteration"] = hrd_status

    if msi_status:
        selector["plugins.genomic_landscape.results.genomic_biomarkers.MSI.Genomic biomarker alteration"] = msi_status

    if tmb_status:
        selector["plugins.genomic_landscape.results.genomic_biomarkers.TMB.Genomic biomarker alteration"] = tmb_status

    if hrd_value:
        selector["plugins.genomic_landscape.results.genomic_biomarkers.HRD.Genomic biomarker value"] = hrd_value

    if msi_value:
        selector["plugins.genomic_landscape.results.genomic_biomarkers.MSI.Genomic biomarker value"] = msi_value

    if tmb_value:
        selector["plugins.genomic_landscape.results.genomic_biomarkers.TMB.Genomic biomarker value"] = tmb_value

    if cancer_type:
        selector["plugins.case_overview.results.primary_cancer"] = cancer_type
    
    if cnv_genes:
        selector["plugins.wgts.cnv_purple.results.body.Gene"] = cnv_genes

    if snv_genes:
        selector["plugins.wgts.snv_indel.results.body.Gene"] = snv_genes

    if cnv_type:
        selector["plugins.wgts.cnv_purple.results.body.Alteration"] = cnv_type
    
    if snv_type:
        selector["plugins.wgts.snv_indel.results.body.Type"] = snv_type

    if assay:
        selector["config.input_params_helper.assay"] = assay        #plugins.case_overview.results.assay

    if project:
        selector["config.input_params_helper.project"] = project

    if donor:
        selector["config.input_params_helper.donor"] = donor        #plugins.case_overview.results.donor
    
    if report_type:
        selector["config.input_params_helper.attributes"] = report_type      #plugins.genomic_landscape.attributes

    if report_id:
        selector["_id"] = report_id

    if date:
        selector["last_updated"] = date         # string timestamp - DD/MM/YYYY_HH:MM:SSZ

    if limit is None:
        limit=100000    # maximum if none specified

    return {"selector": selector, "limit":limit}


def download_documents(db, query, output_dir):

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"Executing query: {json.dumps(query)}")

    results = db.find(query)
    downloaded_count = 0

    for doc in results:
        doc_id = doc.id
        file_path = os.path.join(output_dir, f"{doc_id}.json")
        try:
            with open(file_path, "w") as f:
                json.dump(doc, f, indent=2)
            print(f"Downloaded document '{doc_id}' to '{file_path}'")
            downloaded_count += 1
        except Exception as e:
            print(f"Error saving document '{doc_id}': {e}")

    print(f"Successfully downloaded {downloaded_count} documents.")
    return downloaded_count


def main():
    parser = argparse.ArgumentParser(
        description="Query CouchDB JSON documents based on HRD status filter."
    )
    parser.add_argument("--couchdb_url", required=True, help="URL of the CouchDB server (e.g., http://localhost:5984)")
    parser.add_argument("--db_name", required=True, help="Name of the CouchDB database")
    parser.add_argument("--username", help="CouchDB username (optional if using credentials_file)")
    parser.add_argument("--password", help="CouchDB password (optional if using credentials_file)")
    parser.add_argument("--credentials_file", help="Path to credentials file (username: x, password: x)")
    parser.add_argument("--output_dir", default="downloaded_jsons", help="Directory to save downloaded JSONs")

    parser.add_argument("--hrd_status", help="Filter by HRD status (e.g., 'HR Proficient', 'HR Deficient')")
    parser.add_argument("--msi_status", help="Filter by MSI status (e.g., 'MSS', 'MSI')")
    parser.add_argument("--tmb_status", help="Filter by TMB status (e.g., 'TMB-L', 'TMB-H')")
    parser.add_argument("--hrd_value", help="Filter by HRD biomarker value")
    parser.add_argument("--msi_value", help="Filter by MSI biomarker value")
    parser.add_argument("--tmb_value", help="Filter by TMB biomarker value")
    parser.add_argument("--cancer_type", help="Primary cancer diagnosis")
    parser.add_argument("--cnv_genes", help="Filter by genes containing CNVs")
    parser.add_argument("--snv_genes", help="Filter by genes containing SNVs")
    parser.add_argument("--cnv_type", help="Filter by type of CNV event (e.g., 'Amplification', 'Deletion')")
    parser.add_argument("--snv_type", help="Filter by type of SNV event (e.g., 'Missense Mutation', 'Frame Shift Ins', 'Splice Site')")

    parser.add_argument("--assay", help="Filter by assay type (e.g., 'WGTS', 'WGS', 'TAR')")
    parser.add_argument("--project", help="Filter by project name")
    parser.add_argument("--donor", help="Filter by donor ID")
    parser.add_argument("--report_type", help="Filter by report type (e.g., 'clinical', 'research')")
    parser.add_argument("--report_id", help="Filter by report ID")
    parser.add_argument("--date", help="Filter by date of last update")

    parser.add_argument("--limit", help="Maximum number of documents to return. Defaults to 100000 if not specified")
    parser.add_argument("--count", action="store_true", help="Returns number of reports satisfying the filters without downloading files")

    args = parser.parse_args()

    # Load credentials from file if provided
    if args.credentials_file:
        try:
            args.username, args.password = read_credentials(args.credentials_file)
        except Exception as e:
            print(f"Failed to read credentials: {e}")
            return

    # Connect to CouchDB
    try:
        db = get_couchdb_database(args.couchdb_url, args.db_name, args.username, args.password)
    except Exception as e:
        print(f"Could not connect to CouchDB: {e}")
        return

    # Build query
    query = build_mango_query(
        hrd_status=args.hrd_status,
        msi_status=args.msi_status,
        tmb_status=args.tmb_status,
        hrd_value=args.hrd_value,
        msi_value=args.msi_value,
        tmb_value=args.tmb_value,
        cancer_type=args.cancer_type,
        cnv_genes=args.cnv_genes,
        snv_genes=args.snv_genes,
        cnv_type=args.cnv_type,
        snv_type=args.snv_type,
        assay=args.assay,
        project=args.project,
        donor=args.donor,
        report_type=args.report_type,
        report_id=args.report_id,
        date=args.date,
        limit=args.limit)
    

    # Download documents or output document count
    if args.count:
        try:
            reports = db.find(query)
            count=sum(1 for _ in reports)
            print(f"Number of reports satisfying the filters: {count}")
        except:
            print(f"An error occurred while downloading documents: {e}")
    else:
        try:
            download_documents(db, query, args.output_dir)
        except Exception as e:
            print(f"An error occurred while downloading documents: {e}")


if __name__ == "__main__":
    main()
