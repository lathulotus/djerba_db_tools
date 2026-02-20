# Troubleshooting

## Archiving by Report Types
> [Repository](./archiving_reportTypes) | [Ticket 1679](https://jira.oicr.on.ca/browse/GCGI-1679)

CouchDB only stores the most updated versions of reports due to Djerba overwriting documents with the same report IDs (409 Conflict). Therefore, a failed clinical report may be lost after being overwritten by the resulting RUO report. Changing naming convention can prevent reports from being overwrittenn.

**TASK**: Edit `database.py` to archive different versions of reports on the same requisition
1. Identifying report types under attributes
2. Using regular expressions to match report IDs (any version)
3. Concatenating report type to the report ID (ex: reportID-v1_report_research.json)


## Amended Reports
> [Repository](./amended_reports) | [Ticket]()

CouchDB only stores JSON files. Amended reports are manually edited using an ```html_to_pdf.py``` script, thereby not producing nor editing and JSON files to be saved onto CouchDB. As such, amended reports do not get archived on CouchDB. Modifying the script to automatically upload HTMLs to the database could allow amended reports to be archived.

**TASK**: Update `html_to_pdf.py` script to upload HTML
1. Use upload logic from djerba.py update
2. Modify script to upload HTML upon run
3. Account for HTML documents during querying


## Last Updated
> [Repository](./last_updated) | [Ticket]()

Last updated field saves in date/month/year format along with string timestamp (i.e., 30/01/2026_12:34:10Z). To allow for simple querying, format can be changed to year/month/date, and timestamp can be removed (or saved to another field if required).

**TASK**: Edit `database.py` to change the last_updated field
1. Edit from d/m/y to y-m-d
2. Remove timestamp or save to another field if required