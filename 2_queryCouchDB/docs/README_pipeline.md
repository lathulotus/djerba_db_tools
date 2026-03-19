# Usage Guide: Running the Pipeline
Querying is done using the pipeline script, found under **[couchDB_query_pipeline.py](../couchDB_query_pipeline.py)**. Each script supports different functions, as laid out in this table...
|                      Script                                |            Supports                                  |
|------------------------------------------------------------|------------------------------------------------------|
|**[couchDB_dynamic_query.py](../couchDB_dynamic_query.py)**  |Local report retrieval via string-based Mango querying|
|**[couchDB_variant_search.py](../couchDB_variant_search.py)**|Variant-based filtering (i.e., SNV, CNV, Fusions)     |
|**[couchDB_dynamic_query.py](../couchDB_dynamic_query.py)**  |Numeric-based filtering & plotting report accumulation|
|**[couchDB_summary.py](../couchDB_summary.py)**       |Generation of a thorough summary table                |

## Usage
Querying requires a config YAML, found under **[couchDB_query_pipeline.yaml](../couchDB_query_pipeline.yaml)**. To run the pipeline in commandline, python (v8+):

```
python3 couchDB_query_pipeline.py --config couchDB_query_pipeline.yaml
```

Config must be set by running `--config couchDB_query_pipeline.yaml`, which specifies the filters and login credentials.
- Filters should be defined within the [pre-existing YAML file](../couchDB_query_pipeline.yaml), in which fields that are not being searched should be set to null or false, as per the template.
- **Examples** on how to format this config YAML can be found under [example_config.md](./example_config.md)
- Connection **must** be authenticated by setting host, port, database name, and login credentials. Login is directly added to pre-existing config YAML.

## Run Retrieve
Retrieval [script](../couchDB_dynamic_query.py) allows for local download of reports from CouchDB. Dynamic querying to download reports based on Mango search logic works best for string-based querying. This script supports querying through fields containing string values. Run_retrieve **must** be set to true for downstream querying.

```
run_retrieve: true
```

## Run Variant
Variant searching [script](../couchDB_variant_search.py) allows for gene or alteration-based searching. To bypass naming conventions, python-based search logic is applied to already downloaded reports to perform variant-based querying.

To filter through variant-based parameters:
```
run_variant: true
```

If no variant filters are applied, must set to false:
```
run_variant: false
```

### Run Numeric
Numeric querying [script](../couchDB_numeric_analysis.py) allows for analysis and plotting of quantitative data. To bypass lexicographic logic applied to integers saved as strings, python-based search logic is applied to downloaded reports to perform integer querying and visual analysis. 

To filter through numeric parameters:
```
run_numeric: true
```

If no numeric filters are applied, must set to false:
```
run_numeric: false
```

### Run Summary
Summary [script](../couchDB_summary.py) results in the generation of a summary table as a CSV file. This table contains all data extracted from reports, providing and overview for data analysis or visualization.

To generate a summary table:
```
run_summary: true
```

<br>
