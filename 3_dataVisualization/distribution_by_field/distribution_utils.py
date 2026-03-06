""" Helper functions for data cleaning and plotting """

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def clean_oncotree(series):
    series = series.apply(lambda x: "Other" if isinstance(x, str) and " " in x else x)
    return series.astype(str).replace({"nan": "Blank", "": "Blank", "None": "Blank"})

def clean_blank(series):
    s = series.fillna("Blank").astype(str).str.split(",").explode().str.strip()
    return s.replace({"": "Blank"})

def to_histogram_df(values, bins, label):
    counts, edges = np.histogram(values.dropna(), bins=bins)
    ranges = [f"{edges[i]:.0f}-{edges[i+1]:.0f}" for i in range(len(counts))]
    return pd.DataFrame({label: ranges, "Count": counts})

def write_table(df, index_name, csv_path, excel_writer, sheet_name):
    df = df.rename("Count").reset_index()
    df.columns = [index_name, "Count"]
    df.to_csv(csv_path, index=False)
    df.to_excel(excel_writer, sheet_name=sheet_name, index=False)
    return df

def plot_bar(x, y, title, xlabel, ylabel, output_path, rotation=45):
    plt.figure(figsize=(12, 7))
    plt.bar(x, y, color="steelblue", edgecolor="white", alpha=0.9)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.xticks(rotation=rotation)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
