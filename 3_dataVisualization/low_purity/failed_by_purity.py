""" Assess rate of failed reporty due to purity threshold """

import pandas as pd
import argparse

def main():
    parser = argparse.ArgumentParser(description="Calculate low-purity failure rate.")
    parser.add_argument("--input_csv", required=True, help="Path to summary CSV file")
    parser.add_argument("--threshold", type=float, default=0.30, help="Purity threshold (defaults to 0.30)")
    args = parser.parse_args()

    df = pd.read_csv(args.input_csv)
    df_purity = df[(df["purity"].notna()) & (df["purity"].astype(str).str.strip() != "")]
    df_purity["purity"] = df_purity["purity"].astype(float)

    failed_purity = df_purity[(df_purity["purity"] < args.threshold) & (df_purity["failed"] == True)]
    total_failed_purity = len(failed_purity)
    total_all = len(df_purity)
    failure_rate = (total_failed_purity / total_all) * 100

    print(f"Input CSV: {args.input_csv}")
    print(f"Purity threshold: {args.threshold}")
    print(f"Total low-purity fails: {total_failed_purity}")
    print(f"Total reports (all): {total_all}")
    print(f"Percentage: {round(failure_rate, 2)}%")

if __name__ == "__main__":
    main()
