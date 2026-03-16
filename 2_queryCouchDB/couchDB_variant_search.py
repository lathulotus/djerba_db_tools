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
from couchDB_utils import get_nested

def evaluate_criterion(value, criterion, value_type='string', mode="exact"):
    """ Case-insensitive match. Supports comma-separated strings or lists (OR condition) """
    if not criterion:
        return True
    if value is None:
        return False
    
    # Support comma-separated strings or lists
    if isinstance(criterion, str) and "," in criterion:
        criterion = [c.strip() for c in criterion.split(",")]
    
    if isinstance(criterion, list):
        return any(evaluate_criterion(value, c, value_type, mode) for c in criterion)

    value_norm = str(value).lower()
    criterion_norm = str(criterion).lower()

    if mode == "exact":
        return value_norm == criterion_norm
    if mode == "contains":
        return criterion_norm in value_norm
    
    return False

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
        "ctdna_status": (["plugins/pwgs.summary/results/ctdna_detection"]),
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
        
        requested_cnv = criteria["cnv_gene"] or criteria["cnv_type"]
        requested_snv = criteria["snv_gene"] or criteria["snv_type"]
        requested_fusion = criteria["fusion_gene"] or criteria["fusion_effect"] or criteria["fusion_frame"]

        cnv_body = get_nested(data, paths["cnv"][0])
        snv_body = get_nested(data, paths["snv"][0])
        fusion_body = get_nested(data, paths["fusion"][0])
        ctdna_status = get_nested(data, paths["ctdna_status"][0])
        ctdna_cnv = get_nested(data, paths["ctdna_cnv"][0])
        ctdna_snv = get_nested(data, paths["ctdna_snv"][0])

        if requested_cnv and not isinstance(cnv_body, list):
            continue
        if requested_snv and not isinstance(snv_body, list):
            continue
        if requested_fusion and not isinstance(fusion_body, list):
            continue
        if criteria.get("ctdna_status"):
            if str(ctdna_status).lower() != str(criteria["ctdna_status"]).lower():
                continue
        if criteria.get("ctdna_cnv") is not None:
            if bool(ctdna_cnv) != (criteria["ctdna_cnv"].lower() == "true"):
                continue
        if criteria.get("ctdna_snv"):
            if bool(ctdna_snv) != (criteria["ctdna_snv"].lower() == "true"):
                continue
        
        cnv_values = []
        if isinstance(cnv_body, list):
            for entry in cnv_body:
                if not isinstance(entry, dict):
                    continue
                if not evaluate_criterion(entry.get("Gene"), criteria["cnv_gene"], mode='exact'):
                    continue
                if not evaluate_criterion(entry.get("Alteration"), criteria["cnv_type"], mode='contains'):
                    continue
                cnv_values.append(entry)
        
        snv_values = []
        if isinstance(snv_body, list):
            for entry in snv_body:
                if not isinstance(entry, dict):
                    continue
                if not evaluate_criterion(entry.get("Gene"), criteria["snv_gene"], mode='exact'):
                    continue
                if not evaluate_criterion(entry.get("type"), criteria["snv_type"], mode='contains'):
                    continue
                snv_values.append(entry)

        fusion_values = []
        if isinstance(fusion_body, list):
            fusion_genes = []
            if criteria["fusion_gene"]:
                try:
                    fusion_genes = yaml.safe_load(criteria["fusion_gene"])
                    if not isinstance(fusion_genes, list):
                        fusion_genes = [fusion_genes]
                except:
                    fusion_genes = []

            for entry in fusion_body:
                if not isinstance(entry, dict):
                    continue

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
        
        matched = (
            (requested_cnv and cnv_values) or
            (requested_snv and snv_values) or
            (requested_fusion and fusion_values)
        )

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
        "fusion_gene": args.fusion_gene,
        "fusion_effect": args.fusion_effect,
        "fusion_frame": args.fusion_frame,
        "ctdna_status": args.ctdna_status,
        "ctdna_cnv": args.ctdna_cnv,
        "ctdna_snv": args.ctdna_snv
    }

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

        if (criteria["snv_gene"] or criteria["snv_type"]) and m["snvs"]:
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
