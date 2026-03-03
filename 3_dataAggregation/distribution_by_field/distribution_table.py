""" Cleaned summary tables counting number of cases by given parameter (from generated summary tables).
    Availabe parameters: OncoTree code, SNV, CNV, PGA, Fusion, TMB, MSI status, HRD score, Purity

Usage:
    python3 distribution_table.py --summary_csv input_data.csv --output_dir output_folder/
 """

import os
import argparse
import pandas as pd
import numpy as np
from distribution_utils import (clean_oncotree, clean_blank, to_histogram_df, write_table)

parser = argparse.ArgumentParser(description="Generate summary tables")
parser.add_argument("--summary_csv", required=True, help="Path to input summary table")
parser.add_argument("--output_dir", default="./output/tables", help="Path to output folder")
args = parser.parse_args()

os.makedirs(args.output_dir, exist_ok=True)
def out(p): return os.path.join(args.output_dir, p)

df = pd.read_csv(args.summary_csv)
combined = {}

df["oncotree_code"] = clean_oncotree(df["oncotree_code"])

with pd.ExcelWriter(out("summary_clean.xlsx")) as writer:
    # 1) OncoTree
    onco = df["oncotree_code"].value_counts()
    if onco.empty:
        onco = pd.Series({"Blank": 0})
    combined["oncotree"] = write_table(onco, "OncoTree_Code", out("oncotree_count.csv"), writer, "oncotree_count")

    # 2) SNV
    snv = clean_blank(df["snv_genes"]).value_counts()
    if snv.empty:
        snv = pd.Series({"Blank": 0})
    combined["snv"] = write_table(snv, "SNV_Gene", out("snv_count.csv"), writer, "snv_count")

    # 3) CNV
    genes = clean_blank(df["cnv_genes"])
    types = clean_blank(df["cnv_types"])
    cnv = pd.DataFrame({"Gene": genes, "Type": types}).dropna()

    amps = cnv[cnv["Type"].str.lower() == "amplification"]["Gene"].value_counts()
    dels = cnv[cnv["Type"].str.lower() == "deletion"]["Gene"].value_counts()

    if amps.empty:
        amps = pd.Series({"Blank": 0})
    if dels.empty:
        dels = pd.Series({"Blank": 0})

    combined["cnv_amp"] = write_table(amps, "CNV_Amplification_Gene", out("cnv_amplification.csv"), writer, "cnv_amp")
    combined["cnv_del"] = write_table(dels, "CNV_Deletion_Gene", out("cnv_deletions.csv"), writer, "cnv_del")

    # 4) PGA
    pga = pd.to_numeric(df["pga"], errors="coerce")
    pga_hist = to_histogram_df(pga, np.arange(0, 110, 10), "Percentage(%)")
    pga_hist.to_excel(writer, sheet_name="pga", index=False)
    pga_hist.to_csv(out("pga_count.csv"), index=False)
    combined["pga"] = pga_hist

    # 5) Fusions
    fus = clean_blank(df["fusion_pairs"]).value_counts()
    if fus.empty:
        fus = pd.Series({"Blank": 0})
    combined["fusions"] = write_table(fus, "Fusion_Pair", out("fusion_count.csv"), writer, "fusions")

    # 6) TMB
    tmb = pd.to_numeric(df["TMB"], errors="coerce")
    tmb_hist = to_histogram_df(tmb, np.arange(0, 51, 1), "TMB_Range(Mb)")
    tmb_hist.to_excel(writer, sheet_name="tmb", index=False)
    tmb_hist.to_csv(out("tmb_count.csv"), index=False)
    combined["tmb"] = tmb_hist

    # 7) MSI
    def bucket(x):
        x = x.lower()
        if x == "mss": return "MSS"
        if x == "msi-h": return "MSI"
        if x == "inconclusive": return "Inconclusive"
        return "Blank"

    msi = df["msi_status"].astype(str).map(bucket).value_counts()
    if msi.empty:
        msi = pd.Series({"Blank": 0})
    combined["msi"] = write_table(msi, "MSI_Status", out("msi_summary.csv"), writer, "msi")

    # 8) HRD
    hrd = pd.to_numeric(df["hrd_value"], errors="coerce")
    hrd_hist = to_histogram_df(hrd, np.arange(0, 1.1, 0.1), "HRD_Value")
    hrd_hist.to_excel(writer, sheet_name="hrd", index=False)
    hrd_hist.to_csv(out("hrd_count.csv"), index=False)
    combined["hrd"] = hrd_hist

    # 9) Purity
    purity = pd.to_numeric(df["purity"], errors="coerce") * 100
    purity_hist = to_histogram_df(purity, np.arange(0, 110, 10), "Purity(%)")
    purity_hist.to_excel(writer, sheet_name="purity", index=False)
    purity_hist.to_csv(out("purity_count.csv"), index=False)
    combined["purity"] = purity_hist

