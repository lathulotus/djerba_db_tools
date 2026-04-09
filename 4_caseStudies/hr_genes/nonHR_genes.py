""" Top 25  non-HR genes in HRD cases containing no HR genes
  - Input: .csv of summary table (HRD cases) """


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def nonhr_count(df, col, hr_genes):
   counts = {}
   hr_set = set(g.upper() for g in hr_genes)

   for cell in df[col].dropna():
       for g in [x.strip().upper() for x in cell.split(",") if x.strip()]:
           if g not in hr_set:
               counts[g] = counts.get(g, 0) + 1
   return counts

def plot_nonhr(csv_hrd, hr_genes, top_n=25):
   df = pd.read_csv(csv_hrd)

   hr_set = set(g.upper() for g in hr_genes)
   def has_hr_variant(row):
       for col in ["snv_genes", "cnv_genes", "fusion_genes"]:
           if col in row and pd.notna(row[col]):
               genes = [x.strip().upper() for x in row[col].split(",") if x.strip()]
               if any(g in hr_set for g in genes):
                   return True
       return False

   df = df[~df.apply(has_hr_variant, axis=1)]

   snv = nonhr_count(df, "snv_genes", hr_genes)
   cnv = nonhr_count(df, "cnv_genes", hr_genes)

   all_genes = sorted(set(snv) | set(cnv))
   table = pd.DataFrame({
       "Gene": all_genes,
       "SNV": [snv.get(g, 0) for g in all_genes],
       "CNV": [cnv.get(g, 0) for g in all_genes]})

   table["Total"] = table["SNV"] + table["CNV"]
   table = table[table["Total"] > 0].sort_values("Total", ascending=False)
   table = table.head(top_n)

   # Plot
   x = np.arange(len(table))
   plt.figure(figsize=(12, 7))

   plt.bar(x, table["SNV"], 0.6, color="#7cb066ff", edgecolor="white", alpha=0.9, label="SNV")
   plt.bar(x, table["CNV"], 0.6, bottom=table["SNV"], color="#234c13ff", edgecolor="white", alpha=0.9,label="CNV")
   
   plt.xticks(x, table["Gene"], rotation=90)
   plt.xlabel("Non-HR Gene")
   plt.ylabel("Number of Cases")
   plt.title(f"Top 25 Non‑HR Genes in HRD Cases Absent of HR Gene Variants")
   plt.grid(True, linestyle=":", alpha=0.5)
   plt.legend()
   plt.tight_layout()
   plt.savefig("nonHR_genes_top25.png", dpi=300)
   plt.close()

   return table

# Test run: HRD cases against HR genes
genes = ["BRCA1","BRCA2","BRIP1","PALB2","RAD51","RAD51C","RAD51D","RAD50","MRE11","NBN","ATM","ATR","CHEK1","CHEK2","BARD1","FANCA","FANCB","FANCC","FANCD1","FANCD2","FANCE","FANCF","FANCG","FANCI","FANCJ","FANCL","FANCM","BLM","WRN","ERCC1","ERCC4","XPF","PTEN"]
plot_nonhr("summary_hrd.csv", genes)