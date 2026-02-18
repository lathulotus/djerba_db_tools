# Querying CouchDB: Usage Guide
Querying CouchDB database to assess reports stored by Djerba. Complete script can be found under **[couchDB_dynamic_query.py](./couchDB_dynamic_query.py)**.


Usage to download filtered reports:
> `python3 couchdb_query.py --login_file login.txt --filters_file filters.yaml --output_dir ./output_folder`

Usage to count reports without download:
> `python3 couchdb_query.py --login_file login.txt --filters_file filters.yaml --count`

## Login Credentials
Connection **must** be authenticated by setting host, port, database name, and login credentials. Such values can be saved as a text file and be run alongside the `login_file` flag. Login file is required. Text file to be organized as follows:

```
host: djerba-dev-db.gsi.oicr.on.ca
port: 5984
db_name: database_name
username: username
password: password
```

## Filters for Querying
Filters **must** be set by running a `filters.yaml` file after the `filters_file` flag. Filters should be defined within the pre-existing YAML file, in which fields that are not being searched should be set to `null`. Filters file is required.

Visit **[query_types](./query_types.md)** to view supported filter types, definitions, and example.

## Downloading Files
To download all reports that satisfy the set filters, `--output_dir` can be set to specify a path to a directory that holds all reports. Otherwise, this defaults to the folder in which the command is run.

## Count Only
To assess report counts without downloading reports that satisfy the set filters, `--count` can be run at the end. This exports an integer representing reports that satisfy the filters.

## Page Size
Current script is run across all reports found in the specified database. The page size across which reports are assessed can be set using the `--page_size` flag, which takes integers. Otherwise, this defaults to `500`.