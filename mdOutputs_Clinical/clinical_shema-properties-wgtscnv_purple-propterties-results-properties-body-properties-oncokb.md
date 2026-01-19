# Untitled string in Clinical - Report Structure Schema Schema

```txt
Clinical.schema.json#/properties/wgts.cnv_purple/propterties/results/properties/body/properties/OncoKB
```

OncoKB level of evidence

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                                     |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [clinical\_shema.json\*](../../../../../../cygwin64/home/wwwla/out/clinical_shema.json "open original schema") |

## OncoKB Type

`string`

## OncoKB Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value  | Explanation |
| :----- | :---------- |
| `"1"`  |FDA-recognized biomarker predictive of response to an FDA-approved drug in this indication|
| `"2"`  |Standard care biomarker recommended by the NCCN or other expert panels predictive of response to an FDA-approved drug in this indication|
| `"3A"` |Compelling clinical evidence supports the biomarker as being predictive of response to a drug in this indication|
| `"3B"` |Standard care or investigational biomarker predictive of response to an FDA-approved or investigational drug in another indication|
| `"4"`  |Compelling biological evidence supports the biomarker as being predictive of response to a drug|
| `"N1"` |The biomarker is listed as "Oncogenic" by OncoKB, but is not in an actionable tier|
| `"N2"` |The biomarker is listed as "Likely Oncogenic" by OncoKB, but is not in an actionable tier|
| `"N3"` |The biomarker is listed as "Predicted Oncogenic" by OncoKB, but is not in an actionable tier|
| `"N4"` |The biomarker is listed as "Likely Neutral" or "Inconclusive" by OncoKB|
