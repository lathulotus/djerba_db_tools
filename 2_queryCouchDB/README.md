# Querying CouchDB: Usage Guide
Querying CouchDB database to assess reports stored by Djerba.

## Dynamic Querying
Dynamic querying to download reports based on Mango search logic works best for string-based querying. As such, this script supports querying through fields containing string values. Complete script can be found under **[couchDB_dynamic_query.py](./couchDB_dynamic_query.py)**.

Usage to download filtered reports:
> `python3 couchDB_dynamic_query.py --login_file login.txt --filters_file filters.yaml --output_dir script1_output/`

Usage to count reports without download:
> `python3 couchDB_dynamic_query.py --login_file login.txt --filters_file filters.yaml --count`

### Login_File
Connection **must** be authenticated by setting host, port, database name, and login credentials. Such values can be saved as a text file and be run alongside the `login_file` flag. Login file is required. Text file to be organized as follows:

```
host: djerba-dev-db.gsi.oicr.on.ca
port: 5984
db_name: database_name
username: username
password: password
```

### Filters_File
Filters **must** be set by running a `filters.yaml` file after the `filters_file` flag. Filters should be defined within the [pre-existing YAML file](./filters.yaml), in which fields that are not being searched should be set to `null`. Filters file is required.

Visit **[query_types](./query_types.md)** to view supported filter types, definitions, and example.

### Downloading Files
To download all reports that satisfy the set filters, `--output_dir` can be set to specify a path to a directory that holds all reports. Otherwise, this defaults to the folder in which the command is run.

### Count Only
To assess report counts without downloading reports that satisfy the set filters, `--count` can be run at the end. This exports an integer representing reports that satisfy the filters.

### Page Size
Current script is run across all reports found in the specified database. The page size across which reports are assessed can be set using the `--page_size` flag, which takes integers. Otherwise, this defaults to `500`.

## Numeric Analysis
Mango query allows for numeric querying of integers; however, issues arise when searching lexicographically through numbers saved as string. As such, this script converts values into integers for python-based search and visual analysis. Complete script can be found under **[couchDB_numeric_analysis.py](./couchDB_numeric_analysis.py)**.

Usage:
> `python3 couchDB_numeric_analysis.py --input_dir script1_output/ --output_dir numeric_output/ --plot`

## Variant Search
Mango query is stringent in its querying logic. To bypass naming conventions, python-based search is applied to perform variant-based querying. Complete script can be found under **[couchDB_variant_search.py](./couchDB_variant_search.py)**.

Usage to download filtered reports:
> `python3 couchDB_vaiant_search.py --input_dir script1_output/ --output_dir variant_output/`