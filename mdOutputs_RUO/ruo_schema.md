# RUO - Report Structure Schema Schema

```txt
RUO.schema.json
```

Schema documentation of RUO report structures

> Latest report from 24/12/2025

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [ruo\_schema.json](../../../../../../cygwin64/home/wwwla/out/ruo_schema.json "open original schema") |

## RUO - Report Structure Schema Type

`object` ([RUO - Report Structure Schema](ruo_schema.md))

# RUO - Report Structure Schema Properties

| Property                                 | Type     | Required | Nullable       | Defined by                                                                                                                  |
| :--------------------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------- |
| [case\_overview](#case_overview)         | `object` | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-case_overview.md "RUO.schema.json#/properties/case_overview")         |
| [samples](#samples)                      | `object` | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-samples.md "RUO.schema.json#/properties/samples")                     |
| [cnv](#cnv)                              | `object` | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-cnv.md "RUO.schema.json#/properties/cnv")                             |
| [wgts.snv\_indel](#wgtssnv_indel)        | `object` | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-wgtssnv_indel.md "RUO.schema.json#/properties/wgts.snv_indel")        |
| [fusion](#fusion)                        | `object` | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-fusion.md "RUO.schema.json#/properties/fusion")                       |
| [genomic\_landscape](#genomic_landscape) | `object` | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-genomic_landscape.md "RUO.schema.json#/properties/genomic_landscape") |

## case\_overview

Case details: cancer type, site of biopsy, assay.

`case_overview`

* is optional

* Type: `object` ([Details](ruo_schema-properties-case_overview.md))

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-case_overview.md "RUO.schema.json#/properties/case_overview")

### case\_overview Type

`object` ([Details](ruo_schema-properties-case_overview.md))

## samples

Sample details: cancer content, coverage.

`samples`

* is optional

* Type: `object` ([Details](ruo_schema-properties-samples.md))

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-samples.md "RUO.schema.json#/properties/samples")

### samples Type

`object` ([Details](ruo_schema-properties-samples.md))

## cnv

Findings associated with copy number variants

`cnv`

* is optional

* Type: `object` ([Details](ruo_schema-properties-cnv.md))

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-cnv.md "RUO.schema.json#/properties/cnv")

### cnv Type

`object` ([Details](ruo_schema-properties-cnv.md))

## wgts.snv\_indel

Findings associated with short nucleotide variants and indels

`wgts.snv_indel`

* is optional

* Type: `object` ([Details](ruo_schema-properties-wgtssnv_indel.md))

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-wgtssnv_indel.md "RUO.schema.json#/properties/wgts.snv_indel")

### wgts.snv\_indel Type

`object` ([Details](ruo_schema-properties-wgtssnv_indel.md))

## fusion

Findings associated with gene fusions

`fusion`

* is optional

* Type: `object` ([Details](ruo_schema-properties-fusion.md))

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-fusion.md "RUO.schema.json#/properties/fusion")

### fusion Type

`object` ([Details](ruo_schema-properties-fusion.md))

## genomic\_landscape

Genomic Landscape and Biomarkers (TMB, MSI)

`genomic_landscape`

* is optional

* Type: `object` ([Details](ruo_schema-properties-genomic_landscape.md))

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-genomic_landscape.md "RUO.schema.json#/properties/genomic_landscape")

### genomic\_landscape Type

`object` ([Details](ruo_schema-properties-genomic_landscape.md))
