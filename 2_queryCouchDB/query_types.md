# Query Types
Supported query types when searching through reports stored by Djerba on the CouchDB database.

<br>

## 1. General Search
This results in a JSON file per report for report(s) that satisfy query requirements.

| Flag | Query Type | Definition | JSON Path |
|------|------------|------------|-----------|
| `--report_id` | Report ID | Report identifier | _id |
| `--report_type` | Report Type | Type of report | plugins.genomic_landscape.attributes |
| `--last_update` | Last Update | Date the report was last modified | last_updated |


## 2. Filter by Metadata
This results JSON files for report(s) that satisfy query requirements.

### 2a. Case Overview
| Flag | Query Type | Definition | JSON Path |
|------|------------|------------|-----------|
| `--assay` | Assay | Assay used for sequencing | plugins.case_overview.results.assay |
| `--cancer_type` | Primary Cancer | Cancer diagnosis | plugins.case_overview.results.primary_cancer |
| `--biopsy_site` | Biopsy Site | Location of biopsy or surgery | plugins.case_overview.results.site_of_biopsy |
| `--study` | Study | Research study or program identifier | plugins.case_overview.results.study |
| `--project` | Project |Project name | config.input_params_helper.project |
| `--donor` | Donor | Donor ID | config.input_params_helper.donor |

### 2b. Sample Information
| Flag | Query Type | Definition | JSON Path |
|------|------------|------------|-----------|
| `--oncotree_code` | OncoTree Code | OncoTree-standardized cancer classification | plugins.sample.results.OncoTree Code |
| `--sample_type` | Sample Type | Type of sample collected | plugins.sample.results.Sample Type |
| `--purity` | Estimated Purity | Estimated tumour purity | plugins.sample.results.Estimated Cancer Cell Content (%) |
| `--ploidy` | Estimated Ploidy | Estimated chromosomal copy number | plugins.sample.results.Estimated Ploidy |
| `--callability` | Callability | Percentage of genome considered callable | plugins.sample.results.Callability (%) |
| `--coverage` | Coverage | Average sequencing coverage | plugins.sample.results.Coverage (mean) |

### 2c. Genomic Landscape: Biomarkers
| Flag | Query Type | Definition | JSON Path |
|------|------------|------------|-----------|
| `--tmb_value` | TMB Value | Tumor mutation burden per Mb | plugins.genomic_landscape.results.genomic_biomarker.TMB.Genomic biomarker value |
| `--msi_value` | MSI Value | Microsatellite instability per Mb | plugins.genomic_landscape.results.genomic_biomarker.MSI.Genomic biomarker value |
| `--hrd_value` | HRD Value | Homologous recombination deficiency per Mb | plugins.genomic_landscape.results.genomic_biomarker.HRD.Genomic biomarker value |
| `--tmb_status` | TMB Status | TMB status | plugins.genomic_landscape.results.genomic_biomarkers.TMB.Genomic biomarker alteration |
| `--msi_status` | MSI Status | MSI status | plugins.genomic_landscape.results.genomic_biomarkers.MSI.Genomic biomarker alteration |
| `--hrd_status` | HRD Status | HRD status | plugins.genomic_landscape.results.genomic_biomarkers.HRD.Genomic biomarker alteration |

### 2d. CNV Data
| Flag | Query Type | Definition | JSON Path |
|------|------------|------------|-----------|
| `--pga` | Percent Genome Altered | Percentage genome altered by CNVs | plugins.wgts.cnv_purple.results.percent genome altered |
| `--cnv_total` | CNV Total | Total number of CNVs | plugins.wgts.cnv_purple.results.total variants |
| `--cnv_gene` | CNV Gene | Genes affected by copy number change | plugins.wgts.cnv_purple.results.body.Gene |
| `--cnv_type` | CNV Alteration | Type of CNV event | plugins.wgts.cnv_purple.results.body.Alteration |
| `--cnv_chromosome` | CNV Chromosome | Genomic locus of CNV | plugins.wgts.cnv_purple.results.body.Chromosome |
| `--cnv_oncokb` | CNV OncoKB | OncoKB level of evidence for CNV | plugins.wgts.cnv_purple.results.body.OncoKB |

### 2e. SNV/Indel Data
| Flag | Query Type | Definition | JSON Path |
|------|------------|------------|-----------|
| `--snv_somatic` | Somatic SNV Count | Total number of somatic SNVs/indels | plugins.wgts.snv_indel.results.somatic mutations |
| `--snv_coding` | Coding SNV Count | Number of mutations affecting coding regions | plugins.wgts.snv_indel.results.coding sequence mutations |
| `--snv_oncogenic` | Oncogenic SNV Count | Number of mutations classified as oncogenic | plugins.wgts.snv_indel.results.oncogenic mutations |
| `--snv_gene` | SNV Gene | Gene containing SNV/indel | plugins.wgts.snv_indel.results.body.Gene |
| `--snv_protein` | SNV Protein | Protein-level consequence | plugins.wgts.snv_indel.results.body.protein |
| `--snv_type` | SNV Type | Functional mutation classification | plugins.wgts.snv_indel.results.body.type |
| `--snv_vaf` | SNV VAF | Variant allele frequency | plugins.wgts.snv_indel.results.body.vaf |
| `--snv_depth` | SNV Depth | Read depth supporting variant | plugins.wgts.snv_indel.results.body.depth |
| `--snv_loh` | SNV LOH | Loss of heterozygosity status | plugins.wgts.snv_indel.results.body.LOH |
| `--snv_chromosome` | SNV Chromosome | Genomic locus of variant | plugins.wgts.snv_indel.results.body.Chromosome |
| `--snv_oncokb` | SNV OncoKB | OncoKB level of evidence | plugins.wgts.snv_indel.results.body.OncoKB |

### 2f. Fusion
| Flag | Query Type | Definition | JSON Path |
|------|------------|------------|-----------|
| `--fusion_total` | Fusion Total | Total number of fusion events | plugins.fusion.results.Total variants |
| `--fusion_clinical` | Clinical Fusions | Fusions with clinical relevance | plugins.fusion.results.Clinically relevant variants |
| `--fusion_nccn` | NCCN Fusions | Fusions relevant per NCCN guidelines | plugins.fusion.results.nccn_relevant_variants |


