import couchdb
import json
import os
import argparse

def get_couchdb_database(couch_url, couch_db, username=None, password=None):
    """
    Connects to CouchDB and returns the specified database object.
    """
    try:
        if username and password:
            couch = couchdb.Server(couch_url, username=username, password=password)
        else:
            couch = couchdb.Server(couch_url)
        
        if couch_db not in couch:
            raise ValueError(f"Database '{couch_db}' does not exist on the server.")
        
        return couch[couch_db]
    except Exception as e:
        print(f"Error connecting to CouchDB: {e}")
        raise

def build_mango_query(hrd_status=None):
    """
    Builds a CouchDB Mango query selector based on the HRD status filter.
    """
    selector = {}

    if hrd_status:
        selector["plugins.genomic_landscape.results.genomic_biomarkers.HRD.Genomic biomarker alteration"] = hrd_status
    
    # CouchDB requires an index for _find queries on non-primary-key fields.
    # We will assume a default index exists or instruct the user to create one.
    # For complex queries, it's best to create specific indexes.
    return {"selector": selector}

def download_documents(db, query, output_dir):
    """
    Downloads documents matching the query and saves them to the output directory.
    """
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
        description="Query CouchDB for JSON documents based on HRD status."
    )
    parser.add_argument("--couchdb_couch_url", required=True, help="URL of the CouchDB server (e.g., http://localhost:5984)")
    parser.add_argument("--couch_db", required=True, help="Name of the CouchDB database")
    parser.add_argument("--username", help="CouchDB username (optional)")
    parser.add_argument("--password", help="CouchDB password (optional)")
    parser.add_argument("--output_dir", default="downloaded_jsons", help="Directory to save downloaded JSONs")
    
    parser.add_argument("--hrd_status", required=True, help="Filter by HRD status (e.g., 'HR Proficient', 'HR Deficient')")

    args = parser.parse_args()

    # Check if couchdb-python is installed
    try:
        import couchdb
    except ImportError:
        print("The 'couchdb' Python library is not installed.")
        print("Please install it using: pip install couchdb")
        return

    try:
        db = get_couchdb_database(args.couch_url, args.couch_db, args.username, args.password)
        query = build_mango_query(
            hrd_status=args.hrd_status
        )
        download_documents(db, query, args.output_dir)
    except Exception as e:
        print(f"An error occurred during execution: {e}")

if __name__ == "__main__":
    main()