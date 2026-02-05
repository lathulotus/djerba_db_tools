"""
Command-line scripts for retrieving reports stored by Djerba on CouchDB.

Modes for querying CouchDB:
    1. Fetch single report by report ID
    2. Fetch bulk reports by list of report IDs
    3. Filter reports by metadata fields
"""

# Packages
import os
import json
import logging
import requests
from typing import Any
from djerba.core.base import base as core_base

# Retrieve reports
class couchdb_reader(core_base):
    """Read-only access to retrieve reports stored on CouchDB."""

    def __init__(self, log_level=logging.INFO, log_path=None):
        """Initialize CouchDB connection using .env variables."""
        self.couch_db = os.environ.get("COUCH_DB")
        self.couch_user = os.environ.get("COUCH_USER")
        self.couch_pass = os.environ.get("COUCH_PASS")
        self.couch_url = os.environ.get("COUCH_URL")
        if self.couch_url:
            self.couch_url = self.couch_url.rstrip("/")

        missing = [
            name for name, value in{
                "COUCH_URL": self.couch_url,
                "COUCH_DB": self.couch_db,
                "COUCH_USER": self.couch_user,
                "COUCH_PASS": self.couch_pass
            }.items() if value is None
        ]
        if missing:
            raise RuntimeError(f"Missing required environment variable(s): {missing}")
        
        self.auth = (self.couch_user, self.couch_pass)
        logger_name = "djerba:couchdb_reader"
        self.logger = self.get_logger(log_level, logger_name, log_path)


    def fetch_single(self, report_id: str) -> dict[str, Any]:
        """Retrieve single report based on report ID."""
        url = f"{self.couch_url}/{self.couch_db}/{report_id}"
        self.logger.info(f"Fetching report by ID: {report_id}")

        response = requests.get(url, auth=self.auth)
        response.raise_for_status()

        return response.json()
    

    def fetch_bulk(self, report_ids: list[str]) -> list[dict[str, Any]]:
        """Retrieve multiple reports based on a list of report IDs."""
        url = f"{self.couch_url}/{self.couch_db}/_bulk_get"
        docIDs = {"docs": [{"id": repID} for repID in report_ids]}
        self.logger.info(f"Fetching {len(report_ids)} reports.")

        response = requests.post(
            url,
            auth=self.auth,
            headers={"Content-Type": "application/json"},
            data=json.dumps(docIDs)
        )

        response.raise_for_status()

        documents = []
        for result in response.json()["results"]:
            for doc in result["docs"]:
                if "ok" in doc:
                    documents.append(doc["ok"])
        
        return documents
    
    
    def fetch_metadata(self, selector: dict[str, Any]) -> list[dict[str, Any]]:
        """Retrieve reports based on metadata filtering queried via Mango."""

        url = f"{self.couch_url}/{self.couch_db}/_find"
        querying ={"selector": selector}
        self.logger.info(f"Running metadata query: {selector}")

        response = requests.post(
            url,
            auth=self.auth,
            headers={"Content-Type": "application/json"},
            data=json.dumps(querying)
        )

        response.raise_for_status()

        return response.json().get("docs", [])


