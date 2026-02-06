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
    parser.add_argument("--bulk-ids", help="Fetch multiple reports from text file containing report IDs")

    # metadata querying: general
    parser.add_argument("--report-type", help="Possible search types: clinical, research, supplementary, failed")
    parser.add_argument("--last-update", help="Reports updated on or after YYYY-MM-DD")

    # metadata querying: case overview
    parser.add_argument("--assay", help="Assay type")
    parser.add_argument("--primary-cancer", help="Primary cancer diagnosis")
    parser.add_argument("--biopsy-site", help="Biopsy site or surgery location")
    parser.add_argument("--study", help="Study name of research/clinical project")

    # metadata querying: sample information
    parser.add_argument("--oncotree-code", help="OncoTree cancer code")
    parser.add_argument("--sample-type", help="Type of sample extracted")
    parser.add_argument("--purity", type=float, help="Estimated cancer cell content (%)")
    parser.add_argument("--ploidy", type=float, help="Estimated ploidy")
    parser.add_argument("--callability", type=float, help="Callability (%)")
    parser.add_argument("--coverage", type=float, help="Mean coverage")

    # metadata querying: biomarkers
    parser.add_argument("--tmb-value", type=float, help="Tumor mutation burden")
    parser.add_argument("--msi-value", type=float, help="Microsatellite instability")
    parser.add_argument("--hrd-value", type=float, help="Homologous recombination deficiency")
    parser.add_argument("--tmb-alteration", help="Filter by TMB alteration status (TMB-H, TMB-L)")
    parser.add_argument("--msi-alteration", help="Filter by MSI status (MSI, MSS)")
    parser.add_argument("--hrd-alteration", help="Filter by HRD status (HR Deficient, HR Proficient, HRD, HRP)")

    # metadata querying: cnv
    parser.add_argument("--pga", type=int, help="Percent genome altered")
    parser.add_argument("--cnv-total", type=int, help="Total CNV events")
    parser.add_argument("--cnv-gene", help="CNV gene name")
    parser.add_argument("--cnv-alteration", help="CNV alteration type")
    parser.add_argument("--cnv-chromosome", help="CNV chromosome")
    parser.add_argument("--cnv-oncokb", help="CNV OncoKB level")

    # metadata querying: snv_indel
    parser.add_argument("--snv-somatic", type=int, help="Total somatic SNVs")
    parser.add_argument("--snv-coding", type=int, help="Coding SNVs")
    parser.add_argument("--snv-oncogenic", type=int, help="Oncogenic SNVs")
    parser.add_argument("--snv-gene", help="SNV gene name")
    parser.add_argument("--snv-protein", help="Protein alteration")
    parser.add_argument("--snv-type", help="SNV alteration type")
    parser.add_argument("--snv-vaf", type=float, help="Variant allele frequency")
    parser.add_argument("--snv-depth", help="Read depth")
    parser.add_argument("--snv-loh", type=lambda x: x.lower() == "true", help="Loss of heterozygosity (true or false)")
    parser.add_argument("--snv-chromosome", help="Chromosome")
    parser.add_argument("--snv-oncokb", help="SNV OncoKB level")

    # metadata querying: fusion
    parser.add_argument("--fusion-total", type=int, help="Total fusion events")
    parser.add_argument("--fusion-clinical", type=int, help="Clinically relevant fusions")
    parser.add_argument("--fusion-nccn", type=int, help="NCCN relevant fusions")

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

    if args.last_update:
        selector["config.case_overview.last_updated"] = {
            "$gte": args.last_update
        }

    if args.assay:
        selector["config.case_overview.assay"] = args.assay

    if args.primary_cancer:
        selector["config.case_overview.primary_cancer"] = args.primary_cancer

    if args.biopsy_site:
        selector["config.case_overview.site_of_biopsy"] = args.biopsy_site

    if args.study:
        selector["config.case_overview.study"] = args.study

    if args.oncotree_code:
        selector["sample.results.OncoTree Code"] = args.oncotree_code
    
    if args.sample_type:
        selector["sample.results.Sample Type"] = args.sample_type

    if args.purity is not None:
        selector["sample.results.Estimated Cancer Cell Content (%)"] = args.purity

    if args.ploidy is not None:
        selector["sample.results.Estimated Ploidy"] = args.ploidy

    if args.callability is not None:
        selector["sample.results.Callability (%)"] = args.callability

    if args.coverage is not None:
        selector["sample.results.Coverage (mean)"] = args.coverage

    if args.tmb_value is not None:
        selector["genomic_landscape.results.genomic_biomarker.TMB.Genomic biomarker value"] = args.tmb_value

    if args.msi_value is not None:
        selector["genomic_landscape.results.genomic_biomarker.MSI.Genomic biomarker value"] = args.msi_value

    if args.hrd_value is not None:
        selector["genomic_landscape.results.genomic_biomarker.HRD.Genomic biomarker value"] = args.hrd_value

    if args.tmb_alteration:
        selector["genomic_landscape.results.genomic_biomarkers.TMB.Genomic biomarker alteration"] = args.tmb_alteration

    if args.msi_alteration:
        selector["genomic_landscape.results.genomic_biomarkers.MSI.Genomic biomarker alteration"] = args.msi_alteration

    if args.hrd_alteration:
        selector["genomic_landscape.results.genomic_biomarkers.HRD.Genomic biomarker alteration"] = args.hrd_alteration

    if args.pga is not None:
        selector["wgts.cnv_purple.results.percent genome altered"] = args.pga

    if args.cnv_total is not None:
        selector["wgts.cnv_purple.results.total variants"] = args.cnv_total
    
    if args.cnv_gene:
        selector["wgts.cnv_purple.results.body.Gene"] = args.cnv_gene

    if args.cnv_alteration:
        selector["wgts.cnv_purple.results.body.Alteration"] = args.cnv_alteration

    if args.cnv_chromosome:
        selector["wgts.cnv_purple.results.body.Chromosome"] = args.cnv_chromosome

    if args.cnv_oncokb:
        selector["wgts.cnv_purple.results.body.OncoKB"] = args.cnv_oncokb

    if args.snv_somatic is not None:
        selector["wgts.snv_indel.results.somatic mutations"] = args.snv_somatic

    if args.snv_coding is not None:
        selector["wgts.snv_indel.results.coding sequence mutations"] = args.snv_coding

    if args.snv_oncogenic is not None:
        selector["wgts.snv_indel.results.oncogenic mutations"] = args.snv_oncogenic
    
    if args.snv_gene:
        selector["wgts.snv_indel.results.body.Gene"] = args.snv_gene

    if args.snv_protein:
        selector["wgts.snv_indel.results.body.protein"] = args.snv_protein

    if args.snv_type:
        selector["wgts.snv_indel.results.body.type"] = args.snv_type

    if args.snv_vaf is not None:
        selector["wgts.snv_indel.results.body.vaf"] = args.snv_vaf

    if args.snv_depth:
        selector["wgts.snv_indel.results.body.depth"] = args.snv_depth

    if args.snv_loh:
        selector["wgts.snv_indel.results.body.LOH"] = args.snv_loh

    if args.snv_chromosome:
        selector["wgts.snv_indel.results.body.Chromosome"] = args.snv_chromosome

    if args.snv_oncokb:
        selector["wgts.snv_indel.results.body.OncoKB"] = args.snv_oncokb

    if args.fusion_total is not None:
        selector["fusion.results.Total variants"] = args.fusion_total

    if args.fusion_clinical is not None:
        selector["fusion.results.Clinically relevant variants"] = args.fusion_clinical

    if args.fusion_nccn is not None:
        selector["fusion.results.nccn_relevant_variants"] = args.fusion_nccn

    if selector:
        print(json.dumps(reader.fetch_metadata(selector), indent=2))
        return
    
    parser.error("No valid query arguments provided")

