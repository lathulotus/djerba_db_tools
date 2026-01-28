# Clinical - Report Structure Schema Schema

```txt
Clinical.schema.json
```

Schema documentation of clinical report structures

> Latest report from 05/01/2026

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [clinical\_shema.json](../../../../../../cygwin64/home/wwwla/out/clinical_shema.json "open original schema") |

## Clinical - Report Structure Schema Type

`object` ([Clinical - Report Structure Schema](clinical_shema.md))

# Clinical - Report Structure Schema Properties

| Property                                 | Type     | Required | Nullable       | Defined by                                                                                                                                |
| :--------------------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------- |
| [case\_overview](#case_overview)         | `object` | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-case_overview.md "Clinical.schema.json#/properties/case_overview")         |
| [sample](#sample)                        | `object` | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-sample.md "Clinical.schema.json#/properties/sample")                       |
| [wgts.cnv\_purple](#wgtscnv_purple)      | `object` | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-wgtscnv_purple.md "Clinical.schema.json#/properties/wgts.cnv_purple")      |
| [wgts.snv\_indel](#wgtssnv_indel)        | `object` | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-wgtssnv_indel.md "Clinical.schema.json#/properties/wgts.snv_indel")        |
| [fusion](#fusion)                        | `object` | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-fusion.md "Clinical.schema.json#/properties/fusion")                       |
| [genomic\_landscape](#genomic_landscape) | `object` | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-genomic_landscape.md "Clinical.schema.json#/properties/genomic_landscape") |

## case\_overview

Case details: cancer type, site of biopsy, assay.

`case_overview`

* is optional

* Type: `object` ([Details](clinical_shema-properties-case_overview.md))

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-case_overview.md "Clinical.schema.json#/properties/case_overview")

### case\_overview Type

`object` ([Details](clinical_shema-properties-case_overview.md))

## sample

Sample details: cancer content, coverage.

`sample`

* is optional

* Type: `object` ([Details](clinical_shema-properties-sample.md))

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-sample.md "Clinical.schema.json#/properties/sample")

### sample Type

`object` ([Details](clinical_shema-properties-sample.md))

## wgts.cnv\_purple

Findings associated with copy number variants

`wgts.cnv_purple`

* is optional

* Type: `object` ([Details](clinical_shema-properties-wgtscnv_purple.md))

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-wgtscnv_purple.md "Clinical.schema.json#/properties/wgts.cnv_purple")

### wgts.cnv\_purple Type

`object` ([Details](clinical_shema-properties-wgtscnv_purple.md))

## wgts.snv\_indel

Findings associated with short nucleotide variants and indels

`wgts.snv_indel`

* is optional

* Type: `object` ([Details](clinical_shema-properties-wgtssnv_indel.md))

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-wgtssnv_indel.md "Clinical.schema.json#/properties/wgts.snv_indel")

### wgts.snv\_indel Type

`object` ([Details](clinical_shema-properties-wgtssnv_indel.md))

## fusion

Findings associated with gene fusions

`fusion`

* is optional

* Type: `object` ([Details](clinical_shema-properties-fusion.md))

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-fusion.md "Clinical.schema.json#/properties/fusion")

### fusion Type

`object` ([Details](clinical_shema-properties-fusion.md))

## genomic\_landscape

Genomic Landscape and Biomarkers (TMB, MSI)

`genomic_landscape`

* is optional

* Type: `object` ([Details](clinical_shema-properties-genomic_landscape.md))

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-genomic_landscape.md "Clinical.schema.json#/properties/genomic_landscape")

### genomic\_landscape Type

`object` ([Details](clinical_shema-properties-genomic_landscape.md))
