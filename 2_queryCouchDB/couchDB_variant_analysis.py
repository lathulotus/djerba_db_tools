"""
Numeric-based analysis using filter flags to assess downloaded reports

Usage (example):
    python3 couchDB_numeric_analysis.py --input_dir script1_output/ --coverage ">=115" --output_dir HRD_PASSED_FILTERED --plot
"""

import json
import os
import argparse
from datetime import datetime
import re
import shutil
import pandas as pd
import matplotlib.pyplot as plt

def get_nested(data, path):
    """ Get nested values from dict """
    keys = path.split('/')
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key)
        else:
            return None
    return data

def evaluate_criterion(value, criterion, value_type='string', mode="exact"):
    """ Case-insensitive substring match """
    if not criterion:
        return True
    if value is None:
        return False
    
    value_norm = str(value).lower()
    criterion_norm = str(criterion).lower()

    if mode == "exact":
        return value_norm == criterion_norm
    if mode == "contains":
        return value_norm in criterion_norm
    
    return False

def filter_files(input_dir, criteria):
    """ Apply variant-level filters to input JSON files """
    results = []

    if not os.path.exists(input_dir):
        print(f"Error: Directory {input_dir} not found.")
        return []
    
    # Mapping of argument name to (JSON path, type)
    paths = {
        "cnv": ("plugins/wgts.cnv_purple/results/body", 'array'),
        "snv": ("plugins/wgts.snv_indel/results/Body", 'array'),
        "fusion": ("plugins/fusion/results/body", 'array')
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
        
        # Searching through CNVs
        cnv_values = []
        cnv_body = get_nested(data, paths["cnv"])
        if isinstance(cnv_body, list):
            for entry in cnv_body:
                if not isinstance(entry, data):
                    continue
                if not evaluate_criterion(entry.get("Gene"), criteria["cnv_gene"], mode='exact'):
                    continue
                if not evaluate_criterion(entry.get("Alteration"), criteria["cnv_type"], mode='contains'):
                    continue

                cnv_values.append(entry)
        
        # Searching through SNVs
        snv_values = []
        snv_body = get_nested(data, paths["snv"])
        if isinstance(snv_body, list):
            for entry in snv_body:
                if not isinstance(entry, data):
                    continue
                if not evaluate_criterion(entry.get("Gene"), criteria["snv_gene"], mode='exact'):
                    continue
                if not evaluate_criterion(entry.get("type"), criteria["snv_type"], mode='contains'):
                    continue

                snv_values.append(entry)

        # Searching through fusions
        fusion_values = []
        fusion_body = get_nested(data, paths["fusion"])
        if isinstance(fusion_body, list):
            fusion_genes=[]
            if criteria["fusion_gene"]:
                try:
                    fusion_genes = eval(criteria["fusion_gene"])
                except:
                    fusion_genes = []

            for entry in fusion_body:
                if not isinstance(entry, data):
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
        
        # Returning fields
        if cnv_values or snv_values or fusion_values:
            results.append({
                "id": data.get("_id"),
                "cnvs": cnv_values,
                "snvs": snv_values,
                "fusions": fusion_values,
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

    args = parser.parse_args()

    criteria ={
        "cnv_gene": args.cnv_gene,
        "cnv_type": args.cnv_type,
        "snv_gene": args.snv_gene,
        "snv_type": args.snv_type,
        "fusion_gene": args.fusion_gene,
        "fusion_effect": args.fusion_effect,
        "fusion_frame": args.fusion_frame
    }

    
    matches = filter_files(args.input_dir, criteria)

    if args.output_dir and matches:
        if not os.path.exists(args.output_dir):
            os.makedirs(args.output_dir)
            print(f"Created output directory: {args.output_dir}")

    print(f"\nFound {len(matches)} reports with matching variants:\n")
    for m in matches:
        v_filters = []

        if m["snvs"]:
            for snv in m["snvs"]:
                gene = snv.get("Gene")
                alt = snv.get("type")
                protein = snv.get("protein")
                v_filters.append(f"SNV: {gene} {alt} {protein}")

        if m["cnvs"]:
            for cnv in m["cnvs"]:
                gene = cnv.get("Gene")
                alt = cnv.get("Alteration")
                v_filters.append(f"CNV: {gene} {alt}")

        if m["fusions"]:
            for fus in m["fusions"]:
                gene = fus.get("gene")
                fusion = fus.get("fusion")
                effect = fus.get("mutation effect")
                frame = fus.get("frame")
                v_filters.append(f"FUSION: {fusion} {effect} {frame}")

        filtered = " | ".join(v_filters) if v_filters else "No variant filters matched"
        print(f"ID: {m['id']} | {filtered} | File: {m['file']}")

        if args.output_dir:
            shutil.copy(m["full_path"], os.path.join(args.output_dir, m["file"]))

    print()
    if args.output_dir:
        print(f"Copied {len(matches)} files to {args.output_dir}")

    print("-" * 100)

if __name__ == "__main__":
    main()


