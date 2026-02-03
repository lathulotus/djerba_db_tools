## Amended Reports
> [Repository](/database_amendedReports) | [Ticket]()

CouchDB only stores JSON files. Amended reports are manually edited using an ```html_to_pdf.py``` script, thereby not producing nor editing and JSON files. As such, amended reports do not get archived on CouchDB. Modifying the JSON file rather than the HTML could allow for archiving of JSONs.

**TASK**: Modify the JSON instead of HTML (thereby running djerba.py update)
1. Read amended HTML and compare to existing/original JSON
2. Edit modifications from amended HTML to existing JSON
3. Use this as a basis to write instructions on hot to modify JSON instead of HTML
4. Allowing team to run ```djerba.py update``` to upload to CouchDB and generate PDF