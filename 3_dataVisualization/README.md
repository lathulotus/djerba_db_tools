# Data Aggregation & Cohort Level Summaries
- Extract and normalize key variables across reports:
    - Cancer type
    - Key mutations (e.g., KRAS)
    - Biomarkers (HRD, MSI-H, TMB, their scores)
    - Residual disease 
- Build aggregation logic to produce:
    - Counts and proportions
    - Summaries by cancer type or project or report category

Deliverables
- Cleaned tabular dataset derived from CouchDB
- Aggregation scripts
- Summary figures/tables suitable for presentation

<br>

## Accrual by Coverage
Plotting number of cases accumulated by quarter, with mean coverage (per case) being mapped.
![Accumutated Total](accrual_by_coverage/coverage_over_time_combine.png)

Allows for plotting the percentage for better visual of ratios. Intervals can be set to daily or monthly, with date ranges also being specified for total view of close-up snapshot.
![Accumutated Total with Percentage](accrual_by_coverage/coverage_overseq_monthly.png)

<br>

## Distribution by Parameters
Plotting number of cases by parameter as histograms.
![PGA Passed](distribution_by_field/histogram_purity_passed.png)

Distribution plots can allow for view of non-numerical bins.
![MSI Status Passed](distribution_by_field/histogram_msi.png)

<br>

## Distribution by Combined Parameters
Plotting the number of occurrences of variants (SNV, CNV) in the HR gene by HR status (HRD, HRP).
![HR Genes](hr_genes/combined_plot.png)

