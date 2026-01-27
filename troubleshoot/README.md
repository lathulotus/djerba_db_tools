# Troubleshooting

## Report Names
> [Repository](https://github.com/lathulotus/cgi_djerba/tree/main/troubleshoot/database_reportNames) | [Ticket 1679](https://jira.oicr.on.ca/browse/GCGI-1679)

CouchDB only stores the most updated versions of reports due to Djerba overwriting documents with the same report IDs (409 Conflict). Therefore, a failed clinical report may be lost after being overwritten by the resulting RUO report. Changing naming convention can prevent reports from being overwrittenn.

**TASK**: Archiving different versions of reports on the same requisition by:
1. Identifying report types under attributes
2. Using regular expressions to match report IDs (any version)
3. Concatenating report type to the report ID (ex: reportID-v1_research_report.json)


## Amended Reports
> [Repository](https://github.com/lathulotus/cgi_djerba/tree/main/troubleshoot/database_HTMLtoJSON) | [Ticket]()

CouchDB only stores JSON files. Amended reports are manually edited using an ```html_to_pdf.py``` script, thereby not producing nor editing and JSON files. As such, amended reports do not get archived on CouchDB. Modifying the JSON file rather than the HTML could allow for archiving of JSONs.

**TASK**: Modify the JSON instead of HTML (thereby running djerba.py update)
1. Convert modified HTML to JSON to see what it looks like
2. Use this as a basis to write instructions on hot to modify JSON instead of HTML
3. Allowing team to run ```djerba.py update``` to upload to CouchDB and generate PDF

**ALTERNATIVW**: Archive HTML files rather than JSON
1. Modify existing python script (```html_to_pdf.py```) to upload HTML



