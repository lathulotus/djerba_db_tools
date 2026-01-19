# Untitled string in Clinical - Report Structure Schema Schema

```txt
Clinical.schema.json#/properties/case_overview/properties/results/properties/site_of_biopsy
```

Biopsy type/location (cfDNA)

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                                     |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [clinical\_shema.json\*](../../../../../../cygwin64/home/wwwla/out/clinical_shema.json "open original schema") |

## site\_of\_biopsy Type

`string`

## site\_of\_biopsy Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                          | Explanation |
| :----------------------------- | :---------- |
| `"cfDNA"`                      |             |
| `"Liver"`                      |             |
| `"Bone Marrow"`                |             |
| `"Left 4th Rib - Soft Tissue"` |             |
| `"Left Breast"`                |             |
| `"Perihepatic"`                |             |
