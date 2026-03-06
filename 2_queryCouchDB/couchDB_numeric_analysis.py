"""
Numeric-based analysis using filter flags to assess downloaded reports

Usage (example):
    python3 couchDB_numeric_analysis.py --input_dir script1_output/ --output_dir script2_output/ --plot
"""

import json
import os
import argparse
from datetime import datetime
import re
import shutil
import yaml
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
        current = data
        for key in keys:
            if isinstance(current, dict):
                current = current.get(key)
            else:
                current = None
                break
        if current not in (None, "", []):
            return current
    return None

def evaluate_criterion(value, criterion_str, value_type='float'):
    """
    Supports multiple criteria separated by commas (treated as OR condition).
    Also supports:
    - Ranges: [min, max] (inclusive)
    - Operators: >, <, >=, <=, ==
    - Bare values: defaults to >=
    """
    if not criterion_str:
        return True
    
    # Handle multiple criteria separated by commas (OR condition)
    # Check that it's not a single range [x, y]
    if "," in str(criterion_str) and not (str(criterion_str).strip().startswith("[") and str(criterion_str).strip().endswith("]")):
        criteria = [c.strip() for c in str(criterion_str).split(",")]
        return any(evaluate_criterion(value, c, value_type) for c in criteria)
    
    criterion_str = str(criterion_str).strip()

    # Handle Ranges: [80, 100]
    range_match = re.match(r'\[\s*(.*)\s*,\s*(.*)\s*\]', criterion_str)
    if range_match:
        min_raw, max_raw = range_match.groups()
        min_val = transform_value(min_raw, value_type)
        max_val = transform_value(max_raw, value_type)
        return min_val <= value <= max_val

    # Handle Operators
    op_match = re.match(r'^(>=|<=|>|<|==)?\s*(.*)$', criterion_str)
    if op_match:
        op, raw_target = op_match.groups()
        target = transform_value(raw_target, value_type)
        
        if op == '>': return value > target
        if op == '<': return value < target
        if op == '>=': return value >= target
        if op == '<=': return value <= target
        if op == '==': return value == target
        # Default to >= if no operator provided
        return value >= target

    return False

def transform_value(raw_val, value_type):
    """ Convert raw string to the appropriate type for comparison """
    raw_val = raw_val.strip()
    if value_type == 'float':
        return float(raw_val)
    if value_type == 'version':
        return parse_version(raw_val)
    if value_type == 'date':
        return datetime.strptime(raw_val, "%Y-%m-%d")
    return raw_val

def filter_files(input_dir, criteria):
    """ Apply numeric filters to input JSON files """
    results = []
    
    if not os.path.exists(input_dir):
        print(f"Error: Directory {input_dir} not found.")
        return []

    # Mapping of argument name to (JSON path, type)
    paths = {
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

    for filename in os.listdir(input_dir):
        if not filename.endswith(".json"):
            continue
            
        file_path = os.path.join(input_dir, filename)
        with open(file_path, 'r') as f:
            try:
                data = json.load(f)
            except:
                continue

            is_match = True
            extracted_values = {}

            for arg_name, (path, val_type) in paths.items():
                criterion = criteria.get(arg_name)
                raw_data = get_nested(data, path)

                if raw_data is None:
                    if criterion:
                        is_match = False
                        break
                    continue

                try:
                    current_val = transform_value(str(raw_data), val_type)
                    extracted_values[arg_name] = current_val

                    if criterion:
                        if not evaluate_criterion(current_val, criterion, val_type):
                            is_match = False
                            break
                except:
                    if criterion:
                        is_match = False
                        break

            if is_match:
                results.append({
                    "id": data.get("_id"),
                    "values": extracted_values,
                    "file": filename,
                    "full_path": file_path
                })

    return results

def plot_matches(matches, output_path=None):
    """ Cumulative plot over time by coverage """
    if not matches:
        print("No matches to plot.")
        return

    data = []
    for m in matches:
        v = m['values']
        if v.get('date_reported') and v.get('coverage'):
            data.append({
                'Date': v['date_reported'],
                'Coverage': v['coverage'],
                'ID': m['id']
            })
    
    if not data:
        print("No valid date/coverage data found to plot.")
        return

    df = pd.DataFrame(data)
    # Group by date to get count of cases and mean coverage per day
    df_plot = df.groupby('Date').agg(
        Case_Count=('ID', 'count'),
        Avg_Coverage=('Coverage', 'mean')
    ).reset_index().sort_values('Date')
    
    # Calculate cumulative count
    df_plot['Cumulative_Count'] = df_plot['Case_Count'].cumsum()

    plt.figure(figsize=(12, 7))
    
    # Plot a line connecting the cumulative counts
    plt.plot(df_plot['Date'], df_plot['Cumulative_Count'], color='steelblue', linestyle='-', linewidth=2, alpha=0.5, zorder=1)
    
    # Plot the cases as dots at their cumulative position, colored by their average coverage for that day
    scatter = plt.scatter(df_plot['Date'], df_plot['Cumulative_Count'], 
                         c=df_plot['Avg_Coverage'], cmap='viridis', 
                         s=100, alpha=0.9, edgecolors='w', zorder=2)
    
    # Add colorbar to show coverage scale
    cbar = plt.colorbar(scatter)
    cbar.set_label('Mean Coverage (Daily Average)')

    plt.title('Cumulative Case Accrual Over Time')
    plt.xlabel('Date Reported')
    plt.ylabel('Total Number of Cases (Cumulative)')
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.xticks(rotation=45)
    
    # Y axis starts at 0
    plt.ylim(0, df_plot['Cumulative_Count'].max() * 1.05)
    
    plt.tight_layout()

    if output_path:
        plt.savefig(output_path)
        print(f"Plot saved to: {output_path}")
    else:
        plt.show()

def main():
    parser = argparse.ArgumentParser(description="Advanced numeric filter for local Djerba JSONs")
    parser.add_argument("--input_dir", required=True, help="Directory containing JSON files")
    parser.add_argument("--output_dir", help="Directory to save matching JSON files")
    parser.add_argument("--coverage", help="Criterion for coverage (e.g. '>115.5' or '[80, 100]')")
    parser.add_argument("--purity", help="Criterion for purity (e.g. '>0.5')")
    parser.add_argument("--callability", help="Criterion for callability")
    parser.add_argument("--ploidy", help="Criterion for ploidy")
    parser.add_argument("--cnv_pga", help="Criterion for percent genome altered")
    parser.add_argument("--cnv_clinical", help="Criterion for number of clinically relevant CNVs")
    parser.add_argument("--snv_oncogenic", help="Criterion for number of oncogenic SNVs")
    parser.add_argument("--fusion_clinical", help="Criterion for number of clinically relevant fusions")
    parser.add_argument("--djerba_version", help="Criterion for version (e.g. '>1.11.1' or '[1.7.0, 1.12.0]')")
    parser.add_argument("--date_reported", help="Criterion for date (e.g. '>2025-01-01' or '[2024-01-01, 2025-12-31]')")
    parser.add_argument("--plot", action="store_true", help="Generate a plot of matches over time")
    parser.add_argument(  "--plot_out", help="Path to save the generated plot (e.g. 'plot.png')")
    
    args = parser.parse_args()

    criteria = {
        "coverage": args.coverage,
        "purity": args.purity,
        "callability": args.callability,
        "ploidy": args.ploidy,
        "cnv_pga": args.cnv_pga,
        "cnv_clinical": args.cnv_clinical,
        "snv_oncogenic": args.snv_oncogenic,
        "fusion_clinical": args.fusion_clinical,
        "djerba_version": args.djerba_version,
        "date_reported": args.date_reported
    }

    matches = filter_files(args.input_dir, criteria)

    if args.output_dir and matches:
        if not os.path.exists(args.output_dir):
            os.makedirs(args.output_dir)
            print(f"Created output directory: {args.output_dir}")

    print(f"\nFound {len(matches)} files matching filters:")
    for m in matches:
        v = m['values']
        date_str = v.get('date_reported').strftime("%Y-%m-%d") if v.get('date_reported') else "N/A"
        purity_val = v.get("purity", "N/A")

        filtered = ""
        for key, criterion in criteria.items():
            if criterion:
                val = v.get(key, "N/A")
                filtered += f"{key}: {val}"
        
        print(f"ID: {m['id']} \t| Date: {date_str} | {filtered} | Purity: {purity_val} | File: {m['file']}")
                
        if args.output_dir:
            shutil.copy(m['full_path'], os.path.join(args.output_dir, m['file']))
            
    if args.output_dir:
        print(f"\nCopied {len(matches)} files to {args.output_dir}")
    
    if args.plot:
        plot_path = args.plot_out
        if not plot_path and args.output_dir:
            plot_path = os.path.join(args.output_dir, "coverage_over_time.png")
        plot_matches(matches, plot_path)

    print("-" * 100)

if __name__ == "__main__":
    main()
