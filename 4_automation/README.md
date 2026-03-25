# Automate Pipeline
- Submit cron jobs to generate weekly/monthly...
    - Summary CSV files for Marimo
    - Key figures (i.e. HRD Coverage monthly, report counts weekly)
    - note: figures also generated in marimo

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
