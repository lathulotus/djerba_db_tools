# Untitled object in Clinical - Report Structure Schema Schema

```txt
Clinical.schema.json#/properties/wgts.cnv_purple/propterties/results
```

Results pertaining to CNV data

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                                     |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [clinical\_shema.json\*](../../../../../../cygwin64/home/wwwla/out/clinical_shema.json "open original schema") |

## results Type

`object` ([Details](clinical_shema-properties-wgtscnv_purple-propterties-results.md))

# results Properties

| Property                                          | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                       |
| :------------------------------------------------ | :-------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [percent genome altered](#percent-genome-altered) | `integer` | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-wgtscnv_purple-propterties-results-properties-percent-genome-altered.md "Clinical.schema.json#/properties/wgts.cnv_purple/propterties/results/properties/percent genome altered") |
| [total variants](#total-variants)                 | `integer` | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-wgtscnv_purple-propterties-results-properties-total-variants.md "Clinical.schema.json#/properties/wgts.cnv_purple/propterties/results/properties/total variants")                 |
| [body](#body)                                     | `object`  | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-wgtscnv_purple-propterties-results-properties-body.md "Clinical.schema.json#/properties/wgts.cnv_purple/propterties/results/properties/body")                                     |

## percent genome altered

Percent of genome altered by CNV

`percent genome altered`

* is optional

* Type: `integer`

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-wgtscnv_purple-propterties-results-properties-percent-genome-altered.md "Clinical.schema.json#/properties/wgts.cnv_purple/propterties/results/properties/percent genome altered")

### percent genome altered Type

`integer`

## total variants

Number of total variants

`total variants`

* is optional

* Type: `integer`

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-wgtscnv_purple-propterties-results-properties-total-variants.md "Clinical.schema.json#/properties/wgts.cnv_purple/propterties/results/properties/total variants")

### total variants Type

`integer`

## body

Details on each CNV

`body`

* is optional

* Type: `object` ([Details](clinical_shema-properties-wgtscnv_purple-propterties-results-properties-body.md))

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-wgtscnv_purple-propterties-results-properties-body.md "Clinical.schema.json#/properties/wgts.cnv_purple/propterties/results/properties/body")

### body Type

`object` ([Details](clinical_shema-properties-wgtscnv_purple-propterties-results-properties-body.md))
