# README

## Top-level Schemas
* [Clinical - Report Structure Schema](https://github.com/lathulotus/CGIWeek1_2/blob/main/jsonSchemas/clinical_schema.json) – `Clinical.schema.json`

## Top-level Fields
* case_overview: assay, primary cancer, oncotree code, site of biopsy
* sample: sample type, estimated cancer cell content, estimated ploidy, callability
* results: genomic biomarkers (TMB, HRD, MSI), mutations (somatic, oncogenic, CDS), genes, protein-level change, variant type, VAF, depth, LOH, position

## Variant fields
case_overview
* assay: string, genomic sequencing assay
* primary_cancer: string, cancer type
* OncoTree code: string, code associated with cancer
* site_of_biopsy: string, biopsy type/location

sample
*  Sample type: string, collection type
*  Estimated Cancer Cell Content (%): integer, percent of cancer cell content
*  Estimated Ploidy: string, estimated ploidy
*  Callability (%): string, accuracy of call

results
*  Tumour Mutation Burden: integer, total TMB
*  TMB per megabase: integer, relative TMB value
*  genomic_biomarkers: object, TMB/HRD/MSI values
    **   Genomic biomarker value: integer, value per megabase
    **   Genomic alteration actionable: boolean, actionability
*  somatic mutations: integer, number of somatic mutations
*  coding sequence mutations: integer, number of CDS mutations
*  oncogenic mutations: integer, number of oncogenic mutations
*  Gene: string, gene names
*  protein: string, protein alterations
*  type: string, variant classification
*  vaf: integer, variant allele frequency
*  depth: string, variant read depth
*  LOH: boolean, loss of heterozygosity exhibited
*  Chromosome: string, position
*  percent genome altered: integer, alteration from variant
*  total variants: integer, number of variants
*  clinically relevant variants: integer, number of clinically relevant variants

## Other Schemas

### Objects

* [Untitled object in Clinical - Report Structure Schema](./week1clinical-properties-case_overview.md "Overall case details") – `Week1Clinical.schema.json#/properties/case_overview`

* [Untitled object in Clinical - Report Structure Schema](./week1clinical-properties-sample.md "Sample information") – `Week1Clinical.schema.json#/properties/sample`

* [Untitled object in Clinical - Report Structure Schema](./week1clinical-properties-results.md "Results from testing; assay in report ID") – `Week1Clinical.schema.json#/properties/results`

* [Untitled object in Clinical - Report Structure Schema](./week1clinical-properties-results-properties-genomic_landscape_info.md "Genomic landscape-- TMB, cohorts, percentiles") – `Week1Clinical.schema.json#/properties/results/properties/genomic_landscape_info`

* [Untitled object in Clinical - Report Structure Schema](./week1clinical-properties-results-properties-genomic_biomarkers-tmb.md "Tumour mutation burden - high") – `Week1Clinical.schema.json#/properties/results/properties/genomic_biomarkers/TMB`

* [Untitled object in Clinical - Report Structure Schema](./week1clinical-properties-results-properties-genomic_biomarkers-hrd.md "Homologous recombination defficiency") – `Week1Clinical.schema.json#/properties/results/properties/genomic_biomarkers/HRD`

* [Untitled object in Clinical - Report Structure Schema](./week1clinical-properties-results-properties-genomic_biomarkers-msi.md "Microsatellite instability") – `Week1Clinical.schema.json#/properties/results/properties/genomic_biomarkers/MSI`

* [Untitled object in Clinical - Report Structure Schema](./week1clinical-properties-treatment_options_merger.md "Treatment options merged; plugin") – `Week1Clinical.schema.json#/properties/treatment_options_merger`

### Arrays



## Version Note

The schemas linked above follow the JSON Schema Spec version: `http://json-schema.org/draft-07/schema#`
