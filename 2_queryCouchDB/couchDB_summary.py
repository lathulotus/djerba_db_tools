"""
Extract fields from JSONs to produce clean summary table as CSV/XLSX

Usage:
    python3 couchDB_summary.py --input_dir reports_input/ --output_name output_summary
"""

import json
import os
import argparse
from datetime import datetime
import pandas as pd
from couchDB_utils import get_nested, transform_value

string_fields = {
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
    "sample_type": (["plugins/sample/results/Sample Type", "report/sample_info_and_quality/Sample Type", "plugins/tar.sample/results/sample_type", "config/tar_input_params_helper/sample_type"]),
    "tmb_status": (["plugins/genomic_landscape/results/genomic_biomarkers/TMB/Genomic biomarker alteration"]),
    "hrd_status": (["plugins/genomic_landscape/results/genomic_biomarkers/HRD/Genomic biomarker alteration", "plugins/hrd/results/HRD_short"]),
    "msi_status": (["plugins/genomic_landscape/results/genomic_biomarkers/MSI/Genomic biomarker alteration"]),
    "ctdna_status": (["plugins/pwgs.summary/results/ctdna_detection"]),
    "ctdna_cnv": (["config/tar.status/copy_number_ctdna_detected"]),
    "ctdna_snv": (["config/tar.status/small_mutation_ctdna_detected"]),
    "purple_zip": (["config/wgts.cnv_purple/purple_zip"]),
    "sequenza_solution": (["config/cnv/sequenza_solution"])
}

numeric_fields = {
    "coverage": (["plugins/sample/results/Coverage (mean)", "report/sample_info_and_quality/Coverage (mean)", "plugins/pwgs.sample/results/coverage"], 'float'),
    "purity": (["config/genomic_landscape/purity", "supplementary/config/discovered/purity", "config/sample/purity", "config/wgts.cnv_purple/purity"], 'float'),
    "callability": (["plugins/sample/results/Callability (%)", "report/sample_info_and_quality/Callability (%)"], 'float'),
    "ploidy": (["plugins/sample/results/Estimated Ploidy", "report/sample_info_and_quality/Estimated Ploidy", "config/wgts.cnv_purple/ploidy"], 'float'),
    "djerba_version": (["core/core_version", "report/djerba_version", "plugins/case_overview/version"], 'version'),
    "date_reported": (["plugins/supplement.body/results/extract_date", "last_updated"], 'date'),

    "TMB": (["plugins/genomic_landscape/results/genomic_landscape_info/Tumour Mutation Burden", "report/genomic_landscape_info/Tumour Mutation Burden"], 'float'),
    "tmb_value": (["plugins/genomic_landscape/results/genomic_biomarkers/TMB/Genomic biomarker value", "report/genomic_landscape_info/TMB per megabase"], 'float'),
    "hrd_value": (["plugins/genomic_landscape/results/genomic_biomarkers/HRD/Genomic biomarker value"], 'float'),
    "msi_value": (["plugins/genomic_landscape/results/genomic_biomarkers/MSI/Genomic biomarker value"], 'float'),

    "pga": (["plugins/wgts.cnv_purple/results/percent genome altered", "report/genomic_landscape_info/Percent Genome Altered"], 'float'),
    "cnv_clinical": (["plugins/wgts.cnv_purple/results/clinically relevant variants", "plugins/wgts.cnv_purple/results/Clinically relevant variants", "report/oncogenic_somatic_CNVs/Clinically relevant variants"], 'float'),
    "snv_oncogenic": (["plugins/wgts.snv_indel/results/oncogenic mutations", "plugins/wgts.snv_indel/results/Oncogenic mutations", "report/small_mutations_and_indels/Clinically relevant variants", "plugins/tar.snv_indel/results/Clinically relevant variants"], 'float'),
    "fusion_clinical": (["plugins/fusion/results/Clinically relevant variants", "report/structural_variants_and_fusions/Clinically relevant variants"], 'float')
}

variant_fields = {
    "cnv": ["plugins/wgts.cnv_purple/results/body", "plugins/wgts.cnv_purple/results/Body", "report/oncogenic_somatic_CNVs/Body", "plugins/tar.cnv_purple/results/Body"],
    "snv": ["plugins/wgts.snv_indel/results/body", "plugins/wgts.snv_indel/results/Body", "report/small_mutations_and_indels/Body", "plugins/tar.snv_indel/results/Body"],
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
failed_values = {"false": False,
                 "true": True,}
hrd_values = {"hr proficient": "HRP", "hr-p": "HRP", "HR-P": "HRP",
              "hr deficient": "HRD", "hr-d": "HRD", "HR-D": "HRD"}

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
    results = {"hrd_status": None, "hrd_value": None,
               "msi_status": None, "msi_value": None,
               "tmb_status": None, "tmb_value": None}
    
    body = get_nested(data, "report/genomic_biomarkers/Body")
    if isinstance(body, list):
        for entry in body:
            if not isinstance(entry, dict):
                continue
            name = entry.get("Alteration")
            if not name:
                continue
            key = name.strip().upper()
            value = entry.get("Genomic biomarker value")
            status = (entry.get("Genomic biomarker alteration") or entry.get("Genomic biomarker call"))
            if key == "HRD":
                results["hrd_status"] = status
                results["hrd_value"] = value
            elif key == "MSI":
                results["msi_status"] = status
                results["msi_value"] = value
            elif key == "TMB":
                results["tmb_status"] = status
                results["tmb_value"] = value
    
    hrd_short = get_nested(data, "plugins/hrd/results/HRD_short")
    if isinstance(hrd_short, str) and hrd_short.strip():
        results["hrd_status"] = results["hrd_status"] or hrd_short.strip()
    
    return results

def extract_report_type(data, paths):
    """ Extract information from attributes, older reports store data within arrays """
    types_all = []
    for p in paths:
        val = get_nested(data, p)
        if isinstance(val, list):
            for item in val:
                if isinstance(item, str) and item.strip():
                    types_all.append(item.strip())
        elif isinstance(val, dict):
            for k, v in val.items():
                if isinstance(v, str) and v.strip():
                    types_all.append(v.strip())
        elif isinstance(val, str) and val.strip():
            types_all.append(val.strip())
    types_temp = set()
    types_final = []
    for item in types_all:
        if item not in types_temp:
            types_temp.add(item)
            types_final.append(item)
    return ",".join(types_final) if types_final else None

def extract_record(data):
    """ Extract data from JSONs """
    row = {}
    for col, paths in string_fields.items():
        if isinstance(paths, str):
            paths = [paths]
        raw = extract_path(data, paths)

        if col == "failed":
            row[col] = normalize_vals(raw, failed_values)
        elif col == "hrd_status":
            row[col] = normalize_vals(raw, hrd_values)
        elif col == "purple_zip":
            row[col] = os.path.basename(raw) if isinstance(raw, str) else raw
        elif col == "report_type":
            row[col] = extract_report_type(data, paths)
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
            if key == "hrd_status":
                row[key] = normalize_vals(biomarker[key], hrd_values)
            else:
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

    if not rows:
        print(f"No valid records found in {args.input_dir}. Summary table not created.")
        return

    df = pd.DataFrame(rows)
    if df.empty:
        print(f"Summary dataframe is empty for {args.input_dir}. Summary table not created.")
        return

    if "date_reported" in df.columns:
        df["date_reported"] = pd.to_datetime(df["date_reported"], errors="coerce", dayfirst=True).dt.strftime("%Y-%m-%d")

    csv_path = f"{args.output_name}.csv"
    
    column_order = ["report_id", "donor", "project", "study", "date_reported", "djerba_version", "failed", "report_type", "purple_zip", "sequenza_solution"]
    df = df[column_order + [c for c in df.columns if c not in column_order]]

    df.to_csv(csv_path, index=False)

    print(f"Extracted {len(df)} records.")
    print(f"Saved summary table to {csv_path}")

if __name__ == "__main__":
    main()
