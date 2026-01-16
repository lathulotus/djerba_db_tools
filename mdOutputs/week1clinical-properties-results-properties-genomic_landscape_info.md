# Untitled object in Clinical - Report Structure Schema Schema

```txt
Week1Clinical.schema.json#/properties/results/properties/genomic_landscape_info
```

Genomic landscape-- TMB, cohorts, percentiles

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [Week1Clinical.json\*](../../out/Week1Clinical.json "open original schema") |

## genomic\_landscape\_info Type

`object` ([Details](week1clinical-properties-results-properties-genomic_landscape_info.md))

# genomic\_landscape\_info Properties

| Property                                          | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                        |
| :------------------------------------------------ | :-------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Tumour Mutation Burden](#tumour-mutation-burden) | `integer` | Optional | cannot be null | [Clinical - Report Structure Schema](week1clinical-properties-results-properties-genomic_landscape_info-properties-tumour-mutation-burden.md "Week1Clinical.schema.json#/properties/results/properties/genomic_landscape_info/properties/Tumour Mutation Burden") |
| [TMB per megabase](#tmb-per-megabase)             | `integer` | Optional | cannot be null | [Clinical - Report Structure Schema](week1clinical-properties-results-properties-genomic_landscape_info-properties-tmb-per-megabase.md "Week1Clinical.schema.json#/properties/results/properties/genomic_landscape_info/properties/TMB per megabase")             |

## Tumour Mutation Burden

Tumour mutation burden value

`Tumour Mutation Burden`

* is optional

* Type: `integer`

* cannot be null

* defined in: [Clinical - Report Structure Schema](week1clinical-properties-results-properties-genomic_landscape_info-properties-tumour-mutation-burden.md "Week1Clinical.schema.json#/properties/results/properties/genomic_landscape_info/properties/Tumour Mutation Burden")

### Tumour Mutation Burden Type

`integer`

## TMB per megabase

Tumour mutation burden per megabase; relative

`TMB per megabase`

* is optional

* Type: `integer`

* cannot be null

* defined in: [Clinical - Report Structure Schema](week1clinical-properties-results-properties-genomic_landscape_info-properties-tmb-per-megabase.md "Week1Clinical.schema.json#/properties/results/properties/genomic_landscape_info/properties/TMB per megabase")

### TMB per megabase Type

`integer`
