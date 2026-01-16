# Untitled string in Clinical - Report Structure Schema Schema

```txt
Week1Clinical.schema.json#/properties/treatment_options_merger/properties/OncoKB level
```

Level 1 = FDA-recognized biomarker predictive of response; Level 2 = Standard-of-care biomarker predictive of response; Level 3A = Clinical evidence supporting response in this indication; Level 3B = Clinical evidence supporting response in another indication; Level 4 = Biological evidence supporting response.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [Week1Clinical.json\*](../../out/Week1Clinical.json "open original schema") |

## OncoKB level Type

`string`

## OncoKB level Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value        | Explanation |
| :----------- | :---------- |
| `"Level 1"`  |             |
| `"Level 2"`  |             |
| `"Level 3A"` |             |
| `"Level 3B"` |             |
| `"Level 4"`  |             |
