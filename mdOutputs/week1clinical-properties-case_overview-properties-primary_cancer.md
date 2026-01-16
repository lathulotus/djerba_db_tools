# Untitled string in Clinical - Report Structure Schema Schema

```txt
Week1Clinical.schema.json#/properties/case_overview/properties/primary_cancer
```

Pancreatic adenocarcinoma = Pancreatic; Hepatobiliary Tumour = Hepatobiliary; Multiple Myeloma = Blood; Breast Cancer = Breast; Invasive breast carcinoma = Breast.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [Week1Clinical.json\*](../../out/Week1Clinical.json "open original schema") |

## primary\_cancer Type

`string`

## primary\_cancer Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                         | Explanation |
| :---------------------------- | :---------- |
| `"Pancreatic adenocarcinoma"` |             |
| `"Hepatobiliary Tumour"`      |             |
| `"Multiple Myeloma"`          |             |
| `"Breast Cancer"`             |             |
| `"Invasive breast carcinoma"` |             |
