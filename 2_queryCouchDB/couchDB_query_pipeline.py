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
import shutil

def run_step(name, cmd, log):
    start = time.time()
    result = subprocess.run(cmd, capture_output=True, text=True)
    end = time.time()
    duration = end - start

    log[name] = {
        "command": " ".join(cmd),
        "return_code": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
        "duration_sec": duration
    }

    print(f"--- Step {name} finished in {duration:.2f} sec ---")

    if result.returncode != 0:
        raise RuntimeError(f"{name} failed: {result.stderr}")

def main():
    start_all = time.time()
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
    base_out = paths["output_dir"]
    if not base_out: base_out = "."

    filtered_jsons_dir = os.path.join(base_out, "filtered_jsons")
    os.makedirs(base_out, exist_ok=True)

    if pipeline["run_retrieve"]:
        cmd = ["python3", "couchDB_dynamic_query.py",
               "--login_file", args.config,
               "--filters_file", args.config,
               "--output_dir", base_out]
        if filters["dynamic"].get("page_size") is not None:
            cmd += ["--page_size", str(filters["dynamic"]["page_size"])]
        if filters["dynamic"].get("count"):
            cmd += ["--count"]
        run_step("retrieve", cmd, log)

    if pipeline["run_variant"] and os.path.exists(filtered_jsons_dir):
        temp_variant_out = os.path.join(base_out, "temp_variant")
        cmd = ["python3", "couchDB_variant_search.py",
               "--input_dir", filtered_jsons_dir,
               "--output_dir", temp_variant_out]
        for key, val in filters["variant"].items():
            if val is not None:
                cmd += [f"--{key}", str(val)]
        run_step("variant", cmd, log)

        # Replace main filtered_jsons with variant-filtered ones
        temp_filtered = os.path.join(temp_variant_out, "filtered_jsons")
        if os.path.exists(temp_filtered):
            shutil.rmtree(filtered_jsons_dir)
            shutil.move(temp_filtered, filtered_jsons_dir)
            shutil.rmtree(temp_variant_out)

    if pipeline["run_numeric"] and os.path.exists(filtered_jsons_dir):
        temp_numeric_out = os.path.join(base_out, "temp_numeric")
        cmd = ["python3", "couchDB_numeric_analysis.py",
               "--input_dir", filtered_jsons_dir,
               "--output_dir", temp_numeric_out]
        if filters["numeric"].get("plot"):
             cmd += ["--plot_out", paths["plot_out"]]

        for key, val in filters["numeric"].items():
            if key == "plot":
                continue
            if val is not None:
                cmd += [f"--{key}", str(val)]
        if filters["numeric"].get("plot"):
            cmd += ["--plot"]
        run_step("numeric", cmd, log)

        # Replace main filtered_jsons with numeric-filtered ones
        temp_filtered = os.path.join(temp_numeric_out, "filtered_jsons")
        if os.path.exists(temp_filtered):
            shutil.rmtree(filtered_jsons_dir)
            shutil.move(temp_filtered, filtered_jsons_dir)
            shutil.rmtree(temp_numeric_out)

    if pipeline["run_summary"] and os.path.exists(filtered_jsons_dir):
        cmd = ["python3", "couchDB_summary.py",
            "--input_dir", filtered_jsons_dir,
            "--output_name", os.path.splitext(paths["summary_out"])[0]]
        run_step("summary", cmd, log)

    with open(paths["log_file"], "w") as f:
        json.dump(log, f, indent=2)

    duration = (time.time() - start_all) / 60
    print(f"\n=== Pipeline finished in {duration:.2f} min ===")

if __name__ == "__main__":
    main()