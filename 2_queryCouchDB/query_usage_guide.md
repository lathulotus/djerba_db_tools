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
from couchdb_reader import couchdb_reader
reader=couchdb_reader()
report=reader.fetch_single("report_id-v1")
print(report.keys())
```

## Fetch Multiple Reports
```
from couchdb_reader import couchdb_reader
reader=couchdb_reader()
reports=reader.fetch_bulk(["report_id1-v1","report_id2-v1","report_id3-v1"])
print(reports[0]["config"][case_overview])
```

## Filter Metadata Fields
### Filtering simple fields or getting a range of data based on date or report type.
```
"metadata": {
  "report_date": "2024-10-12"
}
```

```
selector = {
    "metadata.report_date": {
        "$gte": "2024-01-01",
        "$lte": "2024-12-31"
    }
}

reports = reader.fetch_metadata(selector)
```

### Filtering specific fields such as primary cancer type or biomarker values.
```
selector = {
    "config.case_overview.primary_cancer": "Ovarian Cancer"
}
reports = reader.fetch_metadata(selector)
```

```
selector = {
    "results.biomarkers.HRD": "Positive"
}
reports = reader.fetch_metadata(selector)
```

### Combined filtering of specific fields such as both primary cancer type and biomarker values.
```
selector = {
    "config.case_overview.primary_cancer": "Ovarian Cancer",
    "results.biomarkers.HRD": "Positive",
    "results.biomarkers.MSI": "Stable"
}
reports = reader.fetch_metadata(selector)
```