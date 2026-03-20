# How to Format the Pipeline Config YAML
#### Table of Contents
1. [Run Retrieve: Searching by Assay Type](#example-1-searching-by-assay-type)
2. [Run Variant: Searching by SNV Genes](#example-2-searching-for-pms2-snvs)
3. [Run Numeric: Searching by Failed Purity](#example-3-searching-by-failed-purity)
4. [Stacking Filters](#example-4-stacking-filters)

## Example 1: Searching by Assay Type
- Scenario: Filtering for WGTS and WGS cases
- Output: All WGTS and WGS cases (JSON files), and a summary.csv
- Application: Can be applied to any other scenarios that simply query through run_retrieve
```
query_pipeline:
  run_retrieve: true
  run_variant: false
  run_numeric: false
  run_summary: true

paths:
  output_dir: output/
  plot_out: output/coverage_over_time.png
  summary_out: output/summary.csv
  log_file: output/pipeline_log.json

login_file:
  host: URL
  port: 0000
  db_name: DB_NAME
  username: USERNAME
  password: PASSWORD

filters:
  dynamic:
    report_id: 
    donor: 
    project: 
    study: 
    report_type: 
    failed: 
    cancer_type: 
    oncotree_code: 
    assay: ["WGTS", "WGS"]
    biopsy_site: 
    sample_type: 
    tmb_status: 
    hrd_status: 
    msi_status: 

    count: 

  variant:
    cnv_gene: 
    cnv_type: 
    snv_gene: 
    snv_type: 
    snv_protein: 
    fusion_gene: 
    fusion_effect: 
    fusion_frame: 

    ctdna_status: 
    ctdna_cnv: 
    ctdna_snv: 

  numeric:
    djerba_version: 
    date_reported: 
    coverage: 
    purity: 
    callability: 
    ploidy: 
    TMB: 
    TMB_value: 
    HRD_value: 
    MSI_value: 
    pga: 
    cnv_clinical: 
    snv_oncogenic: 
    fusion_clinical: 

    plot: 
```

<br>

## Example 2: Searching for PMS2 OR MSH2 SNVs
- Scenario: Filtering for cases with SNVs in either *PMS2* or *MSH2*
- Output: All cases with SNVs in *PMS2* or *MSH2* (JSON files), and a summary.csv
- Application: Can be applied to any other scenarios that simply query through run_variant
- Note: run_retrieve must be set to true! Setting all values under run_retrieve to "" (blank or `null`) allows for all reports to be downloaded for variant filtering.
```
query_pipeline:
  run_retrieve: true
  run_variant: true
  run_numeric: false
  run_summary: true

paths:
  output_dir: output/
  plot_out: output/coverage_over_time.png
  summary_out: output/summary.csv
  log_file: output/pipeline_log.json

login_file:
  host: URL
  port: 0000
  db_name: DB_NAME
  username: USERNAME
  password: PASSWORD

filters:
  dynamic:
    report_id: 
    donor: 
    project: 
    study: 
    report_type: 
    failed: 
    cancer_type: 
    oncotree_code: 
    assay: 
    biopsy_site: 
    sample_type: 
    tmb_status: 
    hrd_status: 
    msi_status: 

    count: 

  variant:
    cnv_gene: 
    cnv_type: 
    snv_gene: ["PMS2", "MSH2"]
    snv_type: 
    snv_protein: 
    fusion_gene: 
    fusion_effect: 
    fusion_frame: 

    ctdna_status: 
    ctdna_cnv: 
    ctdna_snv: 

  numeric:
    djerba_version: 
    date_reported: 
    coverage: 
    purity: 
    callability: 
    ploidy: 
    TMB: 
    TMB_value: 
    HRD_value: 
    MSI_value: 
    pga: 
    cnv_clinical: 
    snv_oncogenic: 
    fusion_clinical: 

    plot: 
```

<br>

## Example 3: Searching by Failed Purity
- Scenario: Filtering for cases with failed purity (less than or equal to 30%)
- Output: All cases with failed purity, and a summary.csv
- Application: Can be applied to any other scenarios that simply query through run_numeric
- Note: run_retrieve must be set to true! Setting all values under run_retrieve to "" (blank or `null`) allows for all reports to be downloaded for numeric filtering.
```
query_pipeline:
  run_retrieve: true
  run_variant: false
  run_numeric: true
  run_summary: true

paths:
  output_dir: output/
  plot_out: output/coverage_over_time.png
  summary_out: output/summary.csv
  log_file: output/pipeline_log.json

login_file:
  host: URL
  port: 0000
  db_name: DB_NAME
  username: USERNAME
  password: PASSWORD

filters:
  dynamic:
    report_id: 
    donor: 
    project: 
    study: 
    report_type: 
    failed: 
    cancer_type: 
    oncotree_code: 
    assay: 
    biopsy_site: 
    sample_type: 
    tmb_status: 
    hrd_status: 
    msi_status: 

    count: 

  variant:
    cnv_gene: 
    cnv_type: 
    snv_gene: 
    snv_type: 
    snv_protein: 
    fusion_gene: 
    fusion_effect: 
    fusion_frame: 

    ctdna_status: 
    ctdna_cnv: 
    ctdna_snv: 

  numeric:
    djerba_version: 
    date_reported: 
    coverage: 
    purity: "<=0.3"
    callability: 
    ploidy: 
    TMB: 
    TMB_value: 
    HRD_value: 
    MSI_value: 
    pga: 
    cnv_clinical: 
    snv_oncogenic: 
    fusion_clinical: 

    plot: 
```

<br>

# Example 4: Stacking Filters
- Scenario: Filtering for **HRD** status from **passed** cases with **excess coverage** (>=115) and **SNVs in both *KRAS* AND *TP53*.**
- Output: JSON reports satisfying filters, summary.csv, and plot
- Application: This is an oddly specific scenario; however, this example demonstrates more complex filtering and shows that filters across different parameters can be stacked!
```
query_pipeline:
  run_retrieve: true
  run_variant: true
  run_numeric: true
  run_summary: true

paths:
  output_dir: output/
  plot_out: output/coverage_over_time.png
  summary_out: output/summary.csv
  log_file: output/pipeline_log.json

login_file:
  host: URL
  port: 0000
  db_name: DB_NAME
  username: USERNAME
  password: PASSWORD

filters:
  dynamic:
    report_id: 
    donor: 
    project: 
    study: 
    report_type: 
    failed: False
    cancer_type: 
    oncotree_code: 
    assay: 
    biopsy_site: 
    sample_type: 
    tmb_status: 
    hrd_status: "HRD"
    msi_status: 

    count: 

  variant:
    cnv_gene: 
    cnv_type: 
    snv_gene: {"AND": ["TP53", "KRAS"]}
    snv_type: 
    snv_protein: 
    fusion_gene: 
    fusion_effect: 
    fusion_frame: 

    ctdna_status: 
    ctdna_cnv: 
    ctdna_snv: 

  numeric:
    djerba_version: 
    date_reported: 
    coverage: ">=115"
    purity: 
    callability: 
    ploidy: 
    TMB: 
    TMB_value: 
    HRD_value: 
    MSI_value: 
    pga: 
    cnv_clinical: 
    snv_oncogenic: 
    fusion_clinical: 

    plot: True
```