# Troubleshooting

## Report Names
> [Repository](https://github.com/lathulotus/cgi_djerba/tree/main/troubleshoot/database_reportNames)
> [Ticket 1679](https://jira.oicr.on.ca/browse/GCGI-1679)

CouchDB only stores the most updated versions of reports due to Djerba overwriting documents with the same report IDs (409 Conflict). Therefore, a failed clinical report may be lost after being overwritten by the resulting RUO report. Changing naming convention can prevent reports from being overwrittenn.

**TASK**: Archiving different versions of reports on the same requisition by:
1. Identifying report types under attributes
2. Using regular expressions to match report IDs (any version)
3. Concatenating report type to the report ID
- Ex: reportID-v1_research_report.json

