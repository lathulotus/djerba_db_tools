# Untitled string in Clinical - Report Structure Schema Schema

```txt
Week1Clinical.schema.json#/properties/case_overview/properties/assay
```

WGTS = Whole genome and transcriptome sequencing; WGS = Whole genome sequencing; TAR = Targeted sequencing.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [Week1Clinical.json\*](../../out/Week1Clinical.json "open original schema") |

## assay Type

`string`

## assay Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value    | Explanation |
| :------- | :---------- |
| `"WGTS"` |             |
| `"WGS"`  |             |
| `"TAR"`  |             |
