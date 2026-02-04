# Troubleshooting

## Report Names
> [Repository](./database_reportNames) | [Ticket 1679](https://jira.oicr.on.ca/browse/GCGI-1679)

CouchDB only stores the most updated versions of reports due to Djerba overwriting documents with the same report IDs (409 Conflict). Therefore, a failed clinical report may be lost after being overwritten by the resulting RUO report. Changing naming convention can prevent reports from being overwrittenn.

**TASK**: Archiving different versions of reports on the same requisition by:
1. Identifying report types under attributes
2. Using regular expressions to match report IDs (any version)
3. Concatenating report type to the report ID (ex: reportID-v1_report_research.json)


## Amended Reports
> [Repository](./database_amendedReports) | [Ticket]()

CouchDB only stores JSON files. Amended reports are manually edited using an ```html_to_pdf.py``` script, thereby not producing nor editing and JSON files. As such, amended reports do not get archived on CouchDB. Modifying the JSON file rather than the HTML could allow for archiving of JSONs.

**TASK**: Modify the JSON instead of HTML (thereby running djerba.py update)
1. Read amended HTML and compare to existing/original JSON
2. Edit modifications from amended HTML to existing JSON
3. Use this as a basis to write instructions on how to modify JSON instead of HTML
4. Allowing team to run ```djerba.py update``` to upload to CouchDB and generate PDF


