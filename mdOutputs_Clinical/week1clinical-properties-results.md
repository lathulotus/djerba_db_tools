# Untitled object in Clinical - Report Structure Schema Schema

```txt
Week1Clinical.schema.json#/properties/results
```

Results from testing; assay in report ID

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [Week1Clinical.json\*](../../out/Week1Clinical.json "open original schema") |

## results Type

`object` ([Details](week1clinical-properties-results.md))

# results Properties

| Property                                                      | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                |
| :------------------------------------------------------------ | :------------ | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [genomic\_landscape\_info](#genomic_landscape_info)           | `object`      | Optional | cannot be null | [Clinical - Report Structure Schema](week1clinical-properties-results-properties-genomic_landscape_info.md "Week1Clinical.schema.json#/properties/results/properties/genomic_landscape_info")             |
| [genomic\_biomarkers](#genomic_biomarkers)                    | Not specified | Optional | cannot be null | [Clinical - Report Structure Schema](week1clinical-properties-results-properties-genomic_biomarkers.md "Week1Clinical.schema.json#/properties/results/properties/genomic_biomarkers")                     |
| [somatic mutations](#somatic-mutations)                       | `integer`     | Optional | cannot be null | [Clinical - Report Structure Schema](week1clinical-properties-results-properties-somatic-mutations.md "Week1Clinical.schema.json#/properties/results/properties/somatic mutations")                       |
| [coding sequence mutations](#coding-sequence-mutations)       | `integer`     | Optional | cannot be null | [Clinical - Report Structure Schema](week1clinical-properties-results-properties-coding-sequence-mutations.md "Week1Clinical.schema.json#/properties/results/properties/coding sequence mutations")       |
| [oncogenic mutations](#oncogenic-mutations)                   | `integer`     | Optional | cannot be null | [Clinical - Report Structure Schema](week1clinical-properties-results-properties-oncogenic-mutations.md "Week1Clinical.schema.json#/properties/results/properties/oncogenic mutations")                   |
| [Gene](#gene)                                                 | `string`      | Optional | cannot be null | [Clinical - Report Structure Schema](week1clinical-properties-results-properties-gene.md "Week1Clinical.schema.json#/properties/results/properties/Gene")                                                 |
| [protein](#protein)                                           | `string`      | Optional | cannot be null | [Clinical - Report Structure Schema](week1clinical-properties-results-properties-protein.md "Week1Clinical.schema.json#/properties/results/properties/protein")                                           |
| [type](#type)                                                 | `string`      | Optional | cannot be null | [Clinical - Report Structure Schema](week1clinical-properties-results-properties-type.md "Week1Clinical.schema.json#/properties/results/properties/type")                                                 |
| [vaf](#vaf)                                                   | `string`      | Optional | cannot be null | [Clinical - Report Structure Schema](week1clinical-properties-results-properties-vaf.md "Week1Clinical.schema.json#/properties/results/properties/vaf")                                                   |
| [depth](#depth)                                               | `string`      | Optional | cannot be null | [Clinical - Report Structure Schema](week1clinical-properties-results-properties-depth.md "Week1Clinical.schema.json#/properties/results/properties/depth")                                               |
| [LOH](#loh)                                                   | `boolean`     | Optional | cannot be null | [Clinical - Report Structure Schema](week1clinical-properties-results-properties-loh.md "Week1Clinical.schema.json#/properties/results/properties/LOH")                                                   |
| [Chromosome](#chromosome)                                     | `string`      | Optional | cannot be null | [Clinical - Report Structure Schema](week1clinical-properties-results-properties-chromosome.md "Week1Clinical.schema.json#/properties/results/properties/Chromosome")                                     |
| [OncoKB](#oncokb)                                             | `string`      | Optional | cannot be null | [Clinical - Report Structure Schema](week1clinical-properties-results-properties-oncokb.md "Week1Clinical.schema.json#/properties/results/properties/OncoKB")                                             |
| [percent genome altered](#percent-genome-altered)             | `integer`     | Optional | cannot be null | [Clinical - Report Structure Schema](week1clinical-properties-results-properties-percent-genome-altered.md "Week1Clinical.schema.json#/properties/results/properties/percent genome altered")             |
| [total variants](#total-variants)                             | `integer`     | Optional | cannot be null | [Clinical - Report Structure Schema](week1clinical-properties-results-properties-total-variants.md "Week1Clinical.schema.json#/properties/results/properties/total variants")                             |
| [clinically relevant variants](#clinically-relevant-variants) | `integer`     | Optional | cannot be null | [Clinical - Report Structure Schema](week1clinical-properties-results-properties-clinically-relevant-variants.md "Week1Clinical.schema.json#/properties/results/properties/clinically relevant variants") |
| [has expression data](#has-expression-data)                   | `boolean`     | Optional | cannot be null | [Clinical - Report Structure Schema](week1clinical-properties-results-properties-has-expression-data.md "Week1Clinical.schema.json#/properties/results/properties/has expression data")                   |
| [Expression Percentile](#expression-percentile)               | `integer`     | Optional | cannot be null | [Clinical - Report Structure Schema](week1clinical-properties-results-properties-expression-percentile.md "Week1Clinical.schema.json#/properties/results/properties/Expression Percentile")               |

## genomic\_landscape\_info

Genomic landscape-- TMB, cohorts, percentiles

`genomic_landscape_info`

* is optional

* Type: `object` ([Details](week1clinical-properties-results-properties-genomic_landscape_info.md))

* cannot be null

* defined in: [Clinical - Report Structure Schema](week1clinical-properties-results-properties-genomic_landscape_info.md "Week1Clinical.schema.json#/properties/results/properties/genomic_landscape_info")

### genomic\_landscape\_info Type

`object` ([Details](week1clinical-properties-results-properties-genomic_landscape_info.md))

## genomic\_biomarkers



`genomic_biomarkers`

* is optional

* Type: unknown

* cannot be null

* defined in: [Clinical - Report Structure Schema](week1clinical-properties-results-properties-genomic_biomarkers.md "Week1Clinical.schema.json#/properties/results/properties/genomic_biomarkers")

### genomic\_biomarkers Type

unknown

## somatic mutations

Number of somatic mutations identified

`somatic mutations`

* is optional

* Type: `integer`

* cannot be null

* defined in: [Clinical - Report Structure Schema](week1clinical-properties-results-properties-somatic-mutations.md "Week1Clinical.schema.json#/properties/results/properties/somatic mutations")

### somatic mutations Type

`integer`

## coding sequence mutations

Number of mutations in coding sequence

`coding sequence mutations`

* is optional

* Type: `integer`

* cannot be null

* defined in: [Clinical - Report Structure Schema](week1clinical-properties-results-properties-coding-sequence-mutations.md "Week1Clinical.schema.json#/properties/results/properties/coding sequence mutations")

### coding sequence mutations Type

`integer`

## oncogenic mutations

Number of oncogenic mutations identified

`oncogenic mutations`

* is optional

* Type: `integer`

* cannot be null

* defined in: [Clinical - Report Structure Schema](week1clinical-properties-results-properties-oncogenic-mutations.md "Week1Clinical.schema.json#/properties/results/properties/oncogenic mutations")

### oncogenic mutations Type

`integer`

## Gene

Gene containing identified variant

`Gene`

* is optional

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](week1clinical-properties-results-properties-gene.md "Week1Clinical.schema.json#/properties/results/properties/Gene")

### Gene Type

`string`

## protein

Protein alteration

`protein`

* is optional

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](week1clinical-properties-results-properties-protein.md "Week1Clinical.schema.json#/properties/results/properties/protein")

### protein Type

`string`

## type

Missense Mutation = Variant causing amino acid change; Nonsense Mutation = Variant causing premature stop codon; Frame Shift Del = Deletion causing frameshift; Frame Shift Ins = Insertion causing frameshift; Splice Site = Variant affecting canonical splice sites; Splice Region = Variant in splice region outside canonical sites.

`type`

* is optional

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](week1clinical-properties-results-properties-type.md "Week1Clinical.schema.json#/properties/results/properties/type")

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

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](week1clinical-properties-results-properties-vaf.md "Week1Clinical.schema.json#/properties/results/properties/vaf")

### vaf Type

`string`

## depth

Variant read depth

`depth`

* is optional

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](week1clinical-properties-results-properties-depth.md "Week1Clinical.schema.json#/properties/results/properties/depth")

### depth Type

`string`

## LOH

true = Loss of heterozygosity; false = No loss of heterozygosity.

`LOH`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [Clinical - Report Structure Schema](week1clinical-properties-results-properties-loh.md "Week1Clinical.schema.json#/properties/results/properties/LOH")

### LOH Type

`boolean`

### LOH Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value   | Explanation |
| :------ | :---------- |
| `true`  |             |
| `false` |             |

## Chromosome



`Chromosome`

* is optional

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](week1clinical-properties-results-properties-chromosome.md "Week1Clinical.schema.json#/properties/results/properties/Chromosome")

### Chromosome Type

`string`

## OncoKB

N1 = SoC evidence indicating lack of sensitivity/resistance; N2 = Clinical/biological evidence indicating lack of sensitivity/resistance.

`OncoKB`

* is optional

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](week1clinical-properties-results-properties-oncokb.md "Week1Clinical.schema.json#/properties/results/properties/OncoKB")

### OncoKB Type

`string`

### OncoKB Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value  | Explanation |
| :----- | :---------- |
| `"N1"` |             |
| `"N2"` |             |

## percent genome altered

Percentage of the genome altered by variant

`percent genome altered`

* is optional

* Type: `integer`

* cannot be null

* defined in: [Clinical - Report Structure Schema](week1clinical-properties-results-properties-percent-genome-altered.md "Week1Clinical.schema.json#/properties/results/properties/percent genome altered")

### percent genome altered Type

`integer`

## total variants

Total number of variants

`total variants`

* is optional

* Type: `integer`

* cannot be null

* defined in: [Clinical - Report Structure Schema](week1clinical-properties-results-properties-total-variants.md "Week1Clinical.schema.json#/properties/results/properties/total variants")

### total variants Type

`integer`

## clinically relevant variants

Number of clinically actionable/relevant variants

`clinically relevant variants`

* is optional

* Type: `integer`

* cannot be null

* defined in: [Clinical - Report Structure Schema](week1clinical-properties-results-properties-clinically-relevant-variants.md "Week1Clinical.schema.json#/properties/results/properties/clinically relevant variants")

### clinically relevant variants Type

`integer`

## has expression data

true = Has expression data; false = Does not have expression data.

`has expression data`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [Clinical - Report Structure Schema](week1clinical-properties-results-properties-has-expression-data.md "Week1Clinical.schema.json#/properties/results/properties/has expression data")

### has expression data Type

`boolean`

### has expression data Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value   | Explanation |
| :------ | :---------- |
| `true`  |             |
| `false` |             |

## Expression Percentile

Variant expression

`Expression Percentile`

* is optional

* Type: `integer`

* cannot be null

* defined in: [Clinical - Report Structure Schema](week1clinical-properties-results-properties-expression-percentile.md "Week1Clinical.schema.json#/properties/results/properties/Expression Percentile")

### Expression Percentile Type

`integer`
