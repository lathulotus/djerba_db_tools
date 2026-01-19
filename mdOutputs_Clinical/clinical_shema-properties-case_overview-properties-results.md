# Untitled object in Clinical - Report Structure Schema Schema

```txt
Clinical.schema.json#/properties/case_overview/properties/results
```

Results covering case overview

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                                     |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [clinical\_shema.json\*](../../../../../../cygwin64/home/wwwla/out/clinical_shema.json "open original schema") |

## results Type

`object` ([Details](clinical_shema-properties-case_overview-properties-results.md))

# results Properties

| Property                            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                  |
| :---------------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [assay](#assay)                     | `string` | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-case_overview-properties-results-properties-assay.md "Clinical.schema.json#/properties/case_overview/properties/results/properties/assay")                   |
| [primary\_cancer](#primary_cancer)  | `string` | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-case_overview-properties-results-properties-primary_cancer.md "Clinical.schema.json#/properties/case_overview/properties/results/properties/primary_cancer") |
| [site\_of\_biopsy](#site_of_biopsy) | `string` | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-case_overview-properties-results-properties-site_of_biopsy.md "Clinical.schema.json#/properties/case_overview/properties/results/properties/site_of_biopsy") |
| [study](#study)                     | `string` | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-case_overview-properties-results-properties-study.md "Clinical.schema.json#/properties/case_overview/properties/results/properties/study")                   |

## assay

Type of assay used for sequencing (WGTS, WGS, TAR)

`assay`

* is optional

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-case_overview-properties-results-properties-assay.md "Clinical.schema.json#/properties/case_overview/properties/results/properties/assay")

### assay Type

`string`

### assay Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value    | Explanation |
| :------- | :---------- |
| `"WGTS"` |             |
| `"WGS"`  |             |
| `"TAR"`  |             |

## primary\_cancer

Cancer type.

`primary_cancer`

* is optional

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-case_overview-properties-results-properties-primary_cancer.md "Clinical.schema.json#/properties/case_overview/properties/results/properties/primary_cancer")

### primary\_cancer Type

`string`

### primary\_cancer Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                         | Explanation |
| :---------------------------- | :---------- |
| `"Pancreatic adenocarcinoma"` |             |
| `"Hepatobiliary Tumour"`      |             |
| `"Multiple Myeloma"`          |             |
| `"Breast Cancer"`             |             |
| `"Invasive breast carcinoma"` |             |

## site\_of\_biopsy

Biopsy type/location (cfDNA)

`site_of_biopsy`

* is optional

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-case_overview-properties-results-properties-site_of_biopsy.md "Clinical.schema.json#/properties/case_overview/properties/results/properties/site_of_biopsy")

### site\_of\_biopsy Type

`string`

### site\_of\_biopsy Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                          | Explanation |
| :----------------------------- | :---------- |
| `"cfDNA"`                      |             |
| `"Liver"`                      |             |
| `"Bone Marrow"`                |             |
| `"Left 4th Rib - Soft Tissue"` |             |
| `"Left Breast"`                |             |
| `"Perihepatic"`                |             |

## study

Research study name

`study`

* is optional

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-case_overview-properties-results-properties-study.md "Clinical.schema.json#/properties/case_overview/properties/results/properties/study")

### study Type

`string`
