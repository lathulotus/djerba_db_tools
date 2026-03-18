""" Assess rate of failed reporty due to purity threshold """

import pandas as pd
import argparse
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser(description="Calculate low-purity failure rate.")
    parser.add_argument("--input_csv", required=True, help="Path to summary CSV file")
    args = parser.parse_args()

    df = pd.read_csv(args.input_csv)
    df_purity = df[(df["purity"].notna()) & (df["purity"].astype(str).str.strip() != "")]
    df_purity["purity"] = df_purity["purity"].astype(float)

    failed_purity = df_purity[(df_purity["purity"] < 0.3) & (df_purity["failed"] == True)]
    total_failed_purity = len(failed_purity)
    total_all = len(df_purity)
    failure_rate = (total_failed_purity / total_all) * 100

    print(f"Input CSV: {args.input_csv}")
    print(f"Total low-purity fails: {total_failed_purity}")
    print(f"Total reports (all): {total_all}")
    print(f"Percentage: {round(failure_rate, 2)}%")


    # Plot
    project_counts = (df_purity[df_purity["purity"] < 0.3].groupby("project").size().reset_index(name="low_purity_fails"))
    print(f"Low purity fails by project:\n {project_counts.to_string(index=False)}")
    
    project_totals = (df_purity.groupby("project").size().reset_index(name="total_reports"))
    merged = project_totals.merge(project_counts, on="project", how="left")
    merged["low_purity_fails"] = merged["low_purity_fails"].fillna(0).astype(int)
    merged["other_reports"] = merged["total_reports"]-merged["low_purity_fails"]
    merged["percent_low_purity"] = (merged["low_purity_fails"]/merged["total_reports"]) * 100
    merged = merged[merged["low_purity_fails"] > 0]
    merged = merged.reset_index(drop=True)
    
    plt.figure(figsize=(12,7))
    plt.bar(merged["project"], merged["low_purity_fails"], label="Low-purity fails", color="indigo")
    plt.bar(merged["project"], merged["other_reports"], bottom=merged["low_purity_fails"], label="Total reports", color="thistle")
    plt.xlabel("project")
    plt.ylabel("Report Count")
    plt.title("Low-Purity Failures by project (purity < 0.3)")
    plt.xticks(rotation=45, ha="right")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend()
    for index, row in merged.iterrows():
        plt.text(index, row["total_reports"] + 0.5, f"{round(row['percent_low_purity'], 2)}%", ha="center", va="bottom", fontsize=9)
    plt.tight_layout()
    plt.savefig("lowpurityfail_by_project.png", dpi=300)
    plt.close()

if __name__ == "__main__":
    main()
