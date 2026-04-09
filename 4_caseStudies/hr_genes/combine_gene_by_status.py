""" Compare variant (SNV, CNV) occurrences in HR Genes between HRP vs HRD cases 
    - Input: .csv of summary tables (HRD cases, HRP cases) """

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def count_genes(df, col, genes):
    counts = {g: 0 for g in genes}
    for cell in df[col].dropna():
        for g in [x.strip().upper() for x in cell.split(",") if x.strip()]:
            if g in counts:
                counts[g] += 1
    return counts

def plot_combine(csv1, csv2, genes):
    df1 = pd.read_csv(csv1)
    df2 = pd.read_csv(csv2)

    snv1 = count_genes(df1, "snv_genes", genes)
    snv2 = count_genes(df2, "snv_genes", genes)
    cnv1 = count_genes(df1, "cnv_genes", genes)
    cnv2 = count_genes(df2, "cnv_genes", genes)

    plot_df = pd.DataFrame({
        "Gene": genes,
        "SNV_HRD": [snv1[g] for g in genes],
        "CNV_HRD": [cnv1[g] for g in genes],
        "SNV_HRP": [snv2[g] for g in genes],
        "CNV_HRP": [cnv2[g] for g in genes]
    })

    x = np.arange(len(genes)) * 1.5
    plt.figure(figsize=(12,7))

    plt.bar(x - 0.3, plot_df["SNV_HRD"], 0.6, color="#7cb066ff", edgecolor="white", alpha=0.9, label="HRD SNV")
    plt.bar(x - 0.3, plot_df["CNV_HRD"], 0.6, bottom=plot_df["SNV_HRD"], color="#7cb066ff", edgecolor="white", alpha=0.9, hatch="////", label="HRD CNV")

    plt.bar(x + 0.3, plot_df["SNV_HRP"], 0.6, color="#234c13ff", edgecolor="white", alpha=0.9, label="HRP SNV")
    plt.bar(x + 0.3, plot_df["CNV_HRP"], 0.6, bottom=plot_df["SNV_HRP"], color="#234c13ff", edgecolor="white", alpha=0.9, hatch="////", label="HRP CNV")

    plt.xticks(x, genes, rotation=45, fontstyle="italic")
    plt.ylabel("Number of Cases")
    plt.gca().yaxis.set_major_locator(plt.MaxNLocator(integer=True))
    plt.title("Variant Occurrence per HR Gene in HR Deficient vs Proficient Cases")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend(ncol=2)
    plt.tight_layout()
    plt.savefig("combined_plot.png", dpi=300)
    plt.close()


# Test run: HRD cases against HR genes
genes = ["BRCA1","BRCA2","BRIP1","PALB2","RAD51","RAD51C","RAD51D","RAD50","MRE11","NBN","ATM","ATR","CHEK1","CHEK2","BARD1","FANCA","FANCB","FANCC","FANCD1","FANCD2","FANCE","FANCF","FANCG","FANCI","FANCJ","FANCL","FANCM","BLM","WRN","ERCC1","ERCC4","XPF","PTEN"]
plot_combine("summary_hrd.csv", "summary_hrp.csv", genes)