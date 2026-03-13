""" Occurrences of top four pancreatic cancer genes (KRAS, TP53, CDKN2A, SMAD4) 
    - Input: .csv of summary table (all PRSPR) """

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

def plot_topgenes(csv):
    df = pd.read_csv(csv)
    genes = ["KRAS", "TP53", "CDKN2A", "SMAD4"]
    total_cases = len(df)

    snv = count_genes(df, "snv_genes", genes)
    cnv = count_genes(df, "cnv_genes", genes)

    table = pd.DataFrame({
       "Gene": genes,
       "SNV": [snv.get(g, 0) for g in genes],
       "CNV": [cnv.get(g, 0) for g in genes]})
    
    table["Total"] = table["SNV"] + table["CNV"]
    table["Percent"] = (table["Total"] / total_cases) * 100

    # Plot
    x = np.arange(len(genes))
    plt.figure(figsize=(12, 7))

    plt.bar(x, table["SNV"], 0.6, color="thistle", edgecolor="white", alpha=0.9, label="SNV")
    plt.bar(x, table["CNV"], 0.6, bottom=table["SNV"], color="indigo", edgecolor="white", alpha=0.9,label="CNV")

    for index, row in table.iterrows():
        plt.text(index, row["Total"] + 0.5, f"{round(row['Percent'], 2)}%", ha="center", va="bottom", fontsize=9)
    
    plt.xticks(x, genes)
    plt.xlabel("Candidate Genes")
    plt.ylabel("Number of Cases")
    plt.title(f"Recurrence of Key Pancreatic Cancer Genes in PRSPR Cases")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig("gene_recurrence.png", dpi=300)
    plt.close()

    return table

plot_topgenes("summary_prspr.csv")