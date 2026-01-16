# Untitled string in Clinical - Report Structure Schema Schema

```txt
Week1Clinical.schema.json#/properties/sample/properties/Sample type
```

Fresh = Fresh unfrozen; FF = Fresh frozen; FFPE = Formalin-fixed, paraffin-embedded; Blood = Whole blood; Plasma = Plasma sample (ctDNA); Bone marrow = Bone marrow.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [Week1Clinical.json\*](../../out/Week1Clinical.json "open original schema") |

## Sample type Type

`string`

## Sample type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value           | Explanation |
| :-------------- | :---------- |
| `"Fresh"`       |             |
| `"FF"`          |             |
| `"FFPE"`        |             |
| `"Blood"`       |             |
| `"Plasma"`      |             |
| `"Bone marrow"` |             |
