# Visualizing the Data
Marimo notebook offers interactive UI for table-viewing and automatic plot generation. This allows for...
- View weekly count of completed reports by project
- View and filter summary table with specified column view
- Generate descriptive histograms and bar plots
- Generate complex case accrual plots by cohort, group, colour bar, etc
    - Ex: Cumulative case accrual in HRD cases by coverage

## Guide
Guide on how to use Marimo can be found in the [presentation slides](../2_queryCouchDB/docs/GSI_presentation_0427.pdf). Presentation delivered on April 27th to GSI team with a demo on navigating data analysis. Demo has been annotated directly in the linked [slides](../2_queryCouchDB/docs/GSI_presentation_0427.pdf).

## Requirements
### Download Marimo
```
pip install marimo
pip install "marimo[recommended]"
```

### Run the Notebook
```
marimo run couchDB_marimo.py
```
