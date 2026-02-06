# Query Types
Supported query types when searching through reports stored by Djerba on the CouchDB database.

<br>

## 1. Single Report ID
| Field | Input | JSON Path | Output |
|------|------------------------|------------------------|------------------------|
| Single Report ID | String (e.g., `SAMPLE-REPORT_v1`) | `_id` | Single full report JSON object |

<br>

## 2. Bulk Report IDs
| Field | Input | JSON Path | Output |
|------|------------------------|------------------------|------------------------|
| >1 Report IDs | Text file with one report ID per line | `_id` | Multiple reports in a single JSON file |

<br>

## 3. Filter by Metadata
Filtering by metadata querying results in the output of full reports in a single JSON file. If one report falls under the filtered requirements, the JSON file output will contain a single report (similar to section 1). If a number of reports fall under the filtered requirements, the JSON file output will contain multiple reports (similar to section 2).

### 3a. Case Overview
| Field | Definition | Input | JSON Path |
|------|------------|-------|----------|
| Assay | Assay used for sequencing | String (e.g., `WGTS`) | `case_overview.results.assay` |
| Primary Cancer | Cancer diagnosis | String (e.g., `Nasopharyngeal cancer`) | `case_overview.results.primary_cancer` |
| Site of Biopsy | Location of biopsy or surgery | String (e.g., `Lung`) | `case_overview.results.site_of_biopsy` |
| Study | Research study or program identifier | String (e.g., `MOHCCN`) | `case_overview.results.study` |

### 3b. Sample Information
| Field | Definition | Input | JSON Path |
|------|------------|-------|----------|
| OncoTree Code | OncoTree-standardized cancer classification | String (e.g., `NPC`) | `sample.results.OncoTree Code` |
| Sample Type | Type of sample collected | String (e.g., `FFPE`) | `sample.results.Sample Type` |
| Estimated Cancer Cell Content (%) | Estimated tumour purity | Integer (e.g., `65`) | `sample.results.Estimated Cancer Cell Content (%)` |
| Estimated Ploidy | Estimated chromosomal copy number | Float (e.g., `2.96`) | `sample.results.Estimated Ploidy` |
| Callability (%) | Percentage of genome considered callable | Float (e.g., `66.4`) | `sample.results.Callability (%)` |
| Coverage (mean) | Average sequencing coverage | Float (e.g., `82.2`) | `sample.results.Coverage (mean)` |

### 3c. Genomic Landscape: Biomarkers
| Field | Definition | Input | JSON Path |
|------|------------|-------|----------|
| TMB | Tumor mutation burden per Mb | Float (e.g., `2.50`) | `genomic_landscape.results.genomic_biomarker.TMB.Genomic biomarker value` |
| MSI | Microsatellite instability per Mb | Float (e.g., `2.50`) | `genomic_landscape.results.genomic_biomarker.MSI.Genomic biomarker value` |
| HRD | Homologous recombination deficiency per Mb | Float (e.g., `2.50`) | `genomic_landscape.results.genomic_biomarker.HRD.Genomic biomarker value` |

### 3d. CNV Data
| Field | Definition | Input | JSON Path |
|------|------------|-------|----------|
| Percent Genome Altered | Percentage of genome altered by CNVs | Integer (e.g., `53`) | `wgts.cnv_purple.results.percent genome altered` |
| Total CNV Variants | Total number of CNVs | Integer (e.g., `21`) | `wgts.cnv_purple.results.total variants` |
| Gene | Genes affected by copy number change | String (e.g., `MTAP`) | `wgts.cnv_purple.results.body.Gene` |
| Alteration | Type of CNV event | String (e.g., `Deletion`, `Amplification`) | `wgts.cnv_purple.results.body.Alteration` |
| Chromosome | Genomic locus of CNV | String (e.g., `9p21.3`) | `wgts.cnv_purple.results.body.Chromosome` |
| OncoKB | OncoKB level of evidence for CNV | String (e.g., `3A`) | `wgts.cnv_purple.results.body.OncoKB` |

### 3e. SNV/Indel Data
| Field | Definition | Input | JSON Path |
|------|------------|-------|----------|
| Somatic Mutations | Total number of somatic SNVs/indels | Integer (e.g., `205`) | `wgts.snv_indel.results.somatic mutations` |
| Coding Sequence Mutations | Number of mutations affecting coding regions | Integer (e.g., `153`) | `wgts.snv_indel.results.coding sequence mutations` |
| Oncogenic Mutations | Number of mutations classified as oncogenic | Integer (e.g., `1`) | `wgts.snv_indel.results.oncogenic mutations` |
| Gene | Gene containing SNV/indel | String (e.g., `TP53`) | `wgts.snv_indel.results.body.Gene` |
| Protein Change | Protein-level consequence | String (e.g., `p.R306*`) | `wgts.snv_indel.results.body.protein` |
| Alteration Type | Functional mutation classification | String (e.g., `Nonsense Mutation`) | `wgts.snv_indel.results.body.type` |
| VAF (%) | Variant allele frequency | Float (e.g., `56`) | `wgts.snv_indel.results.body.vaf` |
| Depth | Read depth supporting variant | String (e.g., `33/56`) | `wgts.snv_indel.results.body.depth` |
| LOH | Loss of heterozygosity status | Boolean (e.g., `True`) | `wgts.snv_indel.results.body.LOH` |
| Chromosome | Genomic locus of variant | String (e.g., `17p13.1`) | `wgts.snv_indel.results.body.Chromosome` |
| OncoKB | OncoKB level of evidence | String (e.g., `N2`) | `wgts.snv_indel.results.body.OncoKB` |


### 3f. Fusion
| Field | Definition | Input | JSON Path |
|------|------------|-------|----------|
| Total Fusion Variants | Total number of fusion events | Integer (e.g., `5`) | `fusion.results.Total variants` |
| Clinically Relevant Fusions | Fusions with clinical relevance | Integer (e.g., `0`) | `fusion.results.Clinically relevant variants` |
| NCCN Relevant Fusions | Fusions relevant per NCCN guidelines | Integer (e.g., `0`) | `fusion.results.nccn_relevant_variants` |

<br>

## 4. Combined Metadata Filters
Similarly, combined metadata filtering results in a single JSON file output containing report(s) that meet the filter requirements.

| Field | Definition | Input | JSON Path |
|------|------------|-------|----------|
| Report Type | Tupe of report | Enum (`clinical`, `research`, `supplementary`, `failed`) | `attributes` |
| Last Updated | Date the report was last modified | Date or date range (`YYYY-MM-DD`) | `case_overview.last_updated` |
