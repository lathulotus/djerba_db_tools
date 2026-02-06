# Query Types
Supported query types when searching through reports stored by Djerba on the CouchDB database.

<br>

## 1. Single Report ID
This results in a JSON file with one single report.

| Flag | Query Type | Definition | JSON Path |
|------|------------|------------|-----------|
| `--report-id` | Report ID | Query by a single report identifier | _id |


## 2. Bulk Report IDs
This results in a JSON file containing more than one report.

| Flag | Query Type | Definition | JSON Path |
|------|------------|------------|-----------|
| `--bulk-ids` | Bulk Report IDs | Query by multiple report identifiers provided in a text file | _id |


## 3. Filter by Metadata
This results in a single JSON file containing report(s) that satisfy query requirements.

### 3a. Case Overview
| Flag | Query Type | Definition | JSON Path |
|------|------------|------------|-----------|
| `--assay` | Assay | Assay used for sequencing | case_overview.results.assay |
| `--primary-cancer` | Primary Cancer | Cancer diagnosis | case_overview.results.primary_cancer |
| `--biopsy-site` | Biopsy Site | Location of biopsy or surgery | case_overview.results.site_of_biopsy |
| `--study` | Study | Research study or program identifier | case_overview.results.study |

### 3b. Sample Information
| Flag | Query Type | Definition | JSON Path |
|------|------------|------------|-----------|
| `--oncotree-code` | OncoTree Code | OncoTree-standardized cancer classification | sample.results.OncoTree Code |
| `--sample-type` | Sample Type | Type of sample collected | sample.results.Sample Type |
| `--purity` | Estimated Purity | Estimated tumour purity | sample.results.Estimated Cancer Cell Content (%) |
| `--ploidy` | Estimated Ploidy | Estimated chromosomal copy number | sample.results.Estimated Ploidy |
| `--callability` | Callability | Percentage of genome considered callable | sample.results.Callability (%) |
| `--coverage` | Coverage | Average sequencing coverage | sample.results.Coverage (mean) |

### 3c. Genomic Landscape: Biomarkers
| Flag | Query Type | Definition | JSON Path |
|------|------------|------------|-----------|
| `--tmb-value` | TMB Value | Tumor mutation burden per Mb | genomic_landscape.results.genomic_biomarker.TMB.Genomic biomarker value |
| `--msi-value` | MSI Value | Microsatellite instability per Mb | genomic_landscape.results.genomic_biomarker.MSI.Genomic biomarker value |
| `--hrd-value` | HRD Value | Homologous recombination deficiency per Mb | genomic_landscape.results.genomic_biomarker.HRD.Genomic biomarker value |
| `--tmb-alteration` | TMB Status | TMB status | genomic_landscape.results.genomic_biomarkers.TMB.Genomic biomarker alteration |
| `--msi-alteration` | MSI Status | MSI status | genomic_landscape.results.genomic_biomarkers.MSI.Genomic biomarker alteration |
| `--hrd-alteration` | HRD Status | HRD status | genomic_landscape.results.genomic_biomarkers.HRD.Genomic biomarker alteration |

### 3d. CNV Data
| Flag | Query Type | Definition | JSON Path |
|------|------------|------------|-----------|
| `--pga` | Percent Genome Altered | Percentage genome altered by CNVs | wgts.cnv_purple.results.percent genome altered |
| `--cnv-total` | CNV Total | Total number of CNVs | wgts.cnv_purple.results.total variants |
| `--cnv-gene` | CNV Gene | Genes affected by copy number change | wgts.cnv_purple.results.body.Gene |
| `--cnv-alteration` | CNV Alteration | Type of CNV event | wgts.cnv_purple.results.body.Alteration |
| `--cnv-chromosome` | CNV Chromosome | Genomic locus of CNV | wgts.cnv_purple.results.body.Chromosome |
| `--cnv-oncokb` | CNV OncoKB | OncoKB level of evidence for CNV | wgts.cnv_purple.results.body.OncoKB |

### 3e. SNV/Indel Data
| Flag | Query Type | Definition | JSON Path |
|------|------------|------------|-----------|
| `--snv-somatic` | Somatic SNV Count | Total number of somatic SNVs/indels | wgts.snv_indel.results.somatic mutations |
| `--snv-coding` | Coding SNV Count | Number of mutations affecting coding regions | wgts.snv_indel.results.coding sequence mutations |
| `--snv-oncogenic` | Oncogenic SNV Count | Number of mutations classified as oncogenic | wgts.snv_indel.results.oncogenic mutations |
| `--snv-gene` | SNV Gene | Gene containing SNV/indel | wgts.snv_indel.results.body.Gene |
| `--snv-protein` | SNV Protein | Protein-level consequence | wgts.snv_indel.results.body.protein |
| `--snv-type` | SNV Type | Functional mutation classification | wgts.snv_indel.results.body.type |
| `--snv-vaf` | SNV VAF | Variant allele frequency | wgts.snv_indel.results.body.vaf |
| `--snv-depth` | SNV Depth | Read depth supporting variant | wgts.snv_indel.results.body.depth |
| `--snv-loh` | SNV LOH | Loss of heterozygosity status | wgts.snv_indel.results.body.LOH |
| `--snv-chromosome` | SNV Chromosome | Genomic locus of variant | wgts.snv_indel.results.body.Chromosome |
| `--snv-oncokb` | SNV OncoKB | OncoKB level of evidence | wgts.snv_indel.results.body.OncoKB |

### 3f. Fusion
| Flag | Query Type | Definition | JSON Path |
|------|------------|------------|-----------|
| `--fusion-total` | Fusion Total | Total number of fusion events | fusion.results.Total variants |
| `--fusion-clinical` | Clinical Fusions | Fusions with clinical relevance | fusion.results.Clinically relevant variants |
| `--fusion-nccn` | NCCN Fusions | Fusions relevant per NCCN guidelines | fusion.results.nccn_relevant_variants |


## 4. Combined Metadata Filters
This results in a single JSON file containing report(s) that satisfy query requirements.

| Flag | Query Type | Definition | JSON Path |
|------|------------|------------|-----------|
| `--report-type` | Report Type | Type of report | attributes |
| `--last-update` | Last Update | Date the report was last modified | case_overview.last_updated |


