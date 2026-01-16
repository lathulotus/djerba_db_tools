# Untitled string in Clinical - Report Structure Schema Schema

```txt
Week1Clinical.schema.json#/properties/results/properties/type
```

Specific type of specific alteration (variant type).

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [Week1Clinical.json\*](../../out/Week1Clinical.json "open original schema") |

## type Type

`string`

## type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                 | Explanation |
| :-------------------- | :---------- |
| `"Missense Mutation"` |Variant causing amino acid change|
| `"Nonsense Mutation"` |Variant causing premature stop codon|
| `"Frame Shift Del"`   |Deletion causing frameshift|
| `"Frame Shift Ins"`   |Insertion causing frameshift|
| `"Splice Site"`       |Variant affecting canonical splice sites|
| `"Splice Region"`     |Variant in splice region outside canonical sites|
