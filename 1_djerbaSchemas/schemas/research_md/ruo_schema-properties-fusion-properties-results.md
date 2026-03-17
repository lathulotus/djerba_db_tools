# Untitled object in RUO - Report Structure Schema Schema

```txt
RUO.schema.json#/properties/fusion/propterties/results
```

Results pertaining to fusion data

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                             |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [ruo\_schema.json\*](../../../../../../cygwin64/home/wwwla/out/ruo_schema.json "open original schema") |

## results Type

`object` ([Details](ruo_schema-properties-fusion-propterties-results.md))

# results Properties

| Property                                                      | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                    |
| :------------------------------------------------------------ | :-------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Total variants](#total-variants)                             | `integer` | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-fusion-propterties-results-properties-total-variants.md "RUO.schema.json#/properties/fusion/propterties/results/properties/Total variants")                             |
| [Clinically relevant variants](#clinically-relevant-variants) | `integer` | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-fusion-propterties-results-properties-clinically-relevant-variants.md "RUO.schema.json#/properties/fusion/propterties/results/properties/Clinically relevant variants") |
| [nccn\_relevant\_variants](#nccn_relevant_variants)           | `integer` | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-fusion-propterties-results-properties-nccn_relevant_variants.md "RUO.schema.json#/properties/fusion/propterties/results/properties/nccn_relevant_variants")             |

## Total variants

Number of fusions identified

`Total variants`

* is optional

* Type: `integer`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-fusion-propterties-results-properties-total-variants.md "RUO.schema.json#/properties/fusion/propterties/results/properties/Total variants")

### Total variants Type

`integer`

## Clinically relevant variants

Number of relevant variants as per OncoKB

`Clinically relevant variants`

* is optional

* Type: `integer`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-fusion-propterties-results-properties-clinically-relevant-variants.md "RUO.schema.json#/properties/fusion/propterties/results/properties/Clinically relevant variants")

### Clinically relevant variants Type

`integer`

## nccn\_relevant\_variants

Number of relevant variants as per NCCN

`nccn_relevant_variants`

* is optional

* Type: `integer`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-fusion-propterties-results-properties-nccn_relevant_variants.md "RUO.schema.json#/properties/fusion/propterties/results/properties/nccn_relevant_variants")

### nccn\_relevant\_variants Type

`integer`
