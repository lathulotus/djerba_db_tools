# Annotated code (used to manually amend reports)
# Usage:
# Run this in the directory where the html is located 
# $ module load djerba
# $ python3 path/to/html_to_pdf.py

import os
import pdfkit
import sys
from time import strftime

if len(sys.argv)==2: #two arguments ('html_to_pdf.py', 'reportID.html')
    report_id = sys.argv[1] #second item is report id
    version = '1' #assign version 1
elif len(sys.argv)==3: #three arguments ('html_to_pdf.py', 'reportID', 2)
    report_id = sys.argv[1] #second item is report id
    version = sys.argv[2] #third item is version
else:
    print("Usage: html_to_pdf.py REPORT_ID [VERSION: optional, defaults to 1]", file=sys.stderr)
    sys.exit(1) #error therefore exit

date = strftime('%Y-%m-%d') #2026-01-27
report_name = report_id+'-v'+version #reportID-v1
options = {
    'footer-right': '[page] of [topage]', #current_page of total_page
    'footer-left': date+' - '+report_name #2026-01-27 - reportID-v1
}

html_path = report_name+'_report.clinical.html' #reportID_report.clinical.html
if not os.path.exists(html_path): #if file missing
    print('Expected input does not exist: '+html_path)
    sys.exit(1)

pdfkit.from_url(html_path, report_name+'_report.clinical.pdf', options=options) #read HTML, writes PDF
