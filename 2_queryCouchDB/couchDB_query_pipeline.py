"""
Wrapper script: retrieve -> variant? -> numeric? -> summary
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

def latest_output(folders):
    """ Search for latest output folder containing JSON files """
    for folder in folders:
        if any(f.endswith(".json") for f in os.listdir(folder)):
            return folder
    return None

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
    
    os.makedirs(paths["retrieve_out"], exist_ok=True)
    os.makedirs(paths["numeric_out"], exist_ok=True)
    os.makedirs(paths["variant_out"], exist_ok=True)
    
    #login_file_path = os.path.join(paths["retrieve_out"], "login.yaml")
    dynamic_filters_path = os.path.join(paths["retrieve_out"], "dynamic_filters.yaml")

    #with open(login_file_path, "w") as f:
        #yaml.dump(login, f)
    with open(dynamic_filters_path, "w") as f:
        yaml.dump(filters["dynamic"], f)
    
    if pipeline["run_retrieve"]:
        cmd = ["python3", "couchDB_dynamic_query.py",
               "--login_file", args.config,
               "--filters_file", dynamic_filters_path,
               "--output_dir", paths["retrieve_out"]]
        if filters["dynamic"].get("page_size") is not None:
            cmd += ["--page_size", str(filters["dynamic"]["page_size"])]
        if filters["dynamic"].get("count"):
            cmd += ["--count"]
        run_step("retrieve", cmd, log)
    
    variant_input = latest_output([paths["numeric_out"], paths["retrieve_out"]])
    if pipeline["run_variant"] and variant_input:
        cmd = ["python3", "couchDB_variant_search.py",
               "--input_dir", variant_input,
               "--output_dir", paths["variant_out"]]
        for key, val in filters["variant"].items():
            if val is not None:
                cmd += [f"--{key}", str(val)]
        run_step("variant", cmd, log)
    
    numeric_input = latest_output([paths["variant_out"], paths["retrieve_out"]])
    if pipeline["run_numeric"] and numeric_input:
        cmd = ["python3", "couchDB_numeric_analysis.py",
               "--input_dir", numeric_input,
               "--output_dir", paths["numeric_out"]]
        for key, val in filters["numeric"].items():
            if key == "plot":
                continue
            if val is not None:
                cmd += [f"--{key}", str(val)]
        if filters["numeric"].get("plot"):
            cmd += ["--plot"]
        run_step("numeric", cmd, log)
     
    summary_input = latest_output([paths["numeric_out"], paths["variant_out"], paths["retrieve_out"]])
    if pipeline["run_summary"] and summary_input:
        cmd = ["python3", "couchDB_summary.py",
            "--input_dir", summary_input,
            "--output_name", os.path.splitext(paths["summary_out"])[0]]
        run_step("summary", cmd, log)
    
    with open(paths["log_file"], "w") as f:
        json.dump(log, f, indent=2)

if __name__ == "__main__":
    main()
    