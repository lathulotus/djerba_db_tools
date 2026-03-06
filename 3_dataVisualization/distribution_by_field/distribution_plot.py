""" Distribution histograms (code run after obtaining tables).
    Availabe parameters: PGA, TMB, MSI status, HRD score, Purity

Usage:
    python3 distribution_plot.py --input_dir input_data/ --output_dir output_folder/
 """

import os
import argparse
import pandas as pd
from distribution_utils import plot_bar

parser = argparse.ArgumentParser(description="Generate summary plots")
parser.add_argument("--input_dir", required=True, help="Path to directory containing CSVs with clean data")
parser.add_argument("--output_dir", default="./output/plot", help="Path to output folder")
args = parser.parse_args()

os.makedirs(args.output_dir, exist_ok=True)
def out(p): return os.path.join(args.output_dir, p)

# Load data
tables = {
    "pga": "pga_histogram.csv",
    "tmb": "tmb_histogram.csv",
    "hrd": "hrd_histogram.csv",
    "purity": "purity_histogram.csv"
}

for key, fname in tables.items():
    df = pd.read_csv(os.path.join(args.input_dir, fname))

    if key == "pga":
        plot_bar(df["Percentage(%)"], df["Count"],
                 "Distribution of Cases by Percent Genome Altered",
                 "Percentage (%)", "Count",
                 out("pga_histogram.png"))

    if key == "tmb":
        plot_bar(df["TMB_Range(Mb)"], df["Count"],
                 "Distribution of Cases by TMB Value",
                 "TMB Range (Mb)", "Count",
                 out("tmb_histogram.png"), rotation=90)

    if key == "hrd":
        plot_bar(df["HRD_Value"], df["Count"],
                 "Distribution of Cases by HRD Score",
                 "HRD Value", "Count",
                 out("hrd_histogram.png"))

    if key == "purity":
        plot_bar(df["Purity(%)"], df["Count"],
                 "Distribution of Cases by Tumour Purity",
                 "Purity (%)", "Count",
                 out("purity_histogram.png"))
