# Visualizing the Data
Marimo notebook offers interactive UI for table-viewing and automatic plot generation. This allows for...
- View weekly count of completed reports by project
- View and filter summary table with specified column view
- Generate descriptive histograms and bar plots
- Generate complex case accrual plots by cohort, group, colour bar, etc
    - Ex: Cumulative case accrual in HRD cases by coverage

## Automate Pipeline
- Set up Olives to run weekly generation of summary.csv from CouchDB that:
    - Runs query pipeline
    - Obtains summary CSV
    - Inputs summary CSV into Marimo

## Requirements
```
pip install marimo
pip install "marimo[recommended]"
```

## Running the Notebook
```
marimo run couchDB_marimo.py
```
