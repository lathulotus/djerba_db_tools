# Untitled string in RUO - Report Structure Schema Schema

```txt
RUO.schema.json#/properties/results/properties/type
```

Type of specific alteration or biological event (Missense Mutation, Nonsense Mutation, Frame Shift Del, Frame Shift Ins, Splice Site, Splice Region)

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                             |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [ruo\_schema.json\*](../../../../../../cygwin64/home/wwwla/out/ruo_schema.json "open original schema") |

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
