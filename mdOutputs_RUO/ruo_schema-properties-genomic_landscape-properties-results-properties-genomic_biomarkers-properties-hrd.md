# Untitled object in RUO - Report Structure Schema Schema

```txt
RUO.schema.json#/properties/genomic_landscape/propterties/results/properties/genomic_biomarkers/properties/HRD
```

Homologous Recombination Deficiency

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                             |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [ruo\_schema.json\*](../../../../../../cygwin64/home/wwwla/out/ruo_schema.json "open original schema") |

## HRD Type

`object` ([Details](ruo_schema-properties-genomic_landscape-propterties-results-properties-genomic_biomarkers-properties-hrd.md))

# HRD Properties

| Property                                                      | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                    |
| :------------------------------------------------------------ | :-------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Genomic biomarker value](#genomic-biomarker-value)           | `integer` | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-genomic_landscape-propterties-results-properties-genomic_biomarkers-properties-hrd-properties-genomic-biomarker-value.md "RUO.schema.json#/properties/genomic_landscape/propterties/results/properties/genomic_biomarkers/properties/HRD/properties/Genomic biomarker value")           |
| [Genomic biomarker alteration](#genomic-biomarker-alteration) | `string`  | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-genomic_landscape-propterties-results-properties-genomic_biomarkers-properties-hrd-properties-genomic-biomarker-alteration.md "RUO.schema.json#/properties/genomic_landscape/propterties/results/properties/genomic_biomarkers/properties/HRD/properties/Genomic biomarker alteration") |

## Genomic biomarker value

HRD per megabase

`Genomic biomarker value`

* is optional

* Type: `integer`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-genomic_landscape-propterties-results-properties-genomic_biomarkers-properties-hrd-properties-genomic-biomarker-value.md "RUO.schema.json#/properties/genomic_landscape/propterties/results/properties/genomic_biomarkers/properties/HRD/properties/Genomic biomarker value")

### Genomic biomarker value Type

`integer`

## Genomic biomarker alteration

Biomarker title

`Genomic biomarker alteration`

* is optional

* Type: `string`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-genomic_landscape-propterties-results-properties-genomic_biomarkers-properties-hrd-properties-genomic-biomarker-alteration.md "RUO.schema.json#/properties/genomic_landscape/propterties/results/properties/genomic_biomarkers/properties/HRD/properties/Genomic biomarker alteration")

### Genomic biomarker alteration Type

`string`

### Genomic biomarker alteration Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation |
| :---- | :---------- |
| `""`  |             |
