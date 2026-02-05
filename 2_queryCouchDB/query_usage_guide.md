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
To fetch a single report based on a known report ID, use the following example. Replace ```SAMPLE-REPORT_v1``` with the ID of the single report that needs to be fetched.
```
python fetch_report.py --report-id SAMPLE-REPORT_v1
```

## Fetch Multiple Reports
To fetch a number of reports based on known report IDs, use the following example. This requires a text file containing each report ID found on a new line.
```
python fetch_report.py --bulk-ids REPORT_IDs.txt
```

## Filter Metadata Fields
Filtering simple fields or getting a range of data based on date or report type.
```
python fetch_report.py --report-type clinical
```

To filter specific metadata fields, use the following example for primary cancer type. 
```
python fetch_report.py --primary-cancer "Ovarian Cancer"
```

Combined filtering of specific fields such as both primary cancer type and report type.
```
python fetch_report.py --report-type clinical --primary-cancer "Ovarian Cancer"
```