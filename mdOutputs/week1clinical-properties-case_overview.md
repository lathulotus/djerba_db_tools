# Untitled object in Clinical - Report Structure Schema Schema

```txt
Week1Clinical.schema.json#/properties/case_overview
```

Overall case details.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [Week1Clinical.json\*](../../out/Week1Clinical.json "open original schema") |

## case\_overview Type

`object` ([Details](week1clinical-properties-case_overview.md))

# case\_overview Properties

| Property                            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                |
| :---------------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [assay](#assay)                     | `string` | Optional | cannot be null | [Clinical - Report Structure Schema](week1clinical-properties-case_overview-properties-assay.md "Week1Clinical.schema.json#/properties/case_overview/properties/assay")                   |
| [primary\_cancer](#primary_cancer)  | `string` | Optional | cannot be null | [Clinical - Report Structure Schema](week1clinical-properties-case_overview-properties-primary_cancer.md "Week1Clinical.schema.json#/properties/case_overview/properties/primary_cancer") |
| [OncoTree code](#oncotree-code)     | `string` | Optional | cannot be null | [Clinical - Report Structure Schema](week1clinical-properties-case_overview-properties-oncotree-code.md "Week1Clinical.schema.json#/properties/case_overview/properties/OncoTree code")   |
| [site\_of\_biopsy](#site_of_biopsy) | `string` | Optional | cannot be null | [Clinical - Report Structure Schema](week1clinical-properties-case_overview-properties-site_of_biopsy.md "Week1Clinical.schema.json#/properties/case_overview/properties/site_of_biopsy") |

## assay

Type of assay used for sequencing.

`assay`

* is optional

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](week1clinical-properties-case_overview-properties-assay.md "Week1Clinical.schema.json#/properties/case_overview/properties/assay")

### assay Type

`string`

### assay Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value    | Explanation |
| :------- | :---------- |
| `"WGTS"` |Whole genome and transcriptome sequencing|
| `"WGS"`  |Whole genome sequencing|
| `"TAR"`  |Targeted sequencing|

## primary\_cancer

Type of cancer.

`primary_cancer`

* is optional

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](week1clinical-properties-case_overview-properties-primary_cancer.md "Week1Clinical.schema.json#/properties/case_overview/properties/primary_cancer")

### primary\_cancer Type

`string`

### primary\_cancer Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                         | Explanation |
| :---------------------------- | :---------- |
| `"Pancreatic adenocarcinoma"` |Pancreatic|
| `"Hepatobiliary Tumour"`      |Hepatobiliary|
| `"Multiple Myeloma"`          |Blood|
| `"Breast Cancer"`             |Breast|
| `"Invasive breast carcinoma"` |Breast|

## OncoTree code

OncoTree code associated with cancer type & subtype

`OncoTree code`

* is optional

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](week1clinical-properties-case_overview-properties-oncotree-code.md "Week1Clinical.schema.json#/properties/case_overview/properties/OncoTree code")

### OncoTree code Type

`string`

## site\_of\_biopsy

Biopsy type/location (cfDNA, Liver, Bone Marrow, Soft Tissue, Left Breast, Perihepatic)

`site_of_biopsy`

* is optional

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](week1clinical-properties-case_overview-properties-site_of_biopsy.md "Week1Clinical.schema.json#/properties/case_overview/properties/site_of_biopsy")

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
