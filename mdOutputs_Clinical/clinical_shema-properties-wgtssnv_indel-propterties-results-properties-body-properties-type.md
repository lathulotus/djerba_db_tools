# Untitled string in Clinical - Report Structure Schema Schema

```txt
Clinical.schema.json#/properties/wgts.snv_indel/propterties/results/properties/body/properties/type
```

Type of SNV event

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                                     |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [clinical\_shema.json\*](../../../../../../cygwin64/home/wwwla/out/clinical_shema.json "open original schema") |

## type Type

`string`

## type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                 | Explanation |
| :-------------------- | :---------- |
| `"Missense Mutation"` |             |
| `"Nonsense Mutation"` |             |
| `"Frame Shift Del"`   |             |
| `"Frame Shift Ins"`   |             |
| `"Splice Site"`       |             |
| `"Splice Region"`     |             |
