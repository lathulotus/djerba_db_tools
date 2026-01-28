# Untitled object in Clinical - Report Structure Schema Schema

```txt
Clinical.schema.json#/properties/genomic_landscape/propterties/results
```

Results pertaining to landscape and biomarkers

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                                     |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [clinical\_shema.json\*](../../../../../../cygwin64/home/wwwla/out/clinical_shema.json "open original schema") |

## results Type

`object` ([Details](clinical_shema-properties-genomic_landscape-propterties-results.md))

# results Properties

| Property                                            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                            |
| :-------------------------------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [genomic\_landscape\_info](#genomic_landscape_info) | `object` | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-genomic_landscape-propterties-results-properties-genomic_landscape_info.md "Clinical.schema.json#/properties/genomic_landscape/propterties/results/properties/genomic_landscape_info") |
| [genomic\_biomarkers](#genomic_biomarkers)          | `object` | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-genomic_landscape-propterties-results-properties-genomic_biomarkers.md "Clinical.schema.json#/properties/genomic_landscape/propterties/results/properties/genomic_biomarkers")         |

## genomic\_landscape\_info

Genomic landscape

`genomic_landscape_info`

* is optional

* Type: `object` ([Details](clinical_shema-properties-genomic_landscape-propterties-results-properties-genomic_landscape_info.md))

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-genomic_landscape-propterties-results-properties-genomic_landscape_info.md "Clinical.schema.json#/properties/genomic_landscape/propterties/results/properties/genomic_landscape_info")

### genomic\_landscape\_info Type

`object` ([Details](clinical_shema-properties-genomic_landscape-propterties-results-properties-genomic_landscape_info.md))

## genomic\_biomarkers

Genomic biomarkers (TMB, MSI, HRD)

`genomic_biomarkers`

* is optional

* Type: `object` ([Details](clinical_shema-properties-genomic_landscape-propterties-results-properties-genomic_biomarkers.md))

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-genomic_landscape-propterties-results-properties-genomic_biomarkers.md "Clinical.schema.json#/properties/genomic_landscape/propterties/results/properties/genomic_biomarkers")

### genomic\_biomarkers Type

`object` ([Details](clinical_shema-properties-genomic_landscape-propterties-results-properties-genomic_biomarkers.md))
