# How to Query CouchDB
A guide to querying CouchDB.

## Environment
Authenticate using environment variables to allow read-only access to CouchDB using external credentials. Input credentials and set connection to CouchDB. 

```
COUCH_URL=insert_url
COUCH_DB=insert_database
COUCH_USER=insert_username
COUCH_PASS=insert_password
```

## Fetch Single Report

```
python fetch_reports.py --report-id SAMPLE-REPORT1_v1
```

## Fetch Multiple Reports
```
python fetch_reports.py --bulk-ids REPORT_IDs.txt
```

## Filter Metadata Fields
### Filtering simple fields or getting a range of data based on date or report type.
```
CODE
```

```
CODE
```

### Filtering specific fields such as primary cancer type or biomarker values.
```
CODE
```

```
CODE
```

### Combined filtering of specific fields such as both primary cancer type and biomarker values.
```
CODE
```