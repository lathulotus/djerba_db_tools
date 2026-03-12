# Untitled object in RUO - Report Structure Schema Schema

```txt
RUO.schema.json#/properties/wgts.snv_indel/propterties/results/properties/body
```

Details on each SNV

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                             |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [ruo\_schema.json\*](../../../../../../cygwin64/home/wwwla/out/ruo_schema.json "open original schema") |

## body Type

`object` ([Details](ruo_schema-properties-wgtssnv_indel-propterties-results-properties-body.md))

# body Properties

| Property                  | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                               |
| :------------------------ | :-------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Gene](#gene)             | `string`  | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-wgtssnv_indel-propterties-results-properties-body-properties-gene.md "RUO.schema.json#/properties/wgts.snv_indel/propterties/results/properties/body/properties/Gene")             |
| [protein](#protein)       | `string`  | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-wgtssnv_indel-propterties-results-properties-body-properties-protein.md "RUO.schema.json#/properties/wgts.snv_indel/propterties/results/properties/body/properties/protein")       |
| [type](#type)             | `string`  | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-wgtssnv_indel-propterties-results-properties-body-properties-type.md "RUO.schema.json#/properties/wgts.snv_indel/propterties/results/properties/body/properties/type")             |
| [vaf](#vaf)               | `integer` | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-wgtssnv_indel-propterties-results-properties-body-properties-vaf.md "RUO.schema.json#/properties/wgts.snv_indel/propterties/results/properties/body/properties/vaf")               |
| [Chromosome](#chromosome) | `string`  | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-wgtssnv_indel-propterties-results-properties-body-properties-chromosome.md "RUO.schema.json#/properties/wgts.snv_indel/propterties/results/properties/body/properties/Chromosome") |
| [OncoKB](#oncokb)         | `string`  | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-wgtssnv_indel-propterties-results-properties-body-properties-oncokb.md "RUO.schema.json#/properties/wgts.snv_indel/propterties/results/properties/body/properties/OncoKB")         |

## Gene

Names of SNV-containing genes

`Gene`

* is optional

* Type: `string`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-wgtssnv_indel-propterties-results-properties-body-properties-gene.md "RUO.schema.json#/properties/wgts.snv_indel/propterties/results/properties/body/properties/Gene")

### Gene Type

`string`

## protein

Protein alteration

`protein`

* is optional

* Type: `string`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-wgtssnv_indel-propterties-results-properties-body-properties-protein.md "RUO.schema.json#/properties/wgts.snv_indel/propterties/results/properties/body/properties/protein")

### protein Type

`string`

## type

Type of SNV event

`type`

* is optional

* Type: `string`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-wgtssnv_indel-propterties-results-properties-body-properties-type.md "RUO.schema.json#/properties/wgts.snv_indel/propterties/results/properties/body/properties/type")

### type Type

`string`

### type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value               | Explanation |
| :------------------ | :---------- |
| `"Frame Shift Ins"` |             |
| `"Frame Shift Del"` |             |

## vaf

Variant allele frequency (percentage)

`vaf`

* is optional

* Type: `integer`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-wgtssnv_indel-propterties-results-properties-body-properties-vaf.md "RUO.schema.json#/properties/wgts.snv_indel/propterties/results/properties/body/properties/vaf")

### vaf Type

`integer`

## Chromosome

Position of SNV/indel

`Chromosome`

* is optional

* Type: `string`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-wgtssnv_indel-propterties-results-properties-body-properties-chromosome.md "RUO.schema.json#/properties/wgts.snv_indel/propterties/results/properties/body/properties/Chromosome")

### Chromosome Type

`string`

## OncoKB

OncoKB level of evidence

`OncoKB`

* is optional

* Type: `string`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-wgtssnv_indel-propterties-results-properties-body-properties-oncokb.md "RUO.schema.json#/properties/wgts.snv_indel/propterties/results/properties/body/properties/OncoKB")

### OncoKB Type

`string`

### OncoKB Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value  | Explanation |
| :----- | :---------- |
| `"1"`  |             |
| `"2"`  |             |
| `"3"`  |             |
| `"4"`  |             |
| `"N1"` |             |
| `"N2"` |             |
