# Clinical Report Structure: Case Overview - Assay

```txt
Clinical.schema.json#/properties/case_overview/properties/results/properties/assay
```

Type of assay used for sequencing (WGTS, WGS, TAR)

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                                     |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [clinical\_shema.json\*](../../../../../../cygwin64/home/wwwla/out/clinical_shema.json "open original schema") |

## assay Type

`string`

## assay Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value    | Explanation                             |
| :------- | :-------------------------------------- |
| `"WGTS"` |Whole genome and transcriptome sequencing|
| `"WGS"`  |Whole genome sequencing|
| `"WES"`  |Whole exome sequencing|
| `"WTS"`  |Whole transcriptome sequencing|
| `"pWGS"` |Personalized whole genome sequencing|
| `"sWGS"` |Shallow whole genome sequencing|
| `"TAR"`  |Targeted sequencing|
