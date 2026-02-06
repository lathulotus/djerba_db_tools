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
import argparse
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
        self.logger = self.get_logger(log_level, "djerba:couchdb_reader", log_path)


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
        payload = {"docs": [{"id": repID} for repID in report_ids]}
        
        self.logger.info(f"Fetching {len(report_ids)} reports.")

        response = requests.post(
            url,
            auth=self.auth,
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload)
        )

        response.raise_for_status()

        documents = []
        for result in response.json().get("results",[]):
            for doc in result.get("docs",[]):
                if "ok" in doc:
                    documents.append(doc["ok"])
        
        return documents
    
    
    def fetch_metadata(self, selector: dict[str, Any]) -> list[dict[str, Any]]:
        """Retrieve reports based on metadata filtering queried via Mango."""

        url = f"{self.couch_url}/{self.couch_db}/_find"
        payload ={"selector": selector}
        
        self.logger.info(f"Running metadata query: {selector}")

        response = requests.post(
            url,
            auth=self.auth,
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload)
        )

        response.raise_for_status()

        return response.json().get("docs", [])


def main():
    """Commandline interface for report fetching from CouchDB.
    """

    parser = argparse.ArgumentParser(description = "Fetch Djerba reports from couchDB")

    # single vs bulk retrieval
    parser.add_argument("--report-id", help="Fetch a single report by ID")
    parser.add_argument("--bulk-ids", help="Fetch multiple reports from text file of report IDs")

    # metadata querying: general
    parser.add_argument("--report-type", help="Possible search types: clinical, research, supplementary, failed")
    parser.add_argument("--last-updated", help="Reports updated on or after YYYY-MM-DD")

    # metadata querying: case overview
    parser.add_argument("--assay", help="Assay type")
    parser.add_argument("--primary-cancer", help="Primary cancer diagnosis")
    parser.add_argument("--site-of-biopsy", help="Biopsy site or surgery location")
    parser.add_argument("--study", help="Study name of research/clinical project")

    # metadata querying: sample information
    parser.add_argument("--oncotree-code", help="OncoTree cancer code")
    parser.add_argument("--estimated-purity", type=float, help="Estimated cancer cell content (%)")
    parser.add_argument("--estimated-ploidy", type=float, help="Estimated ploidy")
    parser.add_argument("--callability", type=float, help="Callability (%)")
    parser.add_argument("--coverage", type=float, help="Mean coverage")

    # metadata querying: biomarkers
    parser.add_argument("--tmb", type=float, help="Tumor mutation burden")
    parser.add_argument("--msi", type=float, help="Microsatellite instability")
    parser.add_argument("--hrd", type=float, help="Homologous recombination deficiency")

    # metadata querying: cnv
    parser.add_argument("--cnv-gene", help="CNV gene name")
    parser.add_argument("--cnv-alteration", help="CNV alteration type")
    parser.add_argument("--cnv-chromosome", help="CNV chromosome")
    parser.add_argument("--cnv-oncokb", help="CNV OncoKB level")

    # metadata querying: snv_indel
    parser.add_argument("--snv-gene", help="SNV gene name")
    parser.add_argument("--snv-protein", help="Protein alteration")
    parser.add_argument("--snv-type", help="SNV alteration type")
    parser.add_argument("--snv-oncokb", help="SNV OncoKB level")

    # wrapper
    args = parser.parse_args()
    reader = couchdb_reader()

    # single report
    if args.report_id:
        print(json.dumps(reader.fetch_single(args.report_id), indent=2))
        return
    
    # bulk reports
    if args.bulk_ids:
        with open(args.bulk_ids) as fh:
            report_ids = [line.strip() for line in fh if line.strip()]
        print(json.dumps(reader.fetch_bulk(report_ids), indent=2))
        return
    
    # metadata querying
    selector = {}

    if args.report_type:
        selector["attributes"] = args.report_type

    if args.last_updated:
        selector["config.case_overview.last_updated"] = {
            "$gte": args.last_updated
        }

    if args.assay:
        selector["config.case_overview.assay"] = args.assay

    if args.primary_cancer:
        selector["config.case_overview.primary_cancer"] = args.primary_cancer

    if args.site_of_biopsy:
        selector["config.case_overview.site_of_biopsy"] = args.site_of_biopsy

    if args.study:
        selector["config.case_overview.study"] = args.study

    if args.oncotree_code:
        selector["sample.results.OncoTree Code"] = args.oncotree_code

    if args.estimated_purity is not None:
        selector["sample.results.Estimated Cancer Cell Content (%)"] = args.estimated_purity

    if args.estimated_ploidy is not None:
        selector["sample.results.Estimated Ploidy"] = args.estimated_ploidy

    if args.callability is not None:
        selector["sample.results.Callability (%)"] = args.callability

    if args.coverage is not None:
        selector["sample.results.Coverage (mean)"] = args.coverage

    if args.tmb is not None:
        selector["genomic_landscape.results.genomic_biomarker.TMB.Genomic biomarker value"] = args.tmb

    if args.msi is not None:
        selector["genomic_landscape.results.genomic_biomarker.MSI.Genomic biomarker value"] = args.msi

    if args.hrd is not None:
        selector["genomic_landscape.results.genomic_biomarker.HRD.Genomic biomarker value"] = args.hrd

    if args.cnv_gene:
        selector["wgts.cnv_purple.results.body.Gene"] = args.cnv_gene

    if args.cnv_alteration:
        selector["wgts.cnv_purple.results.body.Alteration"] = args.cnv_alteration

    if args.cnv_chromosome:
        selector["wgts.cnv_purple.results.body.Chromosome"] = args.cnv_chromosome

    if args.cnv_oncokb:
        selector["wgts.cnv_purple.results.body.OncoKB"] = args.cnv_oncokb

    if args.snv_gene:
        selector["wgts.snv_indel.results.body.Gene"] = args.snv_gene

    if args.snv_protein:
        selector["wgts.snv_indel.results.body.protein"] = args.snv_protein

    if args.snv_type:
        selector["wgts.snv_indel.results.body.type"] = args.snv_type

    if args.snv_oncokb:
        selector["wgts.snv_indel.results.body.OncoKB"] = args.snv_oncokb

    if selector:
        print(json.dumps(reader.fetch_metadata(selector), indent=2))
        return
    
    parser.error("No valid query arguments provided")

