# Query Types
Supported query types when searching through reports stored by Djerba on the CouchDB database.

<br>

## 1. Single Report ID
| Flag | Input | JSON Path | Output |
|------|------------------------|------------------------|------------------------|
| `--report-id` | String (e.g., `sample-report_v1`) | `_id` | Single full report JSON object |

<br>

## 2. Bulk Report IDs
| Flag | Input | JSON Path | Output |
|------|------------------------|------------------------|------------------------|
| `--bulk-ids` | Text file with one report ID per line (e.g., `specific_reports.txt`) | `_id` | Multiple reports in a single JSON file |

<br>

## 3. Filter by Metadata
Filtering by metadata querying results in the output of full reports in a single JSON file. If one report falls under the filtered requirements, the JSON file output will contain a single report (similar to section 1). If a number of reports fall under the filtered requirements, the JSON file output will contain multiple reports (similar to section 2).

### 3a. Case Overview
| Flag | Definition | Input | JSON Path |
|------|------------|-------|----------|
| `--assay` | Assay used for sequencing | String (e.g., `WGTS`) | `case_overview.results.assay` |
| `--primary-cancer` | Cancer diagnosis | String (e.g., `Nasopharyngeal cancer`) | `case_overview.results.primary_cancer` |
| `--biopsy-site` | Location of biopsy or surgery | String (e.g., `Lung`) | `case_overview.results.site_of_biopsy` |
| `--study` | Research study or program identifier | String (e.g., `MOHCCN`) | `case_overview.results.study` |

### 3b. Sample Information
| Flag | Definition | Input | JSON Path |
|------|------------|-------|----------|
| `--oncotree-code` | OncoTree-standardized cancer classification | String (e.g., `NPC`) | `sample.results.OncoTree Code` |
| `--sample-type` | Type of sample collected | String (e.g., `FFPE`) | `sample.results.Sample Type` |
| `--purity` | Estimated tumour purity | Integer (e.g., `65`) | `sample.results.Estimated Cancer Cell Content (%)` |
| `--ploidy` | Estimated chromosomal copy number | Float (e.g., `2.96`) | `sample.results.Estimated Ploidy` |
| `--callability` | Percentage of genome considered callable | Float (e.g., `66.4`) | `sample.results.Callability (%)` |
| `--coverage` | Average sequencing coverage | Float (e.g., `82.2`) | `sample.results.Coverage (mean)` |

### 3c. Genomic Landscape: Biomarkers
| Flag | Definition | Input | JSON Path |
|------|------------|-------|----------|
| `--tmb-value` | Tumor mutation burden per Mb | Float (e.g., `2.50`) | `genomic_landscape.results.genomic_biomarker.TMB.Genomic biomarker value` |
| `--msi-value` | Microsatellite instability per Mb | Float (e.g., `2.50`) | `genomic_landscape.results.genomic_biomarker.MSI.Genomic biomarker value` |
| `--hrd-value` | Homologous recombination deficiency per Mb | Float (e.g., `2.50`) | `genomic_landscape.results.genomic_biomarker.HRD.Genomic biomarker value` |
| `--tmb-alteration` | TMB status | Enum (`TMB-H`, `TMB-L`) | `genomic_landscape.results.genomic_biomarkers.TMB.Genomic biomarker alteration` |
| `--msi-alteration` | MSI status | Enum (`MSI`, `MSS`) | `genomic_landscape.results.genomic_biomarkers.MSI.Genomic biomarker alteration` |
| `--hrd-alteration` | HRD status | Enum (`HR Deficient`, `HR Proficient`, `HRD`, `HRP`) | `genomic_landscape.results.genomic_biomarkers.HRD.Genomic biomarker alteration` |

### 3d. CNV Data
| Flag | Definition | Input | JSON Path |
|------|------------|-------|----------|
| `--pga` | Percentage genome altered by CNVs | Integer (e.g., `53`) | `wgts.cnv_purple.results.percent genome altered` |
| `--cnv-total` | Total number of CNVs | Integer (e.g., `21`) | `wgts.cnv_purple.results.total variants` |
| `--cnv-gene` | Genes affected by copy number change | String (e.g., `MTAP`) | `wgts.cnv_purple.results.body.Gene` |
| `--cnv-alteration` | Type of CNV event | String (e.g., `Deletion`, `Amplification`) | `wgts.cnv_purple.results.body.Alteration` |
| `--cnv-chromosome` | Genomic locus of CNV | String (e.g., `9p21.3`) | `wgts.cnv_purple.results.body.Chromosome` |
| `--cnv-oncokb` | OncoKB level of evidence for CNV | String (e.g., `3A`) | `wgts.cnv_purple.results.body.OncoKB` |

### 3e. SNV/Indel Data
| Flag | Definition | Input | JSON Path |
|------|------------|-------|----------|
| `--snv-somatic` | Total number of somatic SNVs/indels | Integer (e.g., `205`) | `wgts.snv_indel.results.somatic mutations` |
| `--snv-coding` | Number of mutations affecting coding regions | Integer (e.g., `153`) | `wgts.snv_indel.results.coding sequence mutations` |
| `--snv-oncogenic` | Number of mutations classified as oncogenic | Integer (e.g., `1`) | `wgts.snv_indel.results.oncogenic mutations` |
| `--snv-gene` | Gene containing SNV/indel | String (e.g., `TP53`) | `wgts.snv_indel.results.body.Gene` |
| `--snv-protein` | Protein-level consequence | String (e.g., `p.R306*`) | `wgts.snv_indel.results.body.protein` |
| `--snv-type` | Functional mutation classification | String (e.g., `Nonsense Mutation`) | `wgts.snv_indel.results.body.type` |
| `--snv-vaf` | Variant allele frequency | Float (e.g., `56`) | `wgts.snv_indel.results.body.vaf` |
| `--snv-depth` | Read depth supporting variant | String (e.g., `33/56`) | `wgts.snv_indel.results.body.depth` |
| `--snv-loh` | Loss of heterozygosity status | Boolean (e.g., `True`) | `wgts.snv_indel.results.body.LOH` |
| `--snv-chromosome` | Genomic locus of variant | String (e.g., `17p13.1`) | `wgts.snv_indel.results.body.Chromosome` |
| `--snv-oncokb` | OncoKB level of evidence | String (e.g., `N2`) | `wgts.snv_indel.results.body.OncoKB` |

### 3f. Fusion
| Flag | Definition | Input | JSON Path |
|------|------------|-------|----------|
| `--fusion-total` | Total number of fusion events | Integer (e.g., `5`) | `fusion.results.Total variants` |
| `--fusion-clinical` | Fusions with clinical relevance | Integer (e.g., `0`) | `fusion.results.Clinically relevant variants` |
| `--fusion-nccn` | Fusions relevant per NCCN guidelines | Integer (e.g., `0`) | `fusion.results.nccn_relevant_variants` |

<br>

## 4. Combined Metadata Filters
Similarly, combined metadata filtering results in a single JSON file output containing report(s) that meet the filter requirements.

| Field | Definition | Input | JSON Path |
|------|------------|-------|----------|
| `--report-type` | Tupe of report | Enum (`clinical`, `research`, `supplementary`, `failed`) | `attributes` |
| `--last-update` | Date the report was last modified | Date or date range (`YYYY-MM-DD`) | `case_overview.last_updated` |
