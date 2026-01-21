# Untitled object in RUO - Report Structure Schema Schema

```txt
RUO.schema.json#/properties/case_overview/properties/results
```

Results covering case overview

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                             |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [ruo\_schema.json\*](../../../../../../cygwin64/home/wwwla/out/ruo_schema.json "open original schema") |

## results Type

`object` ([Details](ruo_schema-properties-case_overview-properties-results.md))

# results Properties

| Property                            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                    |
| :---------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [assay](#assay)                     | `string` | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-case_overview-properties-results-properties-assay.md "RUO.schema.json#/properties/case_overview/properties/results/properties/assay")                   |
| [study](#study)                     | `string` | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-case_overview-properties-results-properties-study.md "RUO.schema.json#/properties/case_overview/properties/results/properties/study")                   |
| [report_id](#report_id)                 | `string` | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-case_overview-properties-results-properties-report_id.md "RUO.schema.json#/properties/case_overview/properties/results/properties/report_id")               |
| [project](#project)                 | `string` | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-case_overview-properties-results-properties-project.md "RUO.schema.json#/properties/case_overview/properties/results/properties/project")               |

## assay

Type of assay used for sequencing (WGTS, WGS, TAR)

`assay`

* is optional

* Type: `string`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-case_overview-properties-results-properties-assay.md "RUO.schema.json#/properties/case_overview/properties/results/properties/assay")

### assay Type

`string`

### assay Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value    | Explanation                             |
| :------- | :-------------------------------------- |
| `"WGTS"` |Whole genome and transcriptome sequencing|
| `"WGS"`  |Whole genome sequencing|
| `"WES"`  |Whole exome sequencing|
| `"WTS"`  |Whole transcriptome sequencing|
| `"pWGS"` |Personalized whole genome sequencing|
| `"sWGS"` |Shallow whole genome sequencing|
| `"TAR"`  |Targeted sequencing|

## study

Research study name

`study`

* is optional

* Type: `string`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-case_overview-properties-results-properties-study.md "RUO.schema.json#/properties/case_overview/properties/results/properties/study")

### study Type

`string`

## report_id

Report identifier; can be used for single report fetching

`report_id`

* is optional

* Type: `string`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-case_overview-properties-results-properties-report_id.md "RUO.schema.json#/properties/case_overview/properties/results/properties/report_id")

### last_updated Type

`string`

## last_updated

Date of report

`last_updated`

* is optional

* Type: `string`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-case_overview-properties-results-properties-last_updated.md "RUO.schema.json#/properties/case_overview/properties/results/properties/last_updated")

### last_updated Type

`string`