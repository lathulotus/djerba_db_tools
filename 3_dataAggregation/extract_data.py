"""
Produce summary tables (excel/csv) containing relevant data from downloaded JSON files
ex: coverage/quality vs time by HRD status

usage: python3 extract_data.py --input ./input_folder --output output_name
"""

import json
import os
import glob
import argparse
import pandas as pd
from datetime import datetime


def safe_get(data, path, default=None):
    for key in path:
        if not isinstance(data, dict):
            return default
        data = data.get(key)
    return data if data is not None else default


def parse_date(string_date):
    try:
        return datetime.strptime(string_date.split(" ")[0], "%Y-%m-%d_%H:%M:%S")
    except:
        return None


def extract_fields(doc):
    return {
        "report_id": doc.get("_id"),
        "date": parse_date(safe_get(doc, ["core", "extract_time"])),
        "cancer_type": safe_get(doc, ["plugins", "case_overview", "results", "primary_cancer"]),
        "HRD_status": safe_get(doc, ["plugins", "genomic_landscape", "results", "genomic_biomarkers", "HRD", "Genomic biomarker alteration"]),
        "HRD_value": safe_get(doc, ["plugins", "genomic_landscape", "results", "genomic_biomarkers", "HRD", "Genomic biomarker value"]),
        "coverage": safe_get(doc, ["plugins", "sample", "results", "Coverage (mean)"]),
        "callability": safe_get(doc, ["plugins", "sample", "results", "Callability (%)"]),
        "purity": safe_get(doc, ["plugins", "sample", "results", "Estimated Cancer Cell Content (%)"]),
        "snv": safe_get(doc, ["plugins", "wgts.snv_indel", "results", "somatic mutations"])
    }


def main():
    parser = argparse.ArgumentParser(description="Extract relevant data fields from downloaded JSON reports")
    parser.add_argument("--input", default="downloaded_jsons", help="Path to folder containing JSON files (default: ./downloaded_jsons)")
    parser.add_argument("--output", default="json_data", help="Base name for output files (without extension)")
    args = parser.parse_args()
    
    input_folder = args.input
    output_base = args.output
    json_files = os.path.join(input_folder, "*.json")

    rows = []
    for path in glob.glob(json_files):
        with open(path) as file:
            doc = json.load(file)
        rows.append(extract_fields(doc))
    df = pd.DataFrame(rows)

    csv_path = f"{output_base}.csv"
    df.to_csv(csv_path, index=False)
    print(f"Saved {csv_path}")

    xlsx_path = f"{output_base}.xlsx"
    df.to_excel(xlsx_path, index=False)
    print(f"Saved {xlsx_path}")


if __name__ == "__main__":
    main()



