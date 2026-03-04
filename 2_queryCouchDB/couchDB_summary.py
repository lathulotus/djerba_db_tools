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
    
def get_nested(data, paths):
    """ Get nested values from dict """
    if isinstance(paths, str):
        paths = [paths]
    for path in paths:
        keys = path.split('/')
        for key in keys:
            if isinstance(data, dict):
                data = data.get(key)
            else:
                return None
    return data

def transform_value(raw_val, value_type):
    """Convert raw JSON values into typed Python values """
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
            date_fmts = ["%Y-%m-%d", "%d/%m/%Y %H:%M", "%d/%m/%Y_%H:%M:%S", "%d/%m/%Y_%H:%M:%SZ"]
            for fmt in date_fmts:
                try:
                    return datetime.strptime(raw_val, fmt)
                except:
                    pass
            #return datetime.strptime(raw_val, "%Y-%m-%d")
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
    "donor": (["config/input_params_helper/donor", "config/tar_input_params_helper/donor", "report/patient_info/Patient Study ID", "plugins/pwgs.case_overview/results/donor", "config/tar.snv_indel/donor"]),
    "project": (["config/input_params_helper/project", "config/tar_input_params_helper/project", "supplementary/config/inputs/projectid", "report/patient_info/Project", "config/pwgs_provenance_helper/project", "config/wgts.snv_indel/project"]),
    "study": (["plugins/case_overview/results/study", "report/patient_info/Study", "config/input_params_helper/study", "plugins/pwgs.case_overview/results/study_title", "plugins/pwgs.case_overview/results/study"]),
    "failed": (["config/report_title/failed", "report/failed"]),
    "report_type": (["plugins/case_overview/attributes", "config/pwgs.case_overview/attributes", "config/wgts.snv_indel/attributes", "config/tar.snv_indel/attributes"]),
    "cancer_type": (["plugins/case_overview/results/primary_cancer", "report/patient_info/Primary cancer", "config/pwgs.case_overview/primary_cancer"]),
    "oncotree_code": (["plugins/sample/results/OncoTree code", "report/sample_info_and_quality/OncoTree code", "config/wgts.snv_indel/oncotree_code", "config/tar.snv_indel/oncotree_code"]),
    "assay": (["config/input_params_helper/assay", "report/assay_type", "config/supplement.body/assay", "plugins/pwgs.case_overview/results/assay", "config/tar.snv_indel/assay"]),
    "biopsy_site": (["plugins/case_overview/results/site_of_biopsy", "report/patient_info/Site of biopsy/surgery"]),
    "sample_type": (["plugins/sample/results/Sample Type", "report/sample_info_and_quality/Sample Type"]),
    "hrd_status": (["plugins/genomic_landscape/results/genomic_biomarkers/HRD/Genomic biomarker alteration"]),
    "msi_status": (["plugins/genomic_landscape/results/genomic_biomarkers/MSI/Genomic biomarker alteration"]),
    "tmb_status": (["plugins/genomic_landscape/results/genomic_biomarkers/TMB/Genomic biomarker alteration"]),
    "ctdna_status": (["plugins/pwgs.summary/results/ctdna_detection"]),
    "purple_zip": (["config/wgts.cnv_purple/purple_zip"]),
    "sequenza_solution": (["config/cnv/sequenza_solution"])
}

numeric_fields = {
    "coverage": (["plugins/sample/results/Coverage (mean)", "report/sample_info_and_quality/Coverage (mean)", "plugins/pwgs.sample/results/coverage"], 'float'),
    "purity": (["config/genomic_landscape/purity", "supplementary/config/discovered/purity", "config/sample/purity"], 'float'),
    "callability": (["plugins/sample/results/Callability (%)", "report/sample_info_and_quality/Callability (%)"], 'float'),
    "ploidy": (["plugins/sample/results/Estimated Ploidy", "report/sample_info_and_quality/Estimated Ploidy"], 'float'),
    "djerba_version": (["core/core_version", "report/djerba_version", "plugins/case_overview/version"], 'version'),
    "date_reported": (["plugins/supplement.body/results/extract_date", "last_updated"], 'date'),

    "TMB": (["plugins/genomic_landscape/results/genomic_landscape_info/Tumour Mutation Burden", "report/genomic_landscape_info/Tumour Mutation Burden"], 'float'),
    "hrd_value": (["plugins/genomic_landscape/results/genomic_biomarkers/HRD/Genomic biomarker value"], 'float'),
    "msi_value": (["plugins/genomic_landscape/results/genomic_biomarkers/MSI/Genomic biomarker value"], 'float'),
    "tmb_value": (["plugins/genomic_landscape/results/genomic_biomarkers/TMB/Genomic biomarker value"], 'float'),

    "pga": ("plugins/wgts.cnv_purple/results/percent genome altered", 'float'),
    "cnv_clinical": (["plugins/wgts.cnv_purple/results/clinically relevant variants", "report/oncogenic_somatic_CNVs/Clinically relevant variants"], 'float'),
    "snv_oncogenic": (["plugins/wgts.snv_indel/results/oncogenic mutations", "report/small_mutations_and_indels/Clinically relevant variants", "plugins/tar.snv_indel/results/Clinically relevant variants"], 'float'),
    "fusion_clinical": (["plugins/fusion/results/Clinically relevant variants", "report/structural_variants_and_fusions/Clinically relevant variants"], 'float')
}

variant_fields = {
    "cnv": ["plugins/wgts.cnv_purple/results/body", "report/oncogenic_somatic_CNVs/Body", "plugins/tar.cnv_purple/results/Body"],
    "snv": ["plugins/wgts.snv_indel/results/Body", "report/small_mutations_and_indels/Body", "plugins/tar.snv_indel/results/Body"],
    "fusion": ["plugins/fusion/results/body", "report/structural_variants_and_fusions/Body"]
}

def variant_data(data):
    """Extract SNV, CNV, and fusion values """
    snvs = extract_path(data, variant_fields["snv"])
    cnvs = extract_path(data, variant_fields["cnv"])
    fusions = extract_path(data, variant_fields["fusion"])

    def normalize_keys(d, keys):
        if not isinstance(d, dict):
            return None
        for k in keys:
            if k in d and d[k] not in (None, ""):
                return d[k]
        return None
    
    cnv_genes, cnv_types = [], []
    if isinstance(cnvs, list):
        for entry in cnvs:
            if isinstance(entry, dict):
                cnv_genes.append(normalize_keys(entry, ["Gene", "gene"]))
                cnv_types.append(normalize_keys(entry, ["Alteration", "alteration"]))
    
    snv_genes, snv_protein, snv_types = [], [], []
    if isinstance(snvs, list):
        for entry in snvs:
            if isinstance(entry, dict):
                snv_genes.append(normalize_keys(entry, ["Gene", "gene"]))
                snv_types.append(normalize_keys(entry, ["Type", "type"]))
                snv_protein.append(normalize_keys(entry, ["Protein", "protein"]))

    fusion_pairs, fusion_effects = [], []
    if isinstance(fusions, list):
        for entry in fusions:
            if isinstance(entry, dict):
                fusion_pairs.append(normalize_keys(entry, ["Fusion", "fusion"]))
                fusion_effects.append(normalize_keys(entry, ["Mutation effect", "mutation effect"]))
    fusion_events = []
    fusion_exists = set()
    for pair, effect in zip(fusion_pairs, fusion_effects):
        if (pair, effect) not in fusion_exists:
            fusion_exists.add((pair, effect))
            fusion_events.append((pair, effect))
    fusion_pairs = [pair for pair, _ in fusion_events]
    fusion_effects = [effect for _, effect in fusion_events]
    
    return {
        "cnv_genes": ", ".join([g for g in cnv_genes if g]),
        "cnv_types": ", ".join([t for t in cnv_types if t]),
        "snv_genes": ", ".join([g for g in snv_genes if g]),
        "snv_types": ", ".join([t for t in snv_types if t]),
        "snv_protein": ", ".join([p for p in snv_protein if p]),
        "fusion_pairs": ", ".join([f for f in fusion_pairs if f]),
        "fusion_effects": ", ".join([e for e in fusion_effects if e])
    }

def normalize_vals(val, mapping=None, casefold=True):
    """ Normalize capitalization and minor differences in values """
    if val is None:
        return None
    if isinstance(val, str):
        v = val.strip()
        v_key = v.casefold() if casefold else v

        if mapping and v_key in mapping:
            return mapping[v_key]
        return v
    return val
failed_map = {"false": False, "true": True,}
hrd_map = {"hr proficient": "HRP", "hr-p": "HRP", "hr deficient": "HRD", "hr-d": "HRD"}

def clean_list(val, val_type=None):
    """ Cleaning list objects """
    if isinstance(val, list):
        return ", ".join(str(v) for v in val)
    if val_type:
        return transform_value(val, val_type)
    return val

def extract_path(data, paths):
    """ Extract data from paths containing slashes """
    for p in paths:
        if p == "report/patient_info/Site of biopsy/surgery":
            val = (
                data.get("report", {})
                .get("patient_info", {})
                .get("Site of biopsy/surgery"))
        else:
            val = get_nested(data, p)
        if val not in (None, "", []):
            return val
    return None

def extract_biomarker(data):
    """ Extract biomarker data from JSON, older reports store data within arrays """
    body = get_nested(data, "report/genomic_biomarkers/Body")
    if not isinstance(body, list):
        return{}
    
    results = {"hrd_status": None, "hrd_value": None, "msi_status": None, "msi_value": None, "tmb_status": None, "tmb_value": None}

    for entry in body:
        if not isinstance(entry, dict):
            continue
        name = entry.get("Alteration")
        if not name:
            continue

        key = name.strip().upper()
        value = entry.get("Genomic biomarker value")
        status_new = entry.get("Genomic biomarker alteration")
        status_old = entry.get("Genomic biomarker call")
        status = status_new or status_old

        if key == "HRD":
            results["hrd_status"] = status
            results["hrd_value"] = value
        elif key == "MSI":
            results["msi_status"] = status
            results["msi_value"] = value
        elif key == "TMB":
            results["tmb_status"] = status
            results["tmb_value"] = value
    return results

def extract_record(data):
    """ Extract data from JSONs """
    row = {}
    for col, paths in string_fields.items():
        if isinstance(paths, str):
            paths = [paths]
        raw = extract_path(data, paths)

        if col == "failed":
            row[col] = normalize_vals(raw, failed_map)
        elif col == "hrd_status":
            row[col] = normalize_vals(raw, hrd_map)
        elif col == "purple_zip":
            row[col] = os.path.basename(raw) if isinstance(raw, str) else raw
        else:
            row[col] = clean_list(raw)

    for col, (paths, val_type) in numeric_fields.items():
        if isinstance(paths, str):
            paths = [paths]
        raw = extract_path(data, paths)
        row[col] = clean_list(raw, val_type)

    row.update(variant_data(data))

    biomarker = extract_biomarker(data)
    for key in ["hrd_status", "hrd_value", "msi_status", "msi_value", "tmb_status", "tmb_value"]:
        if biomarker.get(key) is not None:
            row[key] = biomarker[key]
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
        df["date_reported"] = pd.to_datetime(df["date_reported"], errors="coerce", dayfirst=True).dt.strftime("%Y-%m-%d")

    csv_path = f"{args.output_name}.csv"
    xlsx_path = f"{args.output_name}.xlsx"
    
    column_order = ["report_id", "donor", "project", "study", "date_reported", "djerba_version", "failed", "report_type", "purple_zip", "sequenza_solution"]
    df = df[column_order + [c for c in df.columns if c not in column_order]]

    df.to_csv(csv_path, index=False)
    df.to_excel(xlsx_path, index=False)

    print(f"Extracted {len(df)} records.")
    print(f"Saved summary table to {csv_path} & {xlsx_path}")

if __name__ == "__main__":
    main()