#!/bin/bash
cd ./queryTest

# Run pipeline to generate master summary (CSV)
python3 couchDB_query_pipeline.py --config couchDB_query_pipeline.yaml
rm -rf filtered_jsons/

# Copy summary.csv to Marimo notebook
cp output/summary.csv ./couchDB_marimo.py

# Runs weekly (Fri @ 6PM)
# 0 18 * * 5 ./couchDB_autopipeline.sh