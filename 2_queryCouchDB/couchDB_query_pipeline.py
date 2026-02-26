"""
Wrapper script thhat searches through CouchDB, retrieve reports, and filters for analysis.
    1. couchDB_dynamic_query.py: Run mango query using string-based filters to retrieve reports.
    2. couchDB_variant_search.py: Run variant-based filtering to output a subset of reports.
    3. couchDB_numeric_analysis.py: Run numeric filtering on reports and output subset of reports and plot.
    4. couchDB_summary.py: Returns summary table of all findings (and allows for plotting)
Usage:
    python3 couchDB_query_pipeline.py --config couchDB_query_pipeline.yaml
"""

import json
import os
import yaml
import argparse
import time
import subprocess

def run_step(name, cmd, log):
    start = time.time()
    result = subprocess.run(cmd, capture_output=True, text=True)
    end = time.time()

    log[name] = {
        "command": " ".join(cmd),
        "return_code": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
        "duration_sec": (end - start)
    }

    if result.returncode != 0:
        raise RuntimeError(f"{name} failed: {result.stderr}")
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True, help="Query pipeline configuration as YAML file")
    args = parser.parse_args()
    
    with open(args.config, "r") as f:
        config = yaml.safe_load(f)
    
    log = {}
    paths = config["paths"]
    filters = config["filters"]
    login = config["login_file"]
    pipeline = config["query_pipeline"]
    
    os.makedirs(paths["extract_out"], exist_ok=True)
    os.makedirs(paths["numeric_out"], exist_ok=True)
    os.makedirs(paths["variant_out"], exist_ok=True)
    os.makedirs(paths["plot_out"], exist_ok=True)
    
    login_file_path = os.path.join(paths["extract_out"], "login.yaml")
    dynamic_filters_path = os.path.join(paths["extract_out"], "dynamic_filters.yaml")

    with open(login_file_path, "w") as f:
        yaml.dump(login, f)
    with open(dynamic_filters_path, "w") as f:
        yaml.dump(filters["dynamic"], f)
    
    if pipeline["run_extract"]:
        cmd = ["python3", "couchDB_dynamic_query.py",
               "--login_file", login_file_path,
               "--filters_file", dynamic_filters_path,
               "--output_dir", paths["extract_out"]]
        if filters["dynamic"].get("page_size") is not None:
            cmd += ["--page_size", str(filters["dynamic"]["page_size"])]
        if filters["dynamic"].get("count"):
            cmd += ["--count"]
        run_step("extract", cmd, log)
    
    if pipeline["run_numeric"]:
        cmd = ["python3", "couchDB_numeric_analysis.py",
               "--input_dir", paths["extract_out"],
               "--output_dir", paths["numeric_out"]]
        for key, val in filters["numeric"].items():
            if key == "plot":
                continue
            if val is not None:
                cmd += [f"--{key}", str(val)]
        if filters["numeric"].get("plot"):
            cmd += ["--plot"]
        run_step("numeric", cmd, log)
    
    if pipeline["run_variant"]:
        cmd = ["python3", "couchDB_variant_search.py",
               "--input_dir", paths["numeric_out"],
               "--output_dir", paths["variant_out"]]
        for key, val in filters["variant"].items():
            if val is not None:
                cmd += [f"--{key}", str(val)]
        run_step("variant", cmd, log)
    
    if pipeline["run_summary"]:
        cmd = ["python3", "couchDB_summary.py",
            "--input_dir", paths["numeric_out"],
            "--output_name", paths["summary_out"]]
        run_step("summary", cmd, log)

    if pipeline["run_plot"]:
        cmd = ["python3", "couchDB_plot.py",
               "--summary_table", paths["summary_out"],
               "--plot_config", args.config,
               "--output_dir", paths["plot_out"]]
        run_step("plot", cmd, log)
    
    with open(paths["log_file"], "w") as f:
        json.dump(log, f, indent=2)

if __name__ == "__main__":
    main()