# Untitled string in Clinical - Report Structure Schema Schema

```txt
Clinical.schema.json#/properties/genomic_landscape/propterties/results/properties/genomic_biomarkers/properties/MSI/properties/Genomic biomarker alteration
```

Biomarker title

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                                     |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [clinical\_shema.json\*](../../../../../../cygwin64/home/wwwla/out/clinical_shema.json "open original schema") |

## Genomic biomarker alteration Type

`string`

## Genomic biomarker alteration Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                           | Explanation |
| :------------------------------ | :---------- |
| `"MSS"`                         |Microsatellite Stable|
| `"MSI-H"` |High Microsatellite Instability|
| `"MSI-L"` |Low Microsatellite Instability|