# Untitled object in Clinical - Report Structure Schema Schema

```txt
Week1Clinical.schema.json#/properties/sample
```

Sample information

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [Week1Clinical.json\*](../../out/Week1Clinical.json "open original schema") |

## sample Type

`object` ([Details](week1clinical-properties-sample.md))

# sample Properties

| Property                                                             | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                     |
| :------------------------------------------------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Sample type](#sample-type)                                          | `string`  | Optional | cannot be null | [Clinical - Report Structure Schema](week1clinical-properties-sample-properties-sample-type.md "Week1Clinical.schema.json#/properties/sample/properties/Sample type")                                          |
| [Estimated Cancer Cell Content (%)](#estimated-cancer-cell-content-) | `integer` | Optional | cannot be null | [Clinical - Report Structure Schema](week1clinical-properties-sample-properties-estimated-cancer-cell-content-.md "Week1Clinical.schema.json#/properties/sample/properties/Estimated Cancer Cell Content (%)") |
| [Estimated Ploidy](#estimated-ploidy)                                | `string`  | Optional | cannot be null | [Clinical - Report Structure Schema](week1clinical-properties-sample-properties-estimated-ploidy.md "Week1Clinical.schema.json#/properties/sample/properties/Estimated Ploidy")                                |
| [Callability (%)](#callability-)                                     | `string`  | Optional | cannot be null | [Clinical - Report Structure Schema](week1clinical-properties-sample-properties-callability-.md "Week1Clinical.schema.json#/properties/sample/properties/Callability (%)")                                     |

## Sample type

Fresh = Fresh unfrozen; FF = Fresh frozen; FFPE = Formalin-fixed, paraffin-embedded; Blood = Whole blood; Plasma = Plasma sample (ctDNA); Bone marrow = Bone marrow.

`Sample type`

* is optional

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](week1clinical-properties-sample-properties-sample-type.md "Week1Clinical.schema.json#/properties/sample/properties/Sample type")

### Sample type Type

`string`

### Sample type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value           | Explanation |
| :-------------- | :---------- |
| `"Fresh"`       |             |
| `"FF"`          |             |
| `"FFPE"`        |             |
| `"Blood"`       |             |
| `"Plasma"`      |             |
| `"Bone marrow"` |             |

## Estimated Cancer Cell Content (%)

Estimated percentage of cancer cell content

`Estimated Cancer Cell Content (%)`

* is optional

* Type: `integer`

* cannot be null

* defined in: [Clinical - Report Structure Schema](week1clinical-properties-sample-properties-estimated-cancer-cell-content-.md "Week1Clinical.schema.json#/properties/sample/properties/Estimated Cancer Cell Content (%)")

### Estimated Cancer Cell Content (%) Type

`integer`

## Estimated Ploidy

Estimated ploidy

`Estimated Ploidy`

* is optional

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](week1clinical-properties-sample-properties-estimated-ploidy.md "Week1Clinical.schema.json#/properties/sample/properties/Estimated Ploidy")

### Estimated Ploidy Type

`string`

## Callability (%)

Read call percentage

`Callability (%)`

* is optional

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](week1clinical-properties-sample-properties-callability-.md "Week1Clinical.schema.json#/properties/sample/properties/Callability (%)")

### Callability (%) Type

`string`
