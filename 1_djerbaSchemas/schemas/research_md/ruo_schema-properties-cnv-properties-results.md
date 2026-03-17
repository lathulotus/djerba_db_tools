# Untitled object in RUO - Report Structure Schema Schema

```txt
RUO.schema.json#/properties/cnv/propterties/results
```

Results pertaining to CNV data

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                             |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [ruo\_schema.json\*](../../../../../../cygwin64/home/wwwla/out/ruo_schema.json "open original schema") |

## results Type

`object` ([Details](ruo_schema-properties-cnv-propterties-results.md))

# results Properties

| Property                                          | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                  |
| :------------------------------------------------ | :-------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [percent genome altered](#percent-genome-altered) | `integer` | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-cnv-propterties-results-properties-percent-genome-altered.md "RUO.schema.json#/properties/cnv/propterties/results/properties/percent genome altered") |
| [total variants](#total-variants)                 | `integer` | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-cnv-propterties-results-properties-total-variants.md "RUO.schema.json#/properties/cnv/propterties/results/properties/total variants")                 |
| [body](#body)                                     | `object`  | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-cnv-propterties-results-properties-body.md "RUO.schema.json#/properties/cnv/propterties/results/properties/body")                                     |

## percent genome altered

Percent of genome altered by CNV

`percent genome altered`

* is optional

* Type: `integer`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-cnv-propterties-results-properties-percent-genome-altered.md "RUO.schema.json#/properties/cnv/propterties/results/properties/percent genome altered")

### percent genome altered Type

`integer`

## total variants

Number of total variants

`total variants`

* is optional

* Type: `integer`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-cnv-propterties-results-properties-total-variants.md "RUO.schema.json#/properties/cnv/propterties/results/properties/total variants")

### total variants Type

`integer`

## body

Details on each CNV

`body`

* is optional

* Type: `object` ([Details](ruo_schema-properties-cnv-propterties-results-properties-body.md))

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-cnv-propterties-results-properties-body.md "RUO.schema.json#/properties/cnv/propterties/results/properties/body")

### body Type

`object` ([Details](ruo_schema-properties-cnv-propterties-results-properties-body.md))
