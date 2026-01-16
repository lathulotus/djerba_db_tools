# Untitled object in RUO - Report Structure Schema Schema

```txt
RUO.schema.json#/properties/results
```

Results from testing; merged

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                             |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [ruo\_schema.json\*](../../../../../../cygwin64/home/wwwla/out/ruo_schema.json "open original schema") |

## results Type

`object` ([Details](ruo_schema-properties-results.md))

# results Properties

| Property                                                      | Type      | Required | Nullable       | Defined by                                                                                                                                                                              |
| :------------------------------------------------------------ | :-------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [assay](#assay)                                               | `string`  | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-results-properties-assay.md "RUO.schema.json#/properties/results/properties/assay")                                               |
| [primary\_cancer](#primary_cancer)                            | `string`  | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-results-properties-primary_cancer.md "RUO.schema.json#/properties/results/properties/primary_cancer")                             |
| [site\_of\_biopsy](#site_of_biopsy)                           | `string`  | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-results-properties-site_of_biopsy.md "RUO.schema.json#/properties/results/properties/site_of_biopsy")                             |
| [study](#study)                                               | `string`  | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-results-properties-study.md "RUO.schema.json#/properties/results/properties/study")                                               |
| [project](#project)                                           | `string`  | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-results-properties-project.md "RUO.schema.json#/properties/results/properties/project")                                           |
| [known\_variants](#known_variants)                            | `string`  | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-results-properties-known_variants.md "RUO.schema.json#/properties/results/properties/known_variants")                             |
| [cancer\_content](#cancer_content)                            | `integer` | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-results-properties-cancer_content.md "RUO.schema.json#/properties/results/properties/cancer_content")                             |
| [raw\_coverage](#raw_coverage)                                | `integer` | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-results-properties-raw_coverage.md "RUO.schema.json#/properties/results/properties/raw_coverage")                                 |
| [unique\_coverage](#unique_coverage)                          | `integer` | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-results-properties-unique_coverage.md "RUO.schema.json#/properties/results/properties/unique_coverage")                           |
| [Clinically relevant variants](#clinically-relevant-variants) | `integer` | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-results-properties-clinically-relevant-variants.md "RUO.schema.json#/properties/results/properties/Clinically relevant variants") |
| [Total variants](#total-variants)                             | `integer` | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-results-properties-total-variants.md "RUO.schema.json#/properties/results/properties/Total variants")                             |
| [Has expression data](#has-expression-data)                   | `boolean` | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-results-properties-has-expression-data.md "RUO.schema.json#/properties/results/properties/Has expression data")                   |
| [somatic mutations](#somatic-mutations)                       | `integer` | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-results-properties-somatic-mutations.md "RUO.schema.json#/properties/results/properties/somatic mutations")                       |
| [coding sequence mutations](#coding-sequence-mutations)       | `integer` | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-results-properties-coding-sequence-mutations.md "RUO.schema.json#/properties/results/properties/coding sequence mutations")       |
| [oncogenic mutations](#oncogenic-mutations)                   | `integer` | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-results-properties-oncogenic-mutations.md "RUO.schema.json#/properties/results/properties/oncogenic mutations")                   |
| [Gene](#gene)                                                 | `array`   | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-results-properties-gene.md "RUO.schema.json#/properties/results/properties/Gene")                                                 |
| [protein](#protein)                                           | `array`   | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-results-properties-protein.md "RUO.schema.json#/properties/results/properties/protein")                                           |
| [type](#type)                                                 | `string`  | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-results-properties-type.md "RUO.schema.json#/properties/results/properties/type")                                                 |
| [vaf](#vaf)                                                   | `array`   | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-results-properties-vaf.md "RUO.schema.json#/properties/results/properties/vaf")                                                   |
| [depth](#depth)                                               | `array`   | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-results-properties-depth.md "RUO.schema.json#/properties/results/properties/depth")                                               |
| [LOH](#loh)                                                   | `array`   | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-results-properties-loh.md "RUO.schema.json#/properties/results/properties/LOH")                                                   |
| [Chromosome](#chromosome)                                     | `array`   | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-results-properties-chromosome.md "RUO.schema.json#/properties/results/properties/Chromosome")                                     |

## assay

Type of assay used for sequencing (WGTS, WGS, TAR)

`assay`

* is optional

* Type: `string`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-results-properties-assay.md "RUO.schema.json#/properties/results/properties/assay")

### assay Type

`string`

### assay Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value    | Explanation |
| :------- | :---------- |
| `"WGTS"` |             |
| `"WGS"`  |             |
| `"TAR"`  |             |

## primary\_cancer

Cancer type.

`primary_cancer`

* is optional

* Type: `string`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-results-properties-primary_cancer.md "RUO.schema.json#/properties/results/properties/primary_cancer")

### primary\_cancer Type

`string`

### primary\_cancer Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                         | Explanation |
| :---------------------------- | :---------- |
| `"Pancreatic adenocarcinoma"` |             |
| `"Hepatobiliary Tumour"`      |             |
| `"Multiple Myeloma"`          |             |
| `"Breast Cancer"`             |             |
| `"Invasive breast carcinoma"` |             |

## site\_of\_biopsy

Biopsy type/location (cfDNA)

`site_of_biopsy`

* is optional

* Type: `string`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-results-properties-site_of_biopsy.md "RUO.schema.json#/properties/results/properties/site_of_biopsy")

### site\_of\_biopsy Type

`string`

## study

Research study name

`study`

* is optional

* Type: `string`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-results-properties-study.md "RUO.schema.json#/properties/results/properties/study")

### study Type

`string`

## project

Specific project name

`project`

* is optional

* Type: `string`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-results-properties-project.md "RUO.schema.json#/properties/results/properties/project")

### project Type

`string`

## known\_variants

Previously known variants (<em>GENE</em> c.notation (p.notation)

`known_variants`

* is optional

* Type: `string`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-results-properties-known_variants.md "RUO.schema.json#/properties/results/properties/known_variants")

### known\_variants Type

`string`

## cancer\_content

Amount of cancer cells

`cancer_content`

* is optional

* Type: `integer`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-results-properties-cancer_content.md "RUO.schema.json#/properties/results/properties/cancer_content")

### cancer\_content Type

`integer`

## raw\_coverage

Sequences read coverage

`raw_coverage`

* is optional

* Type: `integer`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-results-properties-raw_coverage.md "RUO.schema.json#/properties/results/properties/raw_coverage")

### raw\_coverage Type

`integer`

## unique\_coverage

Unique read coverage

`unique_coverage`

* is optional

* Type: `integer`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-results-properties-unique_coverage.md "RUO.schema.json#/properties/results/properties/unique_coverage")

### unique\_coverage Type

`integer`

## Clinically relevant variants

Number of clinically relevant variants

`Clinically relevant variants`

* is optional

* Type: `integer`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-results-properties-clinically-relevant-variants.md "RUO.schema.json#/properties/results/properties/Clinically relevant variants")

### Clinically relevant variants Type

`integer`

## Total variants

Number of total variants identified

`Total variants`

* is optional

* Type: `integer`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-results-properties-total-variants.md "RUO.schema.json#/properties/results/properties/Total variants")

### Total variants Type

`integer`

## Has expression data

Whether variant is expressed

`Has expression data`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-results-properties-has-expression-data.md "RUO.schema.json#/properties/results/properties/Has expression data")

### Has expression data Type

`boolean`

## somatic mutations

Number of somatic mutations identified

`somatic mutations`

* is optional

* Type: `integer`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-results-properties-somatic-mutations.md "RUO.schema.json#/properties/results/properties/somatic mutations")

### somatic mutations Type

`integer`

## coding sequence mutations

Number of mutations in coding sequence

`coding sequence mutations`

* is optional

* Type: `integer`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-results-properties-coding-sequence-mutations.md "RUO.schema.json#/properties/results/properties/coding sequence mutations")

### coding sequence mutations Type

`integer`

## oncogenic mutations

Number of oncogenic mutations identified

`oncogenic mutations`

* is optional

* Type: `integer`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-results-properties-oncogenic-mutations.md "RUO.schema.json#/properties/results/properties/oncogenic mutations")

### oncogenic mutations Type

`integer`

## Gene

Gene containing identified variant

`Gene`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-results-properties-gene.md "RUO.schema.json#/properties/results/properties/Gene")

### Gene Type

`string[]`

## protein

Protein alteration

`protein`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-results-properties-protein.md "RUO.schema.json#/properties/results/properties/protein")

### protein Type

`string[]`

## type

Type of specific alteration or biological event (Missense Mutation, Nonsense Mutation, Frame Shift Del, Frame Shift Ins, Splice Site, Splice Region)

`type`

* is optional

* Type: `string`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-results-properties-type.md "RUO.schema.json#/properties/results/properties/type")

### type Type

`string`

### type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                 | Explanation |
| :-------------------- | :---------- |
| `"Missense Mutation"` |             |
| `"Nonsense Mutation"` |             |
| `"Frame Shift Del"`   |             |
| `"Frame Shift Ins"`   |             |
| `"Splice Site"`       |             |
| `"Splice Region"`     |             |

## vaf

Variant allele frequency

`vaf`

* is optional

* Type: `integer[]`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-results-properties-vaf.md "RUO.schema.json#/properties/results/properties/vaf")

### vaf Type

`integer[]`

## depth

Variant read depth

`depth`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-results-properties-depth.md "RUO.schema.json#/properties/results/properties/depth")

### depth Type

`string[]`

## LOH

Whether loss of heterozygosity is exhibited

`LOH`

* is optional

* Type: `boolean[]`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-results-properties-loh.md "RUO.schema.json#/properties/results/properties/LOH")

### LOH Type

`boolean[]`

## Chromosome



`Chromosome`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-results-properties-chromosome.md "RUO.schema.json#/properties/results/properties/Chromosome")

### Chromosome Type

`string[]`
