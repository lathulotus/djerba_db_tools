# Query Types
Query types are laid out in the **[filters YAML file](./filters.yaml)**. File can be directly altered to query fr specific filters. Fields that do not require querying should remain `null`. Individual JSON file(s) will be output for reports satisfying specific query requirements.

## General Variables
| Filter | Definition | Type | Example |
|--------|------------|------|---------|
| `date` | Date of last update | single entry | `2026/12/01` |
| `report_id` | Report ID | single entry | `REPORT_123-v1` |
| `donor` | Donor ID | single entry | `DONOR_123` |
| `project` | Project name | single entry | `PROJECT` |
| `study` | Study name | single entry | `STUDY` |
| `report_type` | Report type | single entry | `clinical`, `research` |
| `cancer_type` | Primary cancer diagnosis | single entry | `pancreatic adenocarcinoma` |
| `oncotree_code` | Oncotree code | single entry | `PAAD` |
| `assay` | Assay type | single entry | `WGTS` |
| `biopsy_site` | Biopsy/surgery | single entry | `left crest` |
| `sample_type` | Type of sample | single entry | `FFPE  tissue block` |


## General Numeric Variables
| Filter | Definition | Type | Example |
|--------|------------|------|---------|
| `purity` | Estimated tumour purity % | integer | `75` |
| `ploidy` | Estimated chromosomal copy number | single entry | `2.75` |
| `coverage` | Average read coverage | single entry | `75.0` |
| `callability` | Percent of callable genome | single entry | `75.0` |


## Biological Variables: Biomarkers
| Filter | Definition | Type | Example |
|--------|------------|------|---------|
| `hrd_status` | HRD status | single entry | `HR Proficient` |
| `hrd_value` | HRD value per Mb | single entry | `0.0751` |
| `msi_status` | MSI status | single entry | `MSS` |
| `msi_value` | HRD value per Mb | single entry | `2.075` |
| `tmb_status` | TMB status | single entry | `TMB-L` |
| `tmb_value` | HRD value per Mb | single entry | `1.75` |


## Biological Variables: Fusions
| Filter | Definition | Type | Example |
|--------|------------|------|---------|
| `fusion_total` | Total number of fusion events | integer | `5` |
| `fusion_clinical` | Number of clinically relevant fusions | integer | `5` |
| `fusion_nccn` | Number of NCCN relevant fusions | integer | `5` |
| `fusion` |  |  |  |
| `gene` | Genes involved in fusion event, single or pair | single, list of 2 | `SDC1` or `SDC1, BCL2L11` |
| `frame` | Frame | single entry | `no effect` |
| `mutation effect` | Fusion effect | single entry | `Likely Loss-of-function` |



## Biological Variables: CNV, SNV, Indels
| Filter | Definition | Type | Example |
|--------|------------|------|---------|
| `cnv` | CNV gene (and variant type) | gene, gene + effect | `TP53` or `TP53 amplification` |
| `snv` | SNV gene (and variant type) | gene, gene + effect | `TP53` or `TP53 Missense Mutation` |
