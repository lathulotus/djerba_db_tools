# Untitled object in Clinical - Report Structure Schema Schema

```txt
Clinical.schema.json#/properties/genomic_landscape/propterties/results/properties/genomic_biomarkers/properties/MSI
```

Microsatellite Instability

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                                     |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [clinical\_shema.json\*](../../../../../../cygwin64/home/wwwla/out/clinical_shema.json "open original schema") |

## MSI Type

`object` ([Details](clinical_shema-properties-genomic_landscape-propterties-results-properties-genomic_biomarkers-properties-msi.md))

# MSI Properties

| Property                                                      | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                  |
| :------------------------------------------------------------ | :-------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Genomic biomarker value](#genomic-biomarker-value)           | `integer` | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-genomic_landscape-propterties-results-properties-genomic_biomarkers-properties-msi-properties-genomic-biomarker-value.md "Clinical.schema.json#/properties/genomic_landscape/propterties/results/properties/genomic_biomarkers/properties/MSI/properties/Genomic biomarker value")           |
| [Genomic biomarker alteration](#genomic-biomarker-alteration) | `string`  | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-genomic_landscape-propterties-results-properties-genomic_biomarkers-properties-msi-properties-genomic-biomarker-alteration.md "Clinical.schema.json#/properties/genomic_landscape/propterties/results/properties/genomic_biomarkers/properties/MSI/properties/Genomic biomarker alteration") |

## Genomic biomarker value

MSI per megabase

`Genomic biomarker value`

* is optional

* Type: `integer`

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-genomic_landscape-propterties-results-properties-genomic_biomarkers-properties-msi-properties-genomic-biomarker-value.md "Clinical.schema.json#/properties/genomic_landscape/propterties/results/properties/genomic_biomarkers/properties/MSI/properties/Genomic biomarker value")

### Genomic biomarker value Type

`integer`

## Genomic biomarker alteration

Biomarker title

`Genomic biomarker alteration`

* is optional

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-genomic_landscape-propterties-results-properties-genomic_biomarkers-properties-msi-properties-genomic-biomarker-alteration.md "Clinical.schema.json#/properties/genomic_landscape/propterties/results/properties/genomic_biomarkers/properties/MSI/properties/Genomic biomarker alteration")

### Genomic biomarker alteration Type

`string`

### Genomic biomarker alteration Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                           | Explanation |
| :------------------------------ | :---------- |
| `"MSS"`                         |             |
| `"Microsatellite Stable (MSS)"` |             |
