# Clinical - Report Structure Schema Schema

```txt
Clinical.schema.json
```

Schema documentation of clinical report structures

> Latest report from 05/01/2026

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                                     |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [clinical\_schema.json](../../../../../../cygwin64/home/wwwla/out/clinical_schema.json "open original schema") |

## Clinical - Report Structure Schema Type

`object` ([Clinical - Report Structure Schema](clinical_schema.md))

# Clinical - Report Structure Schema Properties

| Property                         | Type     | Required | Nullable       | Defined by                                                                                                                         |
| :------------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| [case\_overview](#case_overview) | `object` | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_schema-properties-case_overview.md "Clinical.schema.json#/properties/case_overview") |
| [sample](#sample)                | `object` | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_schema-properties-sample.md "Clinical.schema.json#/properties/sample")               |
| [results](#results)              | `object` | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_schema-properties-results.md "Clinical.schema.json#/properties/results")             |

## case\_overview

Overall case details

`case_overview`

* is optional

* Type: `object` ([Details](clinical_schema-properties-case_overview.md))

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_schema-properties-case_overview.md "Clinical.schema.json#/properties/case_overview")

### case\_overview Type

`object` ([Details](clinical_schema-properties-case_overview.md))

## sample

Sample information

`sample`

* is optional

* Type: `object` ([Details](clinical_schema-properties-sample.md))

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_schema-properties-sample.md "Clinical.schema.json#/properties/sample")

### sample Type

`object` ([Details](clinical_schema-properties-sample.md))

## results

Results from testing; assay in report ID

`results`

* is optional

* Type: `object` ([Details](clinical_schema-properties-results.md))

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_schema-properties-results.md "Clinical.schema.json#/properties/results")

### results Type

`object` ([Details](clinical_schema-properties-results.md))
