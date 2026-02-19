## Amended Reports
> [Repository](./amended_reports) | [Ticket]()

CouchDB only stores JSON files. Amended reports are manually edited using an ```html_to_pdf.py``` script, thereby not producing nor editing and JSON files to be saved onto CouchDB. As such, amended reports do not get archived on CouchDB. Modifying the script to automatically upload HTMLs to the database could allow amended reports to be archived.

**TASK**: Update `html_to_pdf.py` script to upload HTML
1. Use upload logic from djerba.py update
2. Modify script to upload HTML upon run
3. Account for HTML documents during querying

**OLD TASK**: Modify the JSON instead of HTML (thereby running djerba.py update)
1. Read amended HTML and compare to existing/original JSON
2. Edit modifications from amended HTML to existing JSON
3. Use this as a basis to write instructions on how to modify JSON instead of HTML
4. Allowing team to run ```djerba.py update``` to upload to CouchDB and generate PDF