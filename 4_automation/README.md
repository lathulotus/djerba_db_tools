# Automate Pipeline
- Set up Olives to run weekly generation of summary.csv from CouchDB
    - Run query pipeline
    - Obtain summary CSV
    - Input summary CSV into Marimo

# Marimo Notebook
- Interactive UI for tables and plots
    - Input specific report/donor IDs
    - Change summary table columns (i.e., filter values/view)
    - Automatically change plots
- Generate various plots from summary.csv
    - Case accrual in [parameter 1] by [parameter 2] (i.e., HRD by coverage, project by gene)

## Requirements
```
pip install marimo
pip install "marimo[recommended]"
```

## Running the Notebook
```
marimo run couchDB_marimo.py
```
