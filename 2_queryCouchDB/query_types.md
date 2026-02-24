# Query Types
Querying couchDB supports string-based search via Mango and numeric-based search via Python. Filters may be set through YAML files and/or search flags, depending on the search focus.


## String-Based Querying
Query types are laid out in the **[filters YAML file](./filters.yaml)**. Fields that do not require querying should remain `null`. Individual JSON file(s) will be output for reports satisfying specific query requirements.

| Filter | Definition | Example |
|--------|------------|---------|
| `report_id` | Report ID | `REPORT_123-v1` |
| `donor` | Donor ID | `DONOR_123` |
| `project` | Project name | `PROJECT` |
| `study` | Study name | `STUDY` |
| `report_type` | Report | `clinical`, `research` |
| `cancer_type` | Primary cancer diagnosis | `pancreatic adenocarcinoma` |
| `oncotree_code` | Oncotree code | `PAAD` |
| `assay` | Assay | `WGTS` |
| `biopsy_site` | Biopsy/surgery | `left crest` |
| `sample_type` | Type of sample | `FFPE  tissue block` |
| `hrd_status` | HRD status | `HR Proficient` |
| `msi_status` | MSI status | `MSS` |
| `tmb_status` | TMB status | `TMB-L` |
| `failed` | Report failure status | `false` |


## Numeric-Based Querying
Query filters can be input using the flag specified below. Individual JSON file(s) will be output for reports satisfying specific query requirements. For specific (rounded) searching, input a single integer formatted as `num` (i.e., `2`). For range searching, input a list formatted as `[min,max]` (i.e., `[0,4]`).
| Filter | Definition | Example |
|--------|------------|---------|
| `--date_reported` | Date report created | `2026/12/01` |
| `--djerba_version` | Report version | `1.10.0` |
| `--coverage` | Average read coverage | `75.0` or `70,80` |
| `--purity` | Estimated tumour purity % | `75` or `70,80` |
| `--callability` | Percent of callable genome | `75.0` or `70,80` |
| `--ploidy` | Estimated chromosomal copy number | `2.75` or `2,3` |
| `--cnv_pga` | Percent genome altered | `2.75` or `2,3` |
| `--cnv_clinical` | Clinically relevant CNVs | `2.75` or `2,3` |
| `--snv_oncologival` | Oncologically relevant SNVs | `2.75` or `2,3` |
| `--fusion_clinical` | Clinically relevant fusions | `2.75` or `2,3` |


## Variant-Based Querying
Query filters can be input using the flag specified below. Individual JSON file(s) will be output for reports satisfying specific query requirements. For specific gene searches, input a singular string containing the gene code. For pairs of genes or multiple genes in one case, input a list formatted as `[gene1,gene2]` (i.e., `[SDC1,BCL2L11]`). Filters are stacked, thus applying a specific gene and type filter searches for that gene + effect (i.e., TP53 amplification, KRAS missense).
| Filter | Definition | Example |
|--------|------------|---------|
| `--cnv_gene` | CNV-containing gene | `TP53` |
| `--cnv_type` | CNV type associated with search | `amplification` |
| `--snv_gene` | SNV-containing gene | `KRAS` |
| `--snv_type` | SNV type asssociated with search | `Missense Mutation` |
| `--fusion_gene` | Fusion-containing gene(s) | `SDC1` or `SDC1, BCL2L11` |
| `--fusion_effect` | Fusion effect | `Likely Loss-of-function` |
| `--fusion_frame` | Fusion associated frame | `out of frame` |


## Archive of Past Filters
| Filter | Definition | Example |
|--------|------------|---------|
| `hrd_value` | HRD value per Mb | `0.0751` or `0.06,0.08` |
| `msi_value` | HRD value per Mb | `2.075` or `1.5,2.5` |
| `tmb_value` | HRD value per Mb | `1.75` or `1,2` |
