
# Usage:
# Run this in the directory where the html is located 
# $ module load djerba
# $ python3 path/to/html_to_pdf.py

import os
import pdfkit
import sys
from time import strftime

if len(sys.argv)==2:
    report_id = sys.argv[1]
    version = '1'
elif len(sys.argv)==3:
    report_id = sys.argv[1]
    version = sys.argv[2]
else:
    print("Usage: html_to_pdf.py REPORT_ID [VERSION: optional, defaults to 1]", file=sys.stderr)
    sys.exit(1)

date = strftime('%Y-%m-%d')
report_name = report_id+'-v'+version
options = {
    'footer-right': '[page] of [topage]',
    'footer-left': date+' - '+report_name
}

html_path = report_name+'_report.clinical.html'
if not os.path.exists(html_path):
    print('Expected input does not exist: '+html_path)
    sys.exit(1)

pdfkit.from_url(html_path, report_name+'_report.clinical.pdf', options=options)


# Upload amended HTML to CouchDB
