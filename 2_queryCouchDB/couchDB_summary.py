"""
Extract fields from JSONs to produce clean summary table as CSV/XLSX

Usage:
    python3 couchDB_summary.py --input_dir reports_input/ --output_name output_summary
"""

import json
import os
import re
import argparse
import yaml
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

def parse_version(version_str):
    """ Convert version string to a tuple of integers for comparison """
    try:
        return tuple(map(int, re.sub(r'[^\d.]', '', version_str).split('.')))
    except:
        return (0,)
    
def get_nested(data, path):
    """ Get nested values from dict """
    keys = path.split('/')
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key)
        else:
            return None
    return data

def transform_value(raw_val, value_type):
    """Convert raw JSON values into typed Python values."""
    if raw_val is None:
        return None
    if isinstance(raw_val, str):
        raw_val = raw_val.strip()

    try:
        if value_type == "float":
            return float(raw_val)
        if value_type == "int":
            return int(raw_val)
        if value_type == "date":
            return datetime.strptime(raw_val, "%Y-%m-%d")
        if value_type == "version":
            return parse_version(raw_val)
        return raw_val

    except Exception:
        return None

def strip_time(val):
    if isinstance(val, datetime):
        return val.date()
    return val

string_fields = {
    "report_id": "_id",
    "donor": (["config/input_params_helper/donor", "config/tar_input_params_helper/donor", "report/patient_info/Patient Study ID"]),
    "project": (["config/input_params_helper/project", "config/tar_input_params_helper/project", "report/patient_info/Project"]),
    "study": (["plugins/case_overview/results/study", "report/patient_info/Study"]),
    "report_type": (["plugins/case_overview/attributes"]),
    "cancer_type": (["plugins/case_overview/results/primary_cancer", "report/patient_info/Primary cancer"]),
    "oncotree_code": (["plugins/sample/results/OncoTree code" "report/sample_info_and_quality/OncoTree code"]),
    "assay": (["config/input_params_helper/assay", "report/assay_type"]),
    "biopsy_site": (["plugins/case_overview/results/site_of_biopsy", "report/patient_info/Site of biopsy*"]),
    "sample_type": (["plugins/sample/results/Sample Type", "report/sample_info_and_quality/Sample Type"]),
    "hrd_status": (["plugins/genomic_landscape/results/genomic_biomarkers/HRD/Genomic biomarker alteration"]),
    "msi_status": (["plugins/genomic_landscape/results/genomic_biomarkers/MSI/Genomic biomarker alteration"]),
    "tmb_status": (["plugins/genomic_landscape/results/genomic_biomarkers/TMB/Genomic biomarker alteration"]),
    "failed": (["config/report_title/failed", "report/failed"]),
}

numeric_fields = {
    "coverage": (["plugins/sample/results/Coverage (mean)", "report/sample_info_and_quality/Coverage (mean)"], 'float'),
    "purity": (["config/genomic_landscape/purity", "supplementary/config/discovered/purity"], 'float'),
    "callability": (["plugins/sample/results/Callability (%)", "report/sample_info_and_quality/Callability (%)"], 'float'),
    "ploidy": (["plugins/sample/results/Estimated Ploidy", "report/sample_info_and_quality/Estimated Ploidy"], 'float'),
    "djerba_version": (["core/core_version", "report/djerba_version"], 'version'),
    "date_reported": (["plugins/supplement.body/results/extract_date", "last_updated"], 'date'),
    "cnv_pga": ("plugins/wgts.cnv_purple/results/percent genome altered", 'float'),
    "cnv_clinical": (["plugins/wgts.cnv_purple/results/clinically relevant variants", "report/oncogenic_somatic_CNVs/Clinically relevant variants"], 'float'),
    "snv_oncogenic": (["plugins/wgts.snv_indel/results/oncogenic mutations", "report/small_mutations_and_indels/Clinically relevant variants"], 'float'),
    "fusion_clinical": (["plugins/fusion/results/Clinically relevant variants", "report/structural_variants_and_fusions/Clinically relevant variants"], 'float'),
}

variant_fields = {
    "cnv": (["plugins/wgts.cnv_purple/results/body", "report/oncogenic_somatic_CNVs/Body"]),
    "snv": (["plugins/wgts.snv_indel/results/Body", "report/small_mutations_and_indels/Body"]),
    "fusion": (["plugins/fusion/results/body", "report/structural_variants_and_fusions/Body"])
}

def variant_data(data):
    """Extract SNV, CNV, and fusion values """
    snvs = get_nested(data, variant_fields["snv"])
    cnvs = get_nested(data, variant_fields["cnv"])
    fusions = get_nested(data, variant_fields["fusion"])
    
    snv_genes, snv_types = [], []
    if isinstance(snvs, list):
        for entry in snvs:
            if isinstance(entry, dict):
                snv_genes.append(entry.get("Gene"))
                snv_types.append(entry.get("type"))
    
    cnv_genes, cnv_types = [], []
    if isinstance(cnvs, list):
        for entry in cnvs:
            if isinstance(entry, dict):
                cnv_genes.append(entry.get("Gene"))
                cnv_types.append(entry.get("Alteration"))
    
    fusion_pairs, fusion_effects = [], []
    if isinstance(fusions, list):
        for entry in fusions:
            if isinstance(entry, dict):
                fusion_pairs.append(entry.get("fusion"))
                fusion_effects.append(entry.get("mutation effect"))
    
    return {
        "snv_genes": ", ".join([g for g in snv_genes if g]),
        "snv_types": ", ".join([t for t in snv_types if t]),
        "cnv_genes": ", ".join([g for g in cnv_genes if g]),
        "cnv_types": ", ".join([t for t in cnv_types if t]),
        "fusion_pairs": ", ".join([f for f in fusion_pairs if f]),
        "fusion_effects": ", ".join([e for e in fusion_effects if e])
    }

def clean_list(val):
    """ Cleaning list objects """
    if isinstance(val, list):
        return ", ".join(str(v) for v in val)
    return val

def extract_path(data, paths):
    """ Extract data from path associated with specific report """
    for p in paths:
        val = get_nested(data, p)
        if val not in (None, "", []):
            return val
    return None

def extract_record(data, paths):
    """ Extract data from JSONs """
    row = {}
    for col, paths in string_fields.items():
        if isinstance(paths, str):
            paths = [paths]
        raw = extract_path(data, paths)
        row[col] = clean_list(raw)
    for col, (paths, vtype) in numeric_fields.items():
        if isinstance(paths, str):
            paths = [paths]
        raw = extract_path(data, paths)
        row[col] = clean_list(raw, vtype)
    row.update(variant_data(data))
    return row

def main():
    parser = argparse.ArgumentParser(description="Produce summary table from reports")
    parser.add_argument("--input_dir", required=True, help="Directory containing JSON files")
    parser.add_argument("--output_name", default="summary_table", help="Name for output summary file")
    args = parser.parse_args()

    rows = []
    for filename in os.listdir(args.input_dir):
        if not filename.endswith(".json"):
            continue
            
        file_path = os.path.join(args.input_dir, filename)
        with open(file_path, 'r') as f:
            try:
                data = json.load(f)
            except:
                continue
        rows.append(extract_record(data))

    df = pd.DataFrame(rows)
    if "date_reported" in df.columns:
        df["date_reported"] = df["date_reported"].apply(strip_time)

    csv_path = f"{args.output_name}.csv"
    xlsx_path = f"{args.output_name}.xlsx"
    
    column_order = ["report_id", "donor", "project", "study", "date_reported", "djerba_version", "report_type"]
    df = df[column_order + [c for c in df.columns if c not in column_order]]

    df.to_csv(csv_path, index=False)
    df.to_excel(xlsx_path, index=False)

    print(f"Extracted {len(df)} records.")
    print(f"Saved summary table to {csv_path} & {xlsx_path}")

if __name__ == "__main__":
    main()