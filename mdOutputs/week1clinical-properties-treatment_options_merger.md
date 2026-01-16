# Untitled object in Clinical - Report Structure Schema Schema

```txt
Week1Clinical.schema.json#/properties/treatment_options_merger
```

Treatment options merged; plugin

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [Week1Clinical.json\*](../../out/Week1Clinical.json "open original schema") |

## treatment\_options\_merger Type

`object` ([Details](week1clinical-properties-treatment_options_merger.md))

# treatment\_options\_merger Properties

| Property                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                  |
| :---------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Tier](#tier)                 | `string` | Optional | cannot be null | [Clinical - Report Structure Schema](week1clinical-properties-treatment_options_merger-properties-tier.md "Week1Clinical.schema.json#/properties/treatment_options_merger/properties/Tier")                 |
| [OncoKB level](#oncokb-level) | `string` | Optional | cannot be null | [Clinical - Report Structure Schema](week1clinical-properties-treatment_options_merger-properties-oncokb-level.md "Week1Clinical.schema.json#/properties/treatment_options_merger/properties/OncoKB level") |
| [Treatments](#treatments)     | `string` | Optional | cannot be null | [Clinical - Report Structure Schema](week1clinical-properties-treatment_options_merger-properties-treatments.md "Week1Clinical.schema.json#/properties/treatment_options_merger/properties/Treatments")     |

## Tier

Approved = Therapy approved for clinical use; Investigational = Therapy under clinical investigation.

`Tier`

* is optional

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](week1clinical-properties-treatment_options_merger-properties-tier.md "Week1Clinical.schema.json#/properties/treatment_options_merger/properties/Tier")

### Tier Type

`string`

### Tier Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value               | Explanation |
| :------------------ | :---------- |
| `"Approved"`        |             |
| `"Investigational"` |             |

## OncoKB level

Level 1 = FDA-recognized biomarker predictive of response; Level 2 = Standard-of-care biomarker predictive of response; Level 3A = Clinical evidence supporting response in this indication; Level 3B = Clinical evidence supporting response in another indication; Level 4 = Biological evidence supporting response.

`OncoKB level`

* is optional

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](week1clinical-properties-treatment_options_merger-properties-oncokb-level.md "Week1Clinical.schema.json#/properties/treatment_options_merger/properties/OncoKB level")

### OncoKB level Type

`string`

### OncoKB level Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value        | Explanation |
| :----------- | :---------- |
| `"Level 1"`  |             |
| `"Level 2"`  |             |
| `"Level 3A"` |             |
| `"Level 3B"` |             |
| `"Level 4"`  |             |

## Treatments

Potential therapies and treatments for biological events

`Treatments`

* is optional

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](week1clinical-properties-treatment_options_merger-properties-treatments.md "Week1Clinical.schema.json#/properties/treatment_options_merger/properties/Treatments")

### Treatments Type

`string`
