# Query Types
Supported query types when searching through reports stored by Djerba on the CouchDB database.

<br>

## 1. Single Report ID
This results in a JSON file with one single report.

| Flag | Query Type | Definition | JSON Path |
|------|------------|------------|-----------|
| `--report-id` | Report ID | Query by a single report identifier | _id |


## 2. Bulk Report IDs
This results in multiple JSON files for each report.

| Flag | Query Type | Definition | JSON Path |
|------|------------|------------|-----------|
| `--bulk-ids` | Bulk Report IDs | Query by multiple report identifiers provided in a text file | _id |


## 3. Filter by Metadata
This results JSON files for report(s) that satisfy query requirements.

### 3a. Case Overview
| Flag | Query Type | Definition | JSON Path |
|------|------------|------------|-----------|
| `--assay` | Assay | Assay used for sequencing | plugins.case_overview.results.assay |
| `--primary-cancer` | Primary Cancer | Cancer diagnosis | plugins.case_overview.results.primary_cancer |
| `--biopsy-site` | Biopsy Site | Location of biopsy or surgery | plugins.case_overview.results.site_of_biopsy |
| `--study` | Study | Research study or program identifier | plugins.case_overview.results.study |

### 3b. Sample Information
| Flag | Query Type | Definition | JSON Path |
|------|------------|------------|-----------|
| `--oncotree-code` | OncoTree Code | OncoTree-standardized cancer classification | plugins.sample.results.OncoTree Code |
| `--sample-type` | Sample Type | Type of sample collected | plugins.sample.results.Sample Type |
| `--purity` | Estimated Purity | Estimated tumour purity | plugins.sample.results.Estimated Cancer Cell Content (%) |
| `--ploidy` | Estimated Ploidy | Estimated chromosomal copy number | plugins.sample.results.Estimated Ploidy |
| `--callability` | Callability | Percentage of genome considered callable | plugins.sample.results.Callability (%) |
| `--coverage` | Coverage | Average sequencing coverage | plugins.sample.results.Coverage (mean) |

### 3c. Genomic Landscape: Biomarkers
| Flag | Query Type | Definition | JSON Path |
|------|------------|------------|-----------|
| `--tmb-value` | TMB Value | Tumor mutation burden per Mb | plugins.genomic_landscape.results.genomic_biomarker.TMB.Genomic biomarker value |
| `--msi-value` | MSI Value | Microsatellite instability per Mb | plugins.genomic_landscape.results.genomic_biomarker.MSI.Genomic biomarker value |
| `--hrd-value` | HRD Value | Homologous recombination deficiency per Mb | plugins.genomic_landscape.results.genomic_biomarker.HRD.Genomic biomarker value |
| `--tmb-alteration` | TMB Status | TMB status | plugins.genomic_landscape.results.genomic_biomarkers.TMB.Genomic biomarker alteration |
| `--msi-alteration` | MSI Status | MSI status | plugins.genomic_landscape.results.genomic_biomarkers.MSI.Genomic biomarker alteration |
| `--hrd-alteration` | HRD Status | HRD status | plugins.genomic_landscape.results.genomic_biomarkers.HRD.Genomic biomarker alteration |

### 3d. CNV Data
| Flag | Query Type | Definition | JSON Path |
|------|------------|------------|-----------|
| `--pga` | Percent Genome Altered | Percentage genome altered by CNVs | plugins.wgts.cnv_purple.results.percent genome altered |
| `--cnv-total` | CNV Total | Total number of CNVs | plugins.wgts.cnv_purple.results.total variants |
| `--cnv-gene` | CNV Gene | Genes affected by copy number change | plugins.wgts.cnv_purple.results.body.Gene |
| `--cnv-alteration` | CNV Alteration | Type of CNV event | plugins.wgts.cnv_purple.results.body.Alteration |
| `--cnv-chromosome` | CNV Chromosome | Genomic locus of CNV | plugins.wgts.cnv_purple.results.body.Chromosome |
| `--cnv-oncokb` | CNV OncoKB | OncoKB level of evidence for CNV | plugins.wgts.cnv_purple.results.body.OncoKB |

### 3e. SNV/Indel Data
| Flag | Query Type | Definition | JSON Path |
|------|------------|------------|-----------|
| `--snv-somatic` | Somatic SNV Count | Total number of somatic SNVs/indels | plugins.wgts.snv_indel.results.somatic mutations |
| `--snv-coding` | Coding SNV Count | Number of mutations affecting coding regions | plugins.wgts.snv_indel.results.coding sequence mutations |
| `--snv-oncogenic` | Oncogenic SNV Count | Number of mutations classified as oncogenic | plugins.wgts.snv_indel.results.oncogenic mutations |
| `--snv-gene` | SNV Gene | Gene containing SNV/indel | plugins.wgts.snv_indel.results.body.Gene |
| `--snv-protein` | SNV Protein | Protein-level consequence | plugins.wgts.snv_indel.results.body.protein |
| `--snv-type` | SNV Type | Functional mutation classification | plugins.wgts.snv_indel.results.body.type |
| `--snv-vaf` | SNV VAF | Variant allele frequency | plugins.wgts.snv_indel.results.body.vaf |
| `--snv-depth` | SNV Depth | Read depth supporting variant | plugins.wgts.snv_indel.results.body.depth |
| `--snv-loh` | SNV LOH | Loss of heterozygosity status | plugins.wgts.snv_indel.results.body.LOH |
| `--snv-chromosome` | SNV Chromosome | Genomic locus of variant | plugins.wgts.snv_indel.results.body.Chromosome |
| `--snv-oncokb` | SNV OncoKB | OncoKB level of evidence | plugins.wgts.snv_indel.results.body.OncoKB |

### 3f. Fusion
| Flag | Query Type | Definition | JSON Path |
|------|------------|------------|-----------|
| `--fusion-total` | Fusion Total | Total number of fusion events | plugins.fusion.results.Total variants |
| `--fusion-clinical` | Clinical Fusions | Fusions with clinical relevance | plugins.fusion.results.Clinically relevant variants |
| `--fusion-nccn` | NCCN Fusions | Fusions relevant per NCCN guidelines | plugins.fusion.results.nccn_relevant_variants |


## 4. Combined Metadata Filters
This results JSON files for report(s) that satisfy query requirements.

| Flag | Query Type | Definition | JSON Path |
|------|------------|------------|-----------|
| `--report-type` | Report Type | Type of report | plugins.genomic_landscape.attributes |
| `--last-update` | Last Update | Date the report was last modified | last_updated |

- Note that last_updated value is stored as MM/DD/YY_24:12:00Z

