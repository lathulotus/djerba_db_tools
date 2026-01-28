# Untitled object in Clinical - Report Structure Schema Schema

```txt
Clinical.schema.json#/properties/sample/properties/results
```

Results covering sample details

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                                     |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [clinical\_shema.json\*](../../../../../../cygwin64/home/wwwla/out/clinical_shema.json "open original schema") |

## results Type

`object` ([Details](clinical_shema-properties-sample-properties-results.md))

# results Properties

| Property                                                             | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                       |
| :------------------------------------------------------------------- | :-------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [OncoTree code](#oncotree-code)                                      | `string`  | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-sample-properties-results-properties-oncotree-code.md "Clinical.schema.json#/properties/sample/properties/results/properties/OncoTree code")                                      |
| [Sample Type](#sample-type)                                          | `string`  | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-sample-properties-results-properties-sample-type.md "Clinical.schema.json#/properties/sample/properties/results/properties/Sample Type")                                          |
| [Estimated Cancer Cell Content (%)](#estimated-cancer-cell-content-) | `integer` | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-sample-properties-results-properties-estimated-cancer-cell-content-.md "Clinical.schema.json#/properties/sample/properties/results/properties/Estimated Cancer Cell Content (%)") |
| [Estimated Ploidy](#estimated-ploidy)                                | `string`  | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-sample-properties-results-properties-estimated-ploidy.md "Clinical.schema.json#/properties/sample/properties/results/properties/Estimated Ploidy")                                |
| [Callability (%)](#callability-)                                     | `string`  | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-sample-properties-results-properties-callability-.md "Clinical.schema.json#/properties/sample/properties/results/properties/Callability (%)")                                     |
| [Coverage (mean)](#coverage-mean)                                    | `string`  | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-sample-properties-results-properties-coverage-mean.md "Clinical.schema.json#/properties/sample/properties/results/properties/Coverage (mean)")                                    |

## OncoTree code

OncoTree-standardized code for cancer identification

`OncoTree code`

* is optional

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-sample-properties-results-properties-oncotree-code.md "Clinical.schema.json#/properties/sample/properties/results/properties/OncoTree code")

### OncoTree code Type

`string`

## Sample Type

Type of sample

`Sample Type`

* is optional

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-sample-properties-results-properties-sample-type.md "Clinical.schema.json#/properties/sample/properties/results/properties/Sample Type")

### Sample Type Type

`string`

### Sample Type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value     | Explanation |
| :-------- | :---------- |
| `"Fresh frozen"` |Fresh Frozen (FF)|
| `"FFPE"`    |Formalin-Fixed Paraffin-Embedded|
| `"Blood"`  |Fresh, whole blood|
|`"Nucleic Acids Extracted from Tissue in a CLIA-certified Laboratory"`|Nucleic Acid Extraction|

## Estimated Cancer Cell Content (%)

Estimated percentage of cancer cell content

`Estimated Cancer Cell Content (%)`

* is optional

* Type: `integer`

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-sample-properties-results-properties-estimated-cancer-cell-content-.md "Clinical.schema.json#/properties/sample/properties/results/properties/Estimated Cancer Cell Content (%)")

### Estimated Cancer Cell Content (%) Type

`integer`

## Estimated Ploidy

Estimated ploidy value

`Estimated Ploidy`

* is optional

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-sample-properties-results-properties-estimated-ploidy.md "Clinical.schema.json#/properties/sample/properties/results/properties/Estimated Ploidy")

### Estimated Ploidy Type

`string`

## Callability (%)

Call quality

`Callability (%)`

* is optional

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-sample-properties-results-properties-callability-.md "Clinical.schema.json#/properties/sample/properties/results/properties/Callability (%)")

### Callability (%) Type

`string`

## Coverage (mean)

Average coverage

`Coverage (mean)`

* is optional

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-sample-properties-results-properties-coverage-mean.md "Clinical.schema.json#/properties/sample/properties/results/properties/Coverage (mean)")

### Coverage (mean) Type

`string`
