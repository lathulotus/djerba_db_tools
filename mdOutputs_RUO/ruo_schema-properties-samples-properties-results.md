# Untitled object in RUO - Report Structure Schema Schema

```txt
RUO.schema.json#/properties/samples/properties/results
```

Results covering sample details

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                             |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [ruo\_schema.json\*](../../../../../../cygwin64/home/wwwla/out/ruo_schema.json "open original schema") |

## results Type

`object` ([Details](ruo_schema-properties-samples-properties-results.md))

# results Properties

| Property                                                             | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                           |
| :------------------------------------------------------------------- | :-------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Sample Type](#sample-type)                                          | `string`  | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-samples-properties-results-properties-sample-type.md "RUO.schema.json#/properties/samples/properties/results/properties/Sample Type")                                          |
| [Estimated Cancer Cell Content (%)](#estimated-cancer-cell-content-) | `integer` | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-samples-properties-results-properties-estimated-cancer-cell-content-.md "RUO.schema.json#/properties/samples/properties/results/properties/Estimated Cancer Cell Content (%)") |
| [Estimated Ploidy](#estimated-ploidy)                                | `string`  | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-samples-properties-results-properties-estimated-ploidy.md "RUO.schema.json#/properties/samples/properties/results/properties/Estimated Ploidy")                                |
| [Callability (%)](#callability-)                                     | `string`  | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-samples-properties-results-properties-callability-.md "RUO.schema.json#/properties/samples/properties/results/properties/Callability (%)")                                     |
| [Coverage (mean)](#coverage-mean)                                    | `string`  | Optional | cannot be null | [RUO - Report Structure Schema](ruo_schema-properties-samples-properties-results-properties-coverage-mean.md "RUO.schema.json#/properties/samples/properties/results/properties/Coverage (mean)")                                    |

## Sample Type

Type of sample

`Sample Type`

* is optional

* Type: `string`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-samples-properties-results-properties-sample-type.md "RUO.schema.json#/properties/samples/properties/results/properties/Sample Type")

### Sample Type Type

`string`

### Sample Type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                         | Explanation |
| :---------------------------- | :---------- |
| `"Fresh frozen tissue block"` |             |
| `"FFPE"`                      |             |

## Estimated Cancer Cell Content (%)

Estimated percentage of cancer cell content

`Estimated Cancer Cell Content (%)`

* is optional

* Type: `integer`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-samples-properties-results-properties-estimated-cancer-cell-content-.md "RUO.schema.json#/properties/samples/properties/results/properties/Estimated Cancer Cell Content (%)")

### Estimated Cancer Cell Content (%) Type

`integer`

## Estimated Ploidy

Estimated ploidy value

`Estimated Ploidy`

* is optional

* Type: `string`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-samples-properties-results-properties-estimated-ploidy.md "RUO.schema.json#/properties/samples/properties/results/properties/Estimated Ploidy")

### Estimated Ploidy Type

`string`

## Callability (%)

Call quality

`Callability (%)`

* is optional

* Type: `string`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-samples-properties-results-properties-callability-.md "RUO.schema.json#/properties/samples/properties/results/properties/Callability (%)")

### Callability (%) Type

`string`

## Coverage (mean)

Average coverage

`Coverage (mean)`

* is optional

* Type: `string`

* cannot be null

* defined in: [RUO - Report Structure Schema](ruo_schema-properties-samples-properties-results-properties-coverage-mean.md "RUO.schema.json#/properties/samples/properties/results/properties/Coverage (mean)")

### Coverage (mean) Type

`string`
