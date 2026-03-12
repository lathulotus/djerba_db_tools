# Untitled object in RUO - Report Structure Schema Schema

```txt
RUO.schema.json#/properties/wgts.snv_indel/propterties/results
```

Results pertaining to SNV/indel data

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                             |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [ruo\_schema.json\*](../../../../../../cygwin64/home/wwwla/out/ruo_schema.json "open original schema") |

## results Type

`object` ([Details](ruo_schema-properties-wgtssnv_indel-propterties-results.md))

# results Properties

| Property                                                | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                             |
| :------------------------------------------------------ | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [somatic mutations](#somatic-mutations)                 | `integer` | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-wgtssnv_indel-propterties-results-properties-somatic-mutations.md "RUO.schema.json#/properties/wgts.snv_indel/propterties/results/properties/somatic mutations")                 |
| [coding sequence mutations](#coding-sequence-mutations) | `integer` | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-wgtssnv_indel-propterties-results-properties-coding-sequence-mutations.md "RUO.schema.json#/properties/wgts.snv_indel/propterties/results/properties/coding sequence mutations") |
| [oncogenic mutations](#oncogenic-mutations)             | `integer` | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-wgtssnv_indel-propterties-results-properties-oncogenic-mutations.md "RUO.schema.json#/properties/wgts.snv_indel/propterties/results/properties/oncogenic mutations")             |
| [body](#body)                                           | `object`  | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-wgtssnv_indel-propterties-results-properties-body.md "RUO.schema.json#/properties/wgts.snv_indel/propterties/results/properties/body")                                           |

## somatic mutations

Number of somatic mutations identified

`somatic mutations`

* is optional

* Type: `integer`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-wgtssnv_indel-propterties-results-properties-somatic-mutations.md "RUO.schema.json#/properties/wgts.snv_indel/propterties/results/properties/somatic mutations")

### somatic mutations Type

`integer`

## coding sequence mutations

Number of mutations in coding sequence

`coding sequence mutations`

* is optional

* Type: `integer`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-wgtssnv_indel-propterties-results-properties-coding-sequence-mutations.md "RUO.schema.json#/properties/wgts.snv_indel/propterties/results/properties/coding sequence mutations")

### coding sequence mutations Type

`integer`

## oncogenic mutations

Number of oncogenic mutations identified

`oncogenic mutations`

* is optional

* Type: `integer`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-wgtssnv_indel-propterties-results-properties-oncogenic-mutations.md "RUO.schema.json#/properties/wgts.snv_indel/propterties/results/properties/oncogenic mutations")

### oncogenic mutations Type

`integer`

## body

Details on each SNV

`body`

* is optional

* Type: `object` ([Details](ruo_schema-properties-wgtssnv_indel-propterties-results-properties-body.md))

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-wgtssnv_indel-propterties-results-properties-body.md "RUO.schema.json#/properties/wgts.snv_indel/propterties/results/properties/body")

### body Type

`object` ([Details](ruo_schema-properties-wgtssnv_indel-propterties-results-properties-body.md))
