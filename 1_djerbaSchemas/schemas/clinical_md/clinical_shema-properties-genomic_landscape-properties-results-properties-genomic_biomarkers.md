# Clinical Report Structure: Genomic Landscape - Genomic Biomarkers

```txt
Clinical.schema.json#/properties/genomic_landscape/propterties/results/properties/genomic_biomarkers
```

Genomic biomarkers (TMB, MSI, HRD)

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                                     |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [clinical\_shema.json\*](../../../../../../cygwin64/home/wwwla/out/clinical_shema.json "open original schema") |

## genomic\_biomarkers Type

`object` ([Details](clinical_shema-properties-genomic_landscape-propterties-results-properties-genomic_biomarkers.md))

# genomic\_biomarkers Properties

| Property    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                  |
| :---------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [TMB](#tmb) | `object` | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-genomic_landscape-propterties-results-properties-genomic_biomarkers-properties-tmb.md "Clinical.schema.json#/properties/genomic_landscape/propterties/results/properties/genomic_biomarkers/properties/TMB") |
| [MSI](#msi) | `object` | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-genomic_landscape-propterties-results-properties-genomic_biomarkers-properties-msi.md "Clinical.schema.json#/properties/genomic_landscape/propterties/results/properties/genomic_biomarkers/properties/MSI") |
| [HRD](#hrd) | `object` | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-genomic_landscape-propterties-results-properties-genomic_biomarkers-properties-hrd.md "Clinical.schema.json#/properties/genomic_landscape/propterties/results/properties/genomic_biomarkers/properties/HRD") |

## TMB

Tumour Mutation Burden

`TMB`

* is optional

* Type: `object` ([Details](clinical_shema-properties-genomic_landscape-propterties-results-properties-genomic_biomarkers-properties-tmb.md))

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-genomic_landscape-propterties-results-properties-genomic_biomarkers-properties-tmb.md "Clinical.schema.json#/properties/genomic_landscape/propterties/results/properties/genomic_biomarkers/properties/TMB")

### TMB Type

`object` ([Details](clinical_shema-properties-genomic_landscape-propterties-results-properties-genomic_biomarkers-properties-tmb.md))

## MSI

Microsatellite Instability

`MSI`

* is optional

* Type: `object` ([Details](clinical_shema-properties-genomic_landscape-propterties-results-properties-genomic_biomarkers-properties-msi.md))

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-genomic_landscape-propterties-results-properties-genomic_biomarkers-properties-msi.md "Clinical.schema.json#/properties/genomic_landscape/propterties/results/properties/genomic_biomarkers/properties/MSI")

### MSI Type

`object` ([Details](clinical_shema-properties-genomic_landscape-propterties-results-properties-genomic_biomarkers-properties-msi.md))

## HRD

Homologous Recombination Deficiency

`HRD`

* is optional

* Type: `object` ([Details](clinical_shema-properties-genomic_landscape-propterties-results-properties-genomic_biomarkers-properties-hrd.md))

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-genomic_landscape-propterties-results-properties-genomic_biomarkers-properties-hrd.md "Clinical.schema.json#/properties/genomic_landscape/propterties/results/properties/genomic_biomarkers/properties/HRD")

### HRD Type

`object` ([Details](clinical_shema-properties-genomic_landscape-propterties-results-properties-genomic_biomarkers-properties-hrd.md))
