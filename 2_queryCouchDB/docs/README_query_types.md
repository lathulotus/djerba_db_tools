# Query Types
Querying couchDB supports string-based search via Mango and numeric-based search via Python. Filters may be set through YAML files and/or search flags, depending on the search focus.


## Dynamic Querying
Fields that do not require querying should remain `null`. Individual JSON file(s) will be output for reports satisfying specific query requirements.

| Filter | Definition | Example |
|--------|------------|---------|
| `report_id` | Report ID | `"REPORT_123-v1"` or `"REPORT_123"` |
| `donor` | Donor ID | `"DONOR_123"` |
| `project` | Project name | `"PROJECT"` |
| `study` | Study name | `"STUDY"` |
| `report_type` | Report | `"clinical"`, `"research"` |
| `author` | Author name | `"Person Name"` |
| `cancer_type` | Primary cancer diagnosis | `"pancreatic adenocarcinoma"` |
| `oncotree_code` | Oncotree code | `"PAAD"` |
| `assay` | Assay | `"WGTS"` |
| `biopsy_site` | Biopsy/surgery | `"left crest"` |
| `sample_type` | Type of sample | `"FFPE  tissue block"` |
| `hrd_status` | HRD status | `"HR Proficient"` |
| `msi_status` | MSI status | `"MSS"` |
| `tmb_status` | TMB status | `"TMB-L"` |
| `failed` | Report failure status | `false` |


## Variant-Based Querying
Query filters can be input using the flag specified below. Individual JSON file(s) will be output for reports satisfying specific query requirements. For specific gene searches, input a singular string containing the gene code. Filters are stacked, thus applying a specific gene and type filter searches for that gene + effect (i.e., TP53 amplification, KRAS missense). Switching between AND or OR is supported when querying through SNV and CNV genes. Fusion gene querying exclusively supports AND condition.

| Filter | Definition | Example |
|--------|------------|---------|
| `--cnv_gene` | CNV-containing gene | `"TP53"` or  |
| `--cnv_type` | CNV type associated with search | `"amplification"` |
| `--snv_gene` | SNV-containing gene | `"KRAS"` |
| `--snv_type` | SNV type asssociated with search | `"Missense Mutation"` or `missense` |
| `--snv_protein` | Protein change resulting from SNV | `"p.S110R"` |
| `--fusion_gene` | Fusion-containing gene(s) | `"SDC1"` |
| `--fusion_effect` | Fusion effect | `"Likely Loss-of-function"` or `"loss"` |
| `--fusion_frame` | Fusion associated frame | `"out of frame"` or `"out"` |
| `--ctdna_status` | ctDNA status, all fields | `"Detected"` |
| `--ctdna_cnv` | ctDNA status in CNV | `True` |
| `--ctdna_snv` | ctDNA status in SNV | `False` |

| Operator | Definition |
|----------|------------|
| `[GENE1, GENE2]` | GENE1 OR GENE2 |
| `{AND: [GENE1, GENE2]}` | GENE1 AND GENE2 |


## Numeric-Based Querying
Query filters can be input using the flag specified below. Individual JSON file(s) will be output for reports satisfying specific query requirements. Operator must be included with the input value, otherwise will be defaulted to `>=`. For filtering across a range (inclusive), input a list formatted as `"[min,max]"` (i.e., `"[0,4]"`). For searching across various values (OR condition), input values seperated by commas as `"num1, num2, num3"` (i.e., `"0, 4, 7"`).
| Filter | Definition | Example |
|--------|------------|---------|
| `--date_reported` | Date report created | `"2026/12/01"` |
| `--djerba_version` | Report version | `"1.10.0"` |
| `--coverage` | Average read coverage | `"==75.0"` or `70,80` |
| `--purity` | Estimated tumour purity % | `"==75"` or `70,80` |
| `--callability` | Percent of callable genome | `"==75.0"` or `70,80` |
| `--ploidy` | Estimated chromosomal copy number | `"==2.75"` or `2,3` |
| `--TMB` | TMB value | `"==79"` |
| `--tmb_value` | TMB score per Mb | `"==0.7"` |
| `--hrd_value` | HRD score per Mb | `"==2.1"` |
| `--msi_value` | MSI score per Mb | `"==0.9"` |
| `--pga` | Percent genome altered | `"==2.75"` or `2,3` |
| `--cnv_clinical` | Clinically relevant CNVs | `"==2.75"` or `2,3` |
| `--snv_oncological` | Oncologically relevant SNVs | `"==2.75"` or `2,3` |
| `--fusion_clinical` | Clinically relevant fusions | `"==2.75"` or `2,3` |
| `--plot` | Plotting cumulative report count | `true` |

| Operator | Definition |
|----------|------------|
| `>` | Greater than input value |
| `<` | Less than input value |
| `>=` | Greater than or equal to input value |
| `<=` | Less than or equal to input value |
| `==` | Equal to input value |
| `"[min,max]"` | Search across range, inclusive |
| `"num1, num2, num3"` | Search various values, OR condition |
