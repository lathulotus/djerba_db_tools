""" Summary tables and figures
python3 distribution_full.py --summary_csv input.csv --output_dir output_folder/
"""
import os
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description="Summary CSV to figures/summary tables")
parser.add_argument("--summary_csv", required=True, help="Path to CSV")
parser.add_argument("--output_dir", required=False, default='.', help="Output directory path")
args = parser.parse_args()

os.makedirs(args.output_dir, exist_ok=True)
def out(path):
    return os.path.join(args.output_dir, path)

df = pd.read_csv(args.summary_csv)
combined = {}

# Clean up OncoTree field
df["oncotree_code"] = df["oncotree_code"].apply(lambda x: "Other" if isinstance(x, str) and " " in x else x)
df["oncotree_code"] = df["oncotree_code"].astype(str).replace({"nan": "Blank", "": "Blank", "None": "Blank"})

# Count number of cases (blank and non-blank rows)
def count_nonblank(series):
    s = series.astype(str).str.strip()
    return (s != "").sum()
def count_blank(series):
    s = series.astype(str).str.strip()
    return (s = "").sum()

# Create figures and cleaned summary table
with pd.ExcelWriter(out("summary_clean.xlsx")) as writer:
    # 1) OncoTree
    oncotree_counts = df["oncotree_code"].fillna("Blank").value_counts()
    if oncotree_counts.empty:
        oncotree_counts = pd.Series({"Blank": 0})

    oncotree_counts = oncotree_counts.rename("Count").reset_index()
    oncotree_counts.columns = ["OncoTree_Code", "Count"]

    oncotree_counts.to_csv(out("oncotree_count.csv"), index=False)
    oncotree_counts.to_excel(writer, sheet_name="oncotree_count", index=False)
    combined["oncotree_count"] = oncotree_counts

    # 2) SNV
    snv = df["snv_genes"].fillna("Blank").astype(str).str.split(",").explode().str.strip()
    snv = snv.replace({"": "Blank"})
    snv_counts = snv.value_counts()
    if snv_counts.empty:
        snv_counts = pd.Series({"Blank": 0})

    snv_counts = snv_counts.rename("Count").reset_index()
    snv_counts.columns = ["SNV_Gene", "Count"]

    snv_counts.to_csv(out("snv_count.csv"), index=False)
    snv_counts.to_excel(writer, sheet_name="snv_count", index=False)
    combined["snv_count"] = snv_counts

    # 3) CNV
    genes = df["cnv_genes"].fillna("Blank").astype(str).str.split(",").explode().str.strip()
    types = df["cnv_types"].fillna("Blank").astype(str).str.split(",").explode().str.strip()
    genes = genes.replace({"": "Blank"})
    types = types.replace({"": "Blank"})
    cnv_df = pd.DataFrame({"Gene": genes, "Type": types}).dropna()

    amps = cnv_df[cnv_df["Type"].str.lower() == "amplification"]["Gene"].value_counts()
    dels = cnv_df[cnv_df["Type"].str.lower() == "deletion"]["Gene"].value_counts()

    if amps.empty:
        amps = pd.Series({"Blank": 0})
    if dels.empty:
        dels = pd.Series({"Blank": 0})

    amps = amps.rename("Count").reset_index()
    amps.columns = ["CNV_Amplification_Gene", "Count"]

    dels = dels.rename("Count").reset_index()
    dels.columns = ["CNV_Deletion_Gene", "Count"]

    amps.to_csv(out("cnv_amplification.csv"), index=False)
    dels.to_csv(out("cnv_deletions.csv"), index=False)
    amps.to_excel(writer, sheet_name="cnv_amp", index=False)
    dels.to_excel(writer, sheet_name="cnv_del", index=False)
    combined["cnv_amp"] = amps
    combined["cnv_del"] = dels

    # 4) PGA
    pga = pd.to_numeric(df["pga"], errors="coerce")
    bins = np.arange(0, 110, 10)
    counts, edges = np.histogram(pga.dropna(), bins=bins)

    pga_hist = pd.DataFrame({
        "Percentage(%)": [f"{edges[i]:.0f}-{edges[i+1]:.0f}" for i in range(len(counts))],
        "Count": counts
    })

    pga_hist.to_excel(writer, sheet_name="pga", index=False)
    combined["pga_histogram"] = pga_hist

    plt.figure(figsize=(12,7))
    plt.bar(pga_hist["Percentage(%)"], pga_hist["Count"], color="steelblue", edgecolor="white", alpha=0.9)
    plt.title("Distribution of Cases by Percent Genome Altered")
    plt.xlabel("Percentage (%)")
    plt.ylabel("Count")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(out("pga_histogram.png"))
    plt.close()

    # 5) Fusions
    fusions = df["fusion_pairs"].fillna("Blank").astype(str).str.split(",").explode().str.strip()
    fusions = fusions.replace({"": "Blank"})
    fusion_counts = fusions.value_counts()
    if fusion_counts.empty:
        fusion_counts = pd.Series({"Blank": 0})

    fusion_counts = fusion_counts.rename("Count").reset_index()
    fusion_counts.columns = ["Fusion_Pair", "Count"]

    fusion_counts.to_csv(out("fusion_count.csv"), index=False)
    fusion_counts.to_excel(writer, sheet_name="fusions", index=False)
    combined["fusion_count"] = fusion_counts

    # 6) TMB
    tmb = pd.to_numeric(df["tmb_value"], errors="coerce")
    bins = np.arange(0, 51, 1)
    counts, edges = np.histogram(tmb.dropna(), bins=bins)

    tmb_hist = pd.DataFrame({
        "TMB_Range(Mb)": [f"{edges[i]:.0f}-{edges[i+1]:.0f}" for i in range(len(counts))],
        "Count": counts
    })

    tmb_hist.to_excel(writer, sheet_name="tmb", index=False)
    combined["tmb_histogram"] = tmb_hist

    plt.figure(figsize=(12,7))
    plt.bar(tmb_hist["TMB_Range(Mb)"], tmb_hist["Count"], color="steelblue", edgecolor="white", alpha=0.9)
    plt.title("Distribution of Cases by TMB per Mb (1-50 mut/Mb)")
    plt.xlabel("TMB Range (per Mb)")
    plt.ylabel("Count")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(out("tmb_histogram.png"))
    plt.close()

    # 7) MSI
    status = df["msi_status"].astype(str).str.strip().str.lower()
    def bucket(x):
        if x in ["mss", "MSS"]: return "MSS"
        if x in ["msi-h", "MSI-H"]: return "MSI"
        if x in ["inconclusive", "INCONCLUSIVE"]: return "Inconclusive"
        return "Blank"

    msi_summary = status.map(bucket).value_counts()
    if msi_summary.empty:
        msi_summary = pd.Series({"Blank": 0})

    msi_summary = msi_summary.rename("Count").reset_index()
    msi_summary.columns = ["MSI_Status", "Count"]

    msi_summary.to_csv(out("msi_summary.csv"), index=False)
    msi_summary.to_excel(writer, sheet_name="msi", index=False)
    combined["msi_summary"] = msi_summary

    plt.figure(figsize=(12,7))
    plt.bar(msi_summary["MSI_Status"], msi_summary["Count"], color="steelblue", edgecolor="white", alpha=0.9)
    plt.title("Distribution of Cases by MSI Status")
    plt.xlabel("MSI Status")
    plt.ylabel("Count")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.tight_layout()
    plt.savefig(out("msi_summary.png"))
    plt.close()

    # 8) HRD
    hrd = pd.to_numeric(df["hrd_value"], errors="coerce")
    bins = np.arange(0, 1.1, 0.1)
    counts, edges = np.histogram(hrd.dropna(), bins=bins)

    hrd_hist = pd.DataFrame({
        "HRD_Value": [f"{edges[i]:.1f}-{edges[i+1]:.1f}" for i in range(len(counts))],
        "Count": counts
    })

    hrd_hist.to_excel(writer, sheet_name="hrd", index=False)
    combined["hrd_histogram"] = hrd_hist

    plt.figure(figsize=(12,7))
    plt.bar(hrd_hist["HRD_Value"], hrd_hist["Count"], color="steelblue", edgecolor="white", alpha=0.9)
    plt.title("Distribution of Cases by HRD Score")
    plt.xlabel("HRD Value")
    plt.ylabel("Count")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(out("hrd_histogram.png"))
    plt.close()

    # 9) Purity
    purity = pd.to_numeric(df["purity"], errors="coerce") * 100
    bins = np.arange(0, 110, 10)
    counts, edges = np.histogram(purity.dropna(), bins=bins)

    purity_hist = pd.DataFrame({
        "Purity(%)": [f"{edges[i]:.0f}-{edges[i+1]:.0f}" for i in range(len(counts))],
        "Count": counts
    })

    purity_hist.to_excel(writer, sheet_name="purity", index=False)
    combined["purity_histogram"] = purity_hist

    plt.figure(figsize=(12,7))
    plt.bar(purity_hist["Purity(%)"], purity_hist["Count"], color="steelblue", edgecolor="white", alpha=0.9)
    plt.title("Distribution of Cases by Tumour Purity")
    plt.xlabel("Purity (%)")
    plt.ylabel("Count")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(out("purity_histogram.png"))
    plt.close()

    # Total counts sheet
    totals = pd.DataFrame({
        "Parameters": ["oncotree_code", "snv_count", "cnv_amp", "cnv_del", "pga", "fusion", "tmb", "msi", "hrd", "purity"],
        "Total_Cases": [count_nonblank(df["oncotree_code"]), count_nonblank(df["snv_genes"]), count_nonblank(df["cnv_genes"]), count_nonblank(df["cnv_genes"]), count_nonblank(df["pga"]), count_nonblank(df["fusions"]), count_nonblank(df["tmb_value"]), count_nonblank(df["msi_status"]), count_nonblank(df["hrd_value"]), count_nonblank(df["purity"])],
        "Total_Blanks": [count_blank(df["oncotree_code"]), count_blank(df["snv_genes"]), count_blank(df["cnv_genes"]), count_blank(df["cnv_genes"]), count_blank(df["pga"]), count_blank(df["fusions"]), count_blank(df["tmb_value"]), count_blank(df["msi_status"]), count_blank(df["hrd_value"]), count_blank(df["purity"])]
    })

    totals.to_excel(writer, sheet_name="totals", index=False)
