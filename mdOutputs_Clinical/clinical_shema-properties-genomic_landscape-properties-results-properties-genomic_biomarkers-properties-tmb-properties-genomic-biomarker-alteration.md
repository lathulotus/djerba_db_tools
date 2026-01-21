# Clinical Report Structure: Genomic Landscape: Biomarker Value (TMB)

```txt
Clinical.schema.json#/properties/genomic_landscape/propterties/results/properties/genomic_biomarkers/properties/TMB/properties/Genomic biomarker alteration
```

Biomarker title

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                                     |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [clinical\_shema.json\*](../../../../../../cygwin64/home/wwwla/out/clinical_shema.json "open original schema") |

## Genomic biomarker alteration Type

`string`

## Genomic biomarker alteration Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value     | Explanation |
| :-------- | :---------- |
| `"TMB-L"` |Low Tumour Mutation Burden|
| `"TMB-H"` |High Tumour Mutation Burden|
| `"TMB-I"` |Intermediate Tumour Mutation Burden|
