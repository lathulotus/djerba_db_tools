# Untitled string in RUO - Report Structure Schema Schema

```txt
RUO.schema.json#/properties/case_overview/properties/results/properties/assay
```

Type of assay used for sequencing (WGTS, WGS, TAR)

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                             |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [ruo\_schema.json\*](../../../../../../cygwin64/home/wwwla/out/ruo_schema.json "open original schema") |

## assay Type

`string`

## assay Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value    | Explanation |
| :------- | :---------- |
| `"WGTS"` |             |
| `"WGS"`  |             |
| `"TAR"`  |             |
