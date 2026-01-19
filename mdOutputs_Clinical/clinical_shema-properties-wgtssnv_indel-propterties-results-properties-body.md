# Untitled object in Clinical - Report Structure Schema Schema

```txt
Clinical.schema.json#/properties/wgts.snv_indel/propterties/results/properties/body
```

Details on each SNV

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                                     |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [clinical\_shema.json\*](../../../../../../cygwin64/home/wwwla/out/clinical_shema.json "open original schema") |

## body Type

`object` ([Details](clinical_shema-properties-wgtssnv_indel-propterties-results-properties-body.md))

# body Properties

| Property                  | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                             |
| :------------------------ | :-------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Gene](#gene)             | `string`  | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-wgtssnv_indel-propterties-results-properties-body-properties-gene.md "Clinical.schema.json#/properties/wgts.snv_indel/propterties/results/properties/body/properties/Gene")             |
| [protein](#protein)       | `string`  | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-wgtssnv_indel-propterties-results-properties-body-properties-protein.md "Clinical.schema.json#/properties/wgts.snv_indel/propterties/results/properties/body/properties/protein")       |
| [type](#type)             | `string`  | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-wgtssnv_indel-propterties-results-properties-body-properties-type.md "Clinical.schema.json#/properties/wgts.snv_indel/propterties/results/properties/body/properties/type")             |
| [vaf](#vaf)               | `integer` | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-wgtssnv_indel-propterties-results-properties-body-properties-vaf.md "Clinical.schema.json#/properties/wgts.snv_indel/propterties/results/properties/body/properties/vaf")               |
| [depth](#depth)           | `array`   | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-wgtssnv_indel-propterties-results-properties-body-properties-depth.md "Clinical.schema.json#/properties/wgts.snv_indel/propterties/results/properties/body/properties/depth")           |
| [LOH](#loh)               | `array`   | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-wgtssnv_indel-propterties-results-properties-body-properties-loh.md "Clinical.schema.json#/properties/wgts.snv_indel/propterties/results/properties/body/properties/LOH")               |
| [Chromosome](#chromosome) | `string`  | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-wgtssnv_indel-propterties-results-properties-body-properties-chromosome.md "Clinical.schema.json#/properties/wgts.snv_indel/propterties/results/properties/body/properties/Chromosome") |
| [OncoKB](#oncokb)         | `string`  | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-wgtssnv_indel-propterties-results-properties-body-properties-oncokb.md "Clinical.schema.json#/properties/wgts.snv_indel/propterties/results/properties/body/properties/OncoKB")         |

## Gene

Names of SNV-containing genes

`Gene`

* is optional

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-wgtssnv_indel-propterties-results-properties-body-properties-gene.md "Clinical.schema.json#/properties/wgts.snv_indel/propterties/results/properties/body/properties/Gene")

### Gene Type

`string`

## protein

Protein alteration

`protein`

* is optional

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-wgtssnv_indel-propterties-results-properties-body-properties-protein.md "Clinical.schema.json#/properties/wgts.snv_indel/propterties/results/properties/body/properties/protein")

### protein Type

`string`

## type

Type of SNV event

`type`

* is optional

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-wgtssnv_indel-propterties-results-properties-body-properties-type.md "Clinical.schema.json#/properties/wgts.snv_indel/propterties/results/properties/body/properties/type")

### type Type

`string`

### type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                 | Explanation |
| :-------------------- | :---------- |
| `"Missense Mutation"` |Variant causing amino acid change|
| `"Nonsense Mutation"` |Variant causing premature stop codon|
| `"Frame Shift Del"`   |Deletion causing frameshift|
| `"Frame Shift Ins"`   |Insertion causing frameshift|
| `"Splice Site"`       |Variant affecting canonical splice sites|
| `"Splice Region"`     |Variant in splice region outside canonical sites|

## vaf

Variant allele frequency (percentage)

`vaf`

* is optional

* Type: `integer`

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-wgtssnv_indel-propterties-results-properties-body-properties-vaf.md "Clinical.schema.json#/properties/wgts.snv_indel/propterties/results/properties/body/properties/vaf")

### vaf Type

`integer`

## depth

Variant read depth

`depth`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-wgtssnv_indel-propterties-results-properties-body-properties-depth.md "Clinical.schema.json#/properties/wgts.snv_indel/propterties/results/properties/body/properties/depth")

### depth Type

`string[]`

## LOH

Whether loss of heterozygosity is exhibited

`LOH`

* is optional

* Type: `boolean[]`

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-wgtssnv_indel-propterties-results-properties-body-properties-loh.md "Clinical.schema.json#/properties/wgts.snv_indel/propterties/results/properties/body/properties/LOH")

### LOH Type

`boolean[]`

## Chromosome

Position of SNV/indel

`Chromosome`

* is optional

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-wgtssnv_indel-propterties-results-properties-body-properties-chromosome.md "Clinical.schema.json#/properties/wgts.snv_indel/propterties/results/properties/body/properties/Chromosome")

### Chromosome Type

`string`

## OncoKB

OncoKB level of evidence

`OncoKB`

* is optional

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-wgtssnv_indel-propterties-results-properties-body-properties-oncokb.md "Clinical.schema.json#/properties/wgts.snv_indel/propterties/results/properties/body/properties/OncoKB")

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
