"""
Variant-based analysis using filter flags to assess downloaded reports

Usage (example):
   python3 couchDB_variant_search.py --input_dir script1_output/ --snv_gene TP53 --output_dir filtered_TP53/
"""

import json
import os
import argparse
import shutil
import yaml
from couchDB_utils import existing_path

def evaluate_criterion(value, criterion, mode="exact"):
    """ Case-insensitive match. Supports comma-separated strings or lists (OR condition) """
    if not criterion:
        return True
    if value is None:
        return False
    
    # Support comma-separated strings or lists
    if isinstance(criterion, str) and "," in criterion:
        criterion = [c.strip() for c in criterion.split(",")]
    
    if isinstance(criterion, list):
        return any(evaluate_criterion(value, c, mode) for c in criterion)

    value_norm = str(value).lower()
    criterion_norm = str(criterion).lower()

    if mode == "exact":
        return value_norm == criterion_norm
    if mode == "contains":
        return criterion_norm in value_norm
    return False

def gene_matches(gene_value, gene_filter):
    if not gene_filter:
        return True
    if isinstance(gene_filter, list):
        return gene_value in [g.lower() for g in gene_filter]
    if isinstance(gene_filter, dict):
        return True
    return gene_value == str(gene_filter).lower()

def all_genes(body, gene_filter):
    if not isinstance(gene_filter, dict) or "AND" not in gene_filter:
        return True
    required = [g.lower() for g in gene_filter["AND"]]
    report_genes = {entry.get("Gene", "").lower() for entry in body}
    return all(g in report_genes for g in required)

def filter_files(input_dir, criteria):
    """ Apply variant-level filters to input JSON files """
    results = []

    if not os.path.exists(input_dir):
        print(f"Error: Directory {input_dir} not found.")
        return []
    
    paths = {
        "cnv": (["plugins/wgts.cnv_purple/results/body", "plugins/wgts.cnv_purple/results/Body", "report/oncogenic_somatic_CNVs/Body", "plugins/tar.cnv_purple/results/Body"], 'array'),
        "snv": (["plugins/wgts.snv_indel/results/body", "plugins/wgts.snv_indel/results/Body", "report/small_mutations_and_indels/Body", "plugins/tar.snv_indel/results/Body"], 'array'),
        "fusion": (["plugins/fusion/results/body", "report/structural_variants_and_fusions/Body"], 'array'),
        "ctdna_status": (["plugins/tar.status/results/any_ctdna_detected", "plugins/pwgs.summary/results/ctdna_detection"]),
        "ctdna_cnv": (["config/tar.status/copy_number_ctdna_detected"]),
        "ctdna_snv": (["config/tar.status/small_mutation_ctdna_detected"])
    }

    for filename in os.listdir(input_dir):
        if not filename.endswith(".json"):
            continue

        file_path = os.path.join(input_dir, filename)
        with open(file_path, 'r') as f:
            try:
                data = json.load(f)
            except:
                continue
        
        cnv_body = existing_path(data, paths["cnv"])
        snv_body = existing_path(data, paths["snv"])
        fusion_body = existing_path(data, paths["fusion"])
        ctdna_status = existing_path(data, paths["ctdna_status"])
        ctdna_cnv = existing_path(data, paths["ctdna_cnv"])
        ctdna_snv = existing_path(data, paths["ctdna_snv"])

        if (criteria["cnv_gene"] or criteria["cnv_type"]) and not cnv_body:
            continue
        if (criteria["snv_gene"] or criteria["snv_type"] or criteria["snv_protein"]) and not snv_body:
            continue
        if (criteria["fusion_gene"] or criteria["fusion_effect"] or criteria["fusion_frame"]) and not fusion_body:
            continue
        if criteria.get("ctdna_status") and str(ctdna_status).strip().lower() != str(criteria["ctdna_status"]).strip().lower():
                continue
        if criteria.get("ctdna_cnv") and str(ctdna_cnv).strip().lower() != str(criteria["ctdna_cnv"]).strip().lower():
                continue
        if criteria.get("ctdna_snv") and str(ctdna_snv).strip().lower() != str(criteria["ctdna_snv"].strip().lower()):
                continue
        
        if not all_genes(cnv_body, criteria["cnv_gene"]):
            continue
        cnv_values = []
        if cnv_body:
            for entry in cnv_body:
                gene_filter = criteria["cnv_gene"]
                gene_value = entry.get("Gene", "").lower()
                if not gene_matches(gene_value, gene_filter):
                    continue
                if not evaluate_criterion(entry.get("Alteration"), criteria["cnv_type"], mode='contains'):
                    continue
                cnv_values.append(entry)
        
        if not all_genes(snv_body, criteria["snv_gene"]):
            continue
        snv_values = []
        if snv_body:
            for entry in snv_body:
                gene_filter = criteria["snv_gene"]
                gene_value = entry.get("Gene", "").lower()
                if not gene_matches(gene_value, gene_filter):
                    continue
                if not evaluate_criterion(entry.get("type"), criteria["snv_type"], mode='contains'):
                    continue
                if not evaluate_criterion(entry.get("Protein"), criteria["snv_protein"], mode='contains'):
                    continue
                snv_values.append(entry)

        fusion_values = []
        if fusion_body:
            fusion_genes = criteria["fusion_gene"] or []
            if isinstance(fusion_genes, str):
                fusion_genes = [fusion_genes]
            for entry in fusion_body:
                fusion_str = entry.get("fusion", "")
                partners = fusion_str.replace(" ", "").split("::")
                partners_norm = [p.lower() for p in partners]

                if fusion_genes:
                    user_genes = [g.lower() for g in fusion_genes]
                    if len(user_genes) == 1:
                        if user_genes[0] not in partners_norm:
                            continue
                    elif len(user_genes) == 2:
                        if not all(g in partners_norm for g in user_genes):
                            continue

                if not evaluate_criterion(entry.get("mutation effect"), criteria["fusion_effect"], mode='contains'):
                    continue
                if not evaluate_criterion(entry.get("frame"), criteria["fusion_frame"], mode='contains'):
                    continue

                fusion_values.append(entry)
        
        matched = True
        if (criteria["snv_gene"] or criteria["snv_type"] or criteria["snv_protein"]) and not snv_values:
            matched = False
        if (criteria["cnv_gene"] or criteria["cnv_type"]) and not cnv_values:
            matched = False
        if (criteria["fusion_gene"] or criteria["fusion_effect"] or criteria["fusion_frame"]) and not fusion_values:
            matched = False
        if matched:
            results.append({
                "id": data.get("_id"),
                "cnvs": cnv_values,
                "snvs": snv_values,
                "fusions": fusion_values,
                "ctdna_status": ctdna_status,
                "ctdna_cnv": ctdna_cnv,
                "ctdna_snv": ctdna_snv,
                "file": filename,
                "full_path": file_path
            })

    return results

def main():
    parser = argparse.ArgumentParser(description="Advanced variant filter for local Djerba JSONs")
    parser.add_argument("--input_dir", required=True, help="Directory containing JSON files")
    parser.add_argument("--output_dir", help="Directory to save matching JSON files")
    parser.add_argument("--cnv_gene", help="Filter by gene symbol type (e.g. TP53)")
    parser.add_argument("--cnv_type", help="Filter by CNV alteration (e.g. amplification)")
    parser.add_argument("--snv_gene", help="Filter by gene symbol (e.g. TP53)")
    parser.add_argument("--snv_type", help="Filter by SNV alteration type (e.g. missense)")
    parser.add_argument("--snv_protein", help="Filter by altered protein (SNV)")
    parser.add_argument("--fusion_gene", help="Filter by gene involved in fusion event (e.g. [TLE2] or [TLE2, PTPRS])")
    parser.add_argument("--fusion_effect", help="Filter by fusion effect (e.g. loss-of-function)")
    parser.add_argument("--fusion_frame", help="Filter by affected frame (e.g. out-of-frame)")
    parser.add_argument("--ctdna_status", help="Filter by whether ctDNA status (SNV and CNV) is 'Detected' or 'Not Detected'.")
    parser.add_argument("--ctdna_cnv", help="Filter by whether ctDNA (CNV) is 'True' or 'False'.")
    parser.add_argument("--ctdna_snv", help="Filter by whether ctDNA (SNV) is 'True' or 'False'.")

    args = parser.parse_args()

    criteria ={
        "cnv_gene": args.cnv_gene,
        "cnv_type": args.cnv_type,
        "snv_gene": args.snv_gene,
        "snv_type": args.snv_type,
        "snv_protein": args.snv_protein,
        "fusion_gene": args.fusion_gene,
        "fusion_effect": args.fusion_effect,
        "fusion_frame": args.fusion_frame,
        "ctdna_status": args.ctdna_status,
        "ctdna_cnv": args.ctdna_cnv,
        "ctdna_snv": args.ctdna_snv
    }

    for key in ("cnv_gene", "snv_gene", "fusion_gene"):
        val = criteria.get(key)
        if isinstance(val, str):
            val_str = val.strip()
            if val_str.startswith("{") or val_str.startswith("["):
                try:
                    criteria[key] = yaml.safe_load(val_str)
                except Exception:
                    pass

    matches = filter_files(args.input_dir, criteria)

    if args.output_dir:
        final_output_path = os.path.join(args.output_dir, "filtered_jsons")
    else:
        final_output_path = "filtered_jsons"

    if args.output_dir and matches:
        if os.path.exists(final_output_path):
            # Clear existing files to start fresh
            for f in os.listdir(final_output_path):
                file_p = os.path.join(final_output_path, f)
                try:
                    if os.path.isfile(file_p) or os.path.islink(file_p):
                        os.unlink(file_p)
                    elif os.path.isdir(file_p):
                        shutil.rmtree(file_p)
                except Exception as e:
                    print(f"Failed to delete {file_p}. Reason: {e}")
            print(f"Cleared existing files in: {final_output_path}")
        else:
            os.makedirs(final_output_path)
            print(f"Created output directory: {final_output_path}")

    print(f"\nFound {len(matches)} reports with matching variants:\n")
    for m in matches:
        v_filters = []

        if (criteria["snv_gene"] or criteria["snv_type"] or criteria["snv_protein"]) and m["snvs"]:
            for snv in m["snvs"]:
                gene = snv.get("Gene")
                alt = snv.get("type")
                v_filters.append(f"SNV: {gene} {alt}")

        if (criteria["cnv_gene"] or criteria["cnv_type"]) and m["cnvs"]:
            for cnv in m["cnvs"]:
                gene = cnv.get("Gene")
                alt = cnv.get("Alteration")
                v_filters.append(f"CNV: {gene} {alt}")

        if (criteria["fusion_gene"] or criteria["fusion_effect"] or criteria["fusion_frame"]) and m["fusions"]:
            for fus in m["fusions"]:
                fusion = fus.get("fusion")
                effect = fus.get("mutation effect")
                v_filters.append(f"FUSION: {fusion} {effect}")

        filtered = " | ".join(v_filters)

        print(f"ID: {m['id']} | {filtered} | File: {m['file']}")

        if args.output_dir:
            shutil.copy(m["full_path"], os.path.join(final_output_path, m["file"]))

    print()
    if args.output_dir:
        print(f"Copied {len(matches)} files to {final_output_path}")

    print("-" * 100)

if __name__ == "__main__":
    main()
