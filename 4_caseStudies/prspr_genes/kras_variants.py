""" KRAS-specific variant recurrence in PRSPR cases 
    - Input: .csv of summary table (all PRSPR) """

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def extract_variants(df, gene):
    gene = gene.upper()
    variants = []

    for _, row in df.iterrows():
        if pd.isna(row["snv_genes"]) or pd.isna(row["snv_protein"]):
            continue
    
        genes = [g.strip().upper() for g in row["snv_genes"].split(",")]
        variant = [p.strip() for p in row["snv_protein"].split(",")]

        if len(genes) != len(variant):
            continue

        for g, v in zip(genes, variant):
            if g == gene:
                variants.append(v)
    return variants

def count_variants(vars):
    counts = {}
    for v in vars:
        counts[v] = counts.get(v, 0) + 1
    return counts

def plot_variants(csv):
    df = pd.read_csv(csv)
    total_cases = len(df)

    variants = extract_variants(df, "KRAS")
    counts = count_variants(variants)
    variant_names = list(counts.keys())
    values = list(counts.values())
    percentage = [(v/total_cases)*100 for v in values]

    # Plot
    x = np.arange(len(variant_names))
    plt.figure(figsize=(12, 7))

    plt.bar(x, values, 0.6, color="#7cb066ff", edgecolor="white", alpha=0.9)

    for index, (count, percent) in enumerate(zip(values, percentage)):
        plt.text(index, count + 0.3, f"{round(percent, 2)}%", ha="center", va="bottom", fontsize=9)
    
    plt.xticks(x, variant_names, rotation=45, ha="right")
    plt.xlabel("Recurring Variants")
    plt.ylabel("Number of Cases")
    plt.title(f"Recurrence of KRAS SNVs in PRSPR Cases")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.tight_layout()
    plt.savefig("kras_variant_recurrence.png", dpi=300)
    plt.close()

    return counts

plot_variants("summary_prspr.csv")