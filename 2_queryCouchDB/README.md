# Querying CouchDB: Usage Guide
Querying is done using the pipeline script, found under **[couchDB_query_pipeline.py](./couchDB_query_pipeline.py)**.

|             Supports                   |                          Script                                   |
|----------------------------------------|-------------------------------------------------------------------|
| Local report retrieval                 |  **[couchDB_dynamic_query.py](./couchDB_dynamic_query.py)**       |
| Filtering by general string parameters |  **[couchDB_dynamic_query.py](./couchDB_dynamic_query.py)**       |
| Filtering by variant-associated fields |  **[couchDB_variant_search.py](./couchDB_variant_search.py)**     |
| Filtering by numeric fields            |  **[couchDB_numeric_analysis.py](./couchDB_numeric_analysis.py)** |
| Plotting report accumulation           |  **[couchDB_numeric_analysis.py](./couchDB_numeric_analysis.py)** |

## Query Pipeline: Filters & Usage
Querying requires a config YAML, found under **[couchDB_query_pipeline.yaml](./couchDB_query_pipeline.yaml)**. To run the pipeline in commandline, python (v8+):

```
python3 couchDB_query_pipeline.py --config couchDB_query_pipeline.yaml
```

Filters **must** be set by running a `couchDB_query_pipeline.yaml` file after the `config` flag. Filters should be defined within the [pre-existing YAML file](./couchDB_query_pipeline.yaml), in which fields that are not being searched should be set to `null` or `false` or `true`, as per the template. Filters file is **required** and login **must** be authenticated for connection to the database.

Visit **[query_types](./query_types.md)** to view supported filter types, definitions, and example.

<br>

### Login Authentification
Connection **must** be authenticated by setting host, port, database name, and login credentials. If pipeline script is being run, login is directly added to pre-existing YAML. If dynamic querying is run alone, such values can be saved as a text file and be run alongside the `login_file` flag. Login file is required. Text file to be organized as follows:


```
host: url
port: 0000
db_name: database_name
username: username
password: password
```

<br>

### Retrieve
Retrieval [script](./couchDB_dynamic_query.py) allows for local download of reports from CouchDB. Dynamic querying to download reports based on Mango search logic works best for string-based querying. As such, this script supports querying through fields containing string values.

`run_retrieve` must be set to `true` for CouchDB query and filtering.

To run dynamic querying without running pipeline script using simplified [filter.txt](./couchDB_dynamic_filters.yaml):
- Downloading reports: `python3 couchDB_dynamic_query.py --login_file login.txt --filters_file filters.yaml --output_dir script1_output/`
- Counting filtered reports: `python3 couchDB_dynamic_query.py --login_file login.txt --filters_file filters.yaml --count`

 <br>

### Variant
Variant searching [script](./couchDB_variant_search.py) allows for gene or alteration-based searching. To bypass naming conventions, python-based search logic is applied to already downloaded reports to perform variant-based querying.

`run_variant` can be set to `true` if being filtered. Else, must be set to `false`.

To run variant filtering without running pipeline, using in-line flags:
- `python3 couchDB_variant_search.py --input_dir script1_output/ --snv_gene TP53 --output_dir filtered_TP53/`

<br>

### Numeric
Numeric querying [script](./couchDB_numeric_analysis.py) allows for analysis and plotting of quantitative data. To bypass lexicographic logic applied to integers saved as strings, python-based search logic is applied to downloaded reports to perform integer querying and visual analysis. 

`run_numeric` can be set to `true` if being filtered or plotted. Else, must be set to `false`.

To run numeric filtering without running pipeline, using in-line flags:
- `python3 couchDB_numeric_analysis.py --input_dir script1_output/ --output_dir script2_output/ --plot`

<br>

### Summary
Summary table generation [script](./couchDB_summary.py) results in the generation of a summary table (XLSX, CSV) of data extracted from reports. Files can be used for ease of data analysis or downstream plotting.

`run_variant` can be set to `true` to generate table. Else, can be set to `false`.

To run summary table generation without running pipeline:
- `python3 couchDB_summary.py --input_dir reports_input/ --output_name output_summary`