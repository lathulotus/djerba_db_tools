"""
Create plots from filtered report summary tables

Usage:
    python3 couchDB_plot.py --summary_table summary.csv --plot_config couchDB_plot_config.yaml --output_dir figures/
"""

import os
import yaml
import pandas as pd
import matplotlib.pyplot as plt
import argparse

def read_yaml(path):
    with open(path) as f:
        return yaml.safe_load(f)

def apply_filters(df, filters):
    if not filters:
        return df
    for k, v in filters.items():
        if k in df.columns and v is not None:
            df = df[df[k] >= v] if isinstance(v, (int, float)) else df[df[k].astype(str).str.lower() == str(v).lower()]
    return df

def fmt(name):
    return "" if not name else " ".join(w.capitalize() for w in name.replace("_", " ").split())

def generate_plot(df, cfg):
    if df.empty:
        print("No data to plot.")
        return

    x = cfg["x"]
    df[x] = pd.to_datetime(df[x].astype(str), errors="coerce")
    df = df.sort_values(x)

    color_by = cfg.get("color_by", "coverage")
    data_min = df[color_by].min()
    data_max = df[color_by].max()
    color_min = cfg.get("color_min", data_min)
    color_max = cfg.get("color_max", data_max)

    plt.figure(figsize=(12, 7))

    handles, labels = [], []
    for g in cfg.get("line_groups", []):
        label = g.get("label", "Group")
        marker = g.get("marker", "o")
        expr = g.get("filter")

        sub = df.query(expr) if expr else df
        if sub.empty:
            continue

        grp = sub.groupby(x).size().reset_index(name="Case_Count")
        grp["Avg_Value"] = sub.groupby(x)[color_by].mean().values
        grp["Cumulative_Count"] = grp["Case_Count"].cumsum()

        plt.plot(grp[x], grp["Cumulative_Count"], color="steelblue", linewidth=2, alpha=0.5)

        sc = plt.scatter(
            grp[x], grp["Cumulative_Count"],
            c=grp["Avg_Value"],
            cmap=cfg.get("colormap", "viridis"),
            s=100,
            alpha=0.9,
            edgecolors="w",
            vmin=color_min,
            vmax=color_max,
            marker=marker
        )

        sc.set_label(label)
        handles.append(sc)
        labels.append(label)

    if handles:
        cbar = plt.colorbar(handles[-1])
        cbar.set_label(cfg.get("color_legend_label", fmt(color_by)))
        plt.legend(handles, labels, title=cfg.get("group_legend_label", "Groups"))

    if cfg.get("x_min") is not None or cfg.get("x_max") is not None:
        plt.xlim(cfg.get("x_min"), cfg.get("x_max"))
    if cfg.get("y_min") is not None or cfg.get("y_max") is not None:
        plt.ylim(cfg.get("y_min"), cfg.get("y_max"))

    plt.title(cfg.get("title", "Cumulative Case Accrual Over Time"))
    plt.xlabel(cfg.get("x_label", fmt(x)))
    plt.ylabel(cfg.get("y_label", "Total Number of Cases (Cumulative)"))
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(cfg["output_file"])
    print(f"Plot saved to: {cfg['output_file']}")
    plt.close()

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--summary_table", required=True)
    p.add_argument("--plot_config", required=True)
    p.add_argument("--output_dir", default="figures")
    args = p.parse_args()

    cfg = read_yaml(args.plot_config)
    df = pd.read_csv(args.summary_table)
    df = apply_filters(df, cfg.get("filters"))

    os.makedirs(args.output_dir, exist_ok=True)
    cfg.setdefault("output_file", os.path.join(args.output_dir, "plot.png"))

    generate_plot(df, cfg)

if __name__ == "__main__":
    main()
