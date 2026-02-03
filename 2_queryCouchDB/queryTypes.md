# Query Types
Supported query types when searching through clinical reports stored by Djerba on the CouchDB database.

<br>

## 1. Single Report ID
- Input: report ID
- Processing: ```_id```
- Output: single JSON report

<br>

## 2. Bulk Report IDs
- Input: multiple report IDs (as a comma-separated list? or as a text/excel file?)
- Processing: ```_id```
- Output: multiple JSON reports

<br>

## 3. Filter by Metadata
### 3a. Case Overview
- Assay: type of assay used for sequencing
    - Input: e.g., WGTS
    - Processing: ```case_overview``` -> ```results``` -> ```assay```
- Primary Cancer: type of cancer
    - Input: e.g., Nasopharyngeal cancer
    - Combine with OncoTree code ??
    - Processing: ```case_overview``` -> ```results``` -> ```primary_cancer```
- Site of biopsy: biopsy type or location
    - Input: e.g., Lung
    - Processing: ```case_overview``` -> ```results``` -> ```site_of_biopsy```
- Study: name of research study
    - Input: e.g., MOHCCN
    - Processing: ```case_overview``` -> ```results``` -> ```study```

### 3b. Sample Information
- OncoTree Code: OncoTree-standardized cancer identifier
    - Input: e.g., NPC
    - Combine with primary_cancer ??
    - Processing: ```sample``` -> ```results``` -> ```OncoTree Code```
- ~~Sample type: type of sample~~
    - ~~Input: e.g., Nucleic acids extracted from tissue in a CLIA-certified laboratory~~
    - ~~Processing: ```sample``` -> ```results``` -> ```Sample Type```~~
- Estimated Cancer Cell Content: estimated percentage of cancer cell content in sample, purity
    - Input: e.g., 65
    - Processing: ```sample``` -> ```results``` -> ```Estimated Cancer Cell Content (%)```
- Estimated Ploidy: Estimated ploidy value or number of chromosomal copies
    - Input: e.g., 2.96
    - Processing: ```sample``` -> ```results``` -> ```Estimated Ploidy```
- Callability: reliability of call quality
    - Input: e.g., 66.4
    - Processing: ```sample``` -> ```results``` -> ```Callability (%)```
- Coverage: average read coverage
    - Input: e.g., 82.2
    - Processing: ```sample``` -> ```results``` -> ```Coverage (mean)```

### 3c. Genomic Landscape: Biomarkers
- TMB value: tumour mutation burden per megabase
    - Input: e.g., 2.53
    - Processing: ```genomic_landscape``` -> ```results``` -> ```genomic_biomarker``` -> ```TMB``` -> ```Genomic biomarker value```
- MSI value: microsatellite instability per megabase
    - Input: e.g., 0.77
    - Processing: ```genomic_landscape``` -> ```results``` -> ```genomic_biomarker``` -> ```MSI``` -> ```Genomic biomarker value```
- HRD value: homologous recombination deficiency per megabase
    - Input: e.g., 2.53
    - Processing: ```genomic_landscape``` -> ```results``` -> ```genomic_biomarker``` -> ```HRD``` -> ```Genomic biomarker value```

### 3d. CNV Data
- Percent Genome Altered: percent of genome altered by cnv
    - Input: e.g., 53
    - Processing: ```wgts.cnv_purple``` -> ```results``` -> ```percent genome altered```
- Total variants: Number of total variants
    - Input: e.g., 21
    - Processing: ```wgts.cnv_purple``` -> ```results``` -> ```total variants```
- Gene: name of CNV-containing genes
    - Input: e.g., MTAP, CDKN2A, CCND1
    - Processing: ```wgts.cnv_purple``` -> ```results``` -> ```body``` -> ```Gene```
- Alteration: type of CNV event
    - Input: e.g., Deletion, Deletion, Amplification
    - Processing: ```wgts.cnv_purple``` -> ```results``` -> ```body``` -> ```Alteration```
- Chromosome: position of CNV
    - Input: e.g., 9p21.3, 9p21.3, 11q13.3
    - Processing: ```wgts.cnv_purple``` -> ```results``` -> ```body``` -> ```Chromosome```
- OncoKB: OncoKB level of evidence
    - Input: e.g., 3A, 4, N2
    - Processing: ```wgts.cnv_purple``` -> ```results``` -> ```body``` -> ```OncoKB```

### 3e. SNV/Indel Data
- Somatic Mutations: number of somatic mutations
    - Input: e.g., 205
    - Processing: ```wgts.snv_indel``` -> ```results``` -> ```somatic mutations```
- Coding Sequence Mutations: number of mutations in CDS
   - Input: e.g., 153
    - Processing: ```wgts.snv_indel``` -> ```results``` -> ```coding sequence mutations```
- Oncogenic Mutations: number of oncogenic mutations
   - Input: e.g., 1
    - Processing: ```wgts.snv_indel``` -> ```results``` -> ```oncogenic mutations```
- Gene: name of SNV-containing genes
   - Input: e.g., TP53
    - Processing: ```wgts.snv_indel``` -> ```results``` -> ```body``` -> ```Gene```
- Protein: protein alteration
   - Input: e.g., p.R306*
    - Processing: ```wgts.snv_indel``` -> ```results``` -> ```body``` -> ```protein```
- Alteration type: type of SNV event
   - Input: e.g., Nonsense Mutation
    - Processing: ```wgts.snv_indel``` -> ```results``` -> ```body``` -> ```type```
- VAF: variant allele frequency (percentage)
   - Input: e.g., 56
    - Processing: ```wgts.snv_indel``` -> ```results``` -> ```body``` -> ```vaf```
- Depth: variant read depth
   - Input: e.g., 33/56
    - Processing: ```wgts.snv_indel``` -> ```results``` -> ```body``` -> ```depth```
- LOH: whether loss of heterozygosity is exhibited
   - Input: e.g., True
    - Processing: ```wgts.snv_indel``` -> ```results``` -> ```body``` -> ```LOH```
- Chromosome: position of SNV/indel
   - Input: e.g., 17p13.1
    - Processing: ```wgts.snv_indel``` -> ```results``` -> ```body``` -> ```Chromosome```
- OncoKB: OncoKB level of evidence
   - Input: e.g., N2
    - Processing: ```wgts.snv_indel``` -> ```results``` -> ```body``` -> ```OncoKB```

### 3f. Fusion
- Total Variants: number of fusion events identified
   - Input: e.g., 5
    - Processing: ```fusion``` -> ```results``` -> ```Total variants```
- Clinically Relevant Variants: number of relevant variants as per OncoKB
   - Input: e.g., 0
    - Processing: ```fusion``` -> ```results``` -> ```Clinically relevant variants```
- NCCN Relevant Variants: number of clinically relevant variants as per NCCN
   - Input: e.g., 0
    - Processing: ```fusion``` -> ```results``` -> ```nccn_relevant_variants```

<br>

## 4. Combined Metadata Filters
- Report type: type of report
   - Input: ```clinical```, ```research```, ```supplementary```, ```failed```
    - Searching for clinical reports:
    ```
    {
    "selector": {
        "_id": { "$gt": null },
        "attributes": "clinical"
        }
    }
    ```
- ~~Requisition Approval: date of approval for testing~~
    - ~~Input: input date or sort feature~~
    - ~~Processing: ```case_overview``` -> ```requisition_approval```~~
- Last Updated: date of report's last update
    - Input: input date or sort feature
    - Processing: ```case_overview``` -> ```last_updated```