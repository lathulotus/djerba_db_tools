# Clinical - Report Structure Schema Schema

```txt
Week1Clinical.schema.json
```

Schema documentation of clinical report structures

> Latest report from 05/01/2026

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [Week1Clinical.json](../../out/Week1Clinical.json "open original schema") |

## Clinical - Report Structure Schema Type

`object` ([Clinical - Report Structure Schema](week1clinical.md))

# Clinical - Report Structure Schema Properties

| Property                                                | Type     | Required | Nullable       | Defined by                                                                                                                                                  |
| :------------------------------------------------------ | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [case\_overview](#case_overview)                        | `object` | Optional | cannot be null | [Clinical - Report Structure Schema](week1clinical-properties-case_overview.md "Week1Clinical.schema.json#/properties/case_overview")                       |
| [sample](#sample)                                       | `object` | Optional | cannot be null | [Clinical - Report Structure Schema](week1clinical-properties-sample.md "Week1Clinical.schema.json#/properties/sample")                                     |
| [results](#results)                                     | `object` | Optional | cannot be null | [Clinical - Report Structure Schema](week1clinical-properties-results.md "Week1Clinical.schema.json#/properties/results")                                   |
| [treatment\_options\_merger](#treatment_options_merger) | `object` | Optional | cannot be null | [Clinical - Report Structure Schema](week1clinical-properties-treatment_options_merger.md "Week1Clinical.schema.json#/properties/treatment_options_merger") |

## case\_overview

Overall case details

`case_overview`

* is optional

* Type: `object` ([Details](week1clinical-properties-case_overview.md))

* cannot be null

* defined in: [Clinical - Report Structure Schema](week1clinical-properties-case_overview.md "Week1Clinical.schema.json#/properties/case_overview")

### case\_overview Type

`object` ([Details](week1clinical-properties-case_overview.md))

## sample

Sample information

`sample`

* is optional

* Type: `object` ([Details](week1clinical-properties-sample.md))

* cannot be null

* defined in: [Clinical - Report Structure Schema](week1clinical-properties-sample.md "Week1Clinical.schema.json#/properties/sample")

### sample Type

`object` ([Details](week1clinical-properties-sample.md))

## results

Results from testing; assay in report ID

`results`

* is optional

* Type: `object` ([Details](week1clinical-properties-results.md))

* cannot be null

* defined in: [Clinical - Report Structure Schema](week1clinical-properties-results.md "Week1Clinical.schema.json#/properties/results")

### results Type

`object` ([Details](week1clinical-properties-results.md))

## treatment\_options\_merger

Treatment options merged; plugin

`treatment_options_merger`

* is optional

* Type: `object` ([Details](week1clinical-properties-treatment_options_merger.md))

* cannot be null

* defined in: [Clinical - Report Structure Schema](week1clinical-properties-treatment_options_merger.md "Week1Clinical.schema.json#/properties/treatment_options_merger")

### treatment\_options\_merger Type

`object` ([Details](week1clinical-properties-treatment_options_merger.md))
