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
            couch = couchdb.Server(url, username=username, password=password)
        else:
            couch = couchdb.Server(url)

        if db_name not in couch:
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


def build_mango_query(hrd_status=None, msi_status=None, tmb_status=None, project=None, study=None, donor=None, assay=None):
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

    if project:
        selector["config.input_params_helper.project"] = project

    if study:
        selector["plugins.case_overview.results.study"] = study

    if donor:
        selector["config.input_params_helper.donor"] = donor        #plugins.case_overview.results.donor
    
    if assay:
        selector["config.input_params_helper.assay"] = assay        #plugins.case_overview.results.assay

    return {"selector": selector}


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
    parser.add_argument("--project", help="Filter by project name")
    parser.add_argument("--study", help="Filter by study name")
    parser.add_argument("--donor", help="Filter by donor ID")
    parser.add_argument("--assay", help="Filter by assay type (e.g., 'WGTS', 'WGS', 'TAR')")

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
        hrd_status=args.hrd_status
        msi_status=args.msi_status,
        tmb_status=args.tmb_status,
        project=args.project,
        study=args.study,
        donor=args.donor,
        assay=args.assay)

    # Download documents
    try:
        download_documents(db, query, args.output_dir)
    except Exception as e:
        print(f"An error occurred while downloading documents: {e}")


if __name__ == "__main__":
    main()
