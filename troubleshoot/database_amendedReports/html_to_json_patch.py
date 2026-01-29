# Strategy:
# Search for superscripts where changes occur within HTML report:
'''<sup><strong style="color:red;">R1</strong></sup>'''
# Search for revision table at top of HTML report:
'''<strong style="color:red;">R1</strong>'''
# Regex to obtain R with any number (account for more than 1 revision ie MOHCCNO-1480)
#---------------------------------------------------


"""Reads amended HTML and appends changes to original JSON (v1) to be saved as an amended JSON (v2)"""
# Usage:
# Run this in the directory where the original JSON and amended HTML are located
# $ module load djerba
# $python3 path/to/html_to_json.py

import os
import sys
import re
import json
from string import Template
from markdown import markdown
from djerba.util.oncokb.tools import levels as oncokb_levels
from bs4 import BeautifulSoup

# Defining version (>=2)
if len(sys.argv) == 3:      # html_to_json_patch.py, originalReport-v1.json, amendedReport-v2.html
    report_id = sys.argv[2] # third item is report ID -> SAVE HTML VER OR TITLE AS THE REPORT ID? THIS WOULD CHANGE IT TO THE UPDATED VERSION
    if "v1" in report_id:
        version = "2"       # defaults to 2 | REGULAR EXPRESSIONS TO EXTRACT THE NUMBER AND ADD 1 TO IT
elif len(sys.argv) == 3:    # html_to_json_patch.py, originalReport-v1.json, amendedReport-v2.html, 2
    report_id = sys.argv[2]
    version = sys.argv[3]   #fourth item is version
else:
    print("Usage: html_to_json_patch.py REPORT_ID [VERSION: optional, defaults to 2]", file=sys.stderr)
    sys.exit(1)             # error: too many/little files

report_name = report_id+'-v'+version



# Asigning report paths/names by attributes
# NOTE: this should be done at the end -> fallback to id failed clinical reports
# NOTE: read this from the HTML: "(RUO)" in report suggests failed clinical
original_report_id = report_data[cc.CORE][cc.REPORT_ID]
try:
    attributes = (
        report_data
        .get("plugins", {})
        .get("supplement.body", {})
        .get("attributes", [])
    )
    analysis_type = "_".join(attributes) if attributes else None

    if analysis_type:
        # Match everything before v<number>
        match = re.match(r"^(.*?)([vV]\d+)$", original_report_id)

        if match:
            base_id, version = match.groups()
            report_id = f"{base_id}-{version}-{analysis_type}"
        else:
            # Fallback if no version pattern is found
            report_id = f"{original_report_id}-{analysis_type}"
    else:
        report_id = original_report_id

html_path = report_name+'_report.clinical.html'     # automatically assigns all report names as clinical ??
if not os.path.exists(html_path):
    print('Expected input does not exist: '+'html_path')
    sys.exit(1)
#pdfkit.from_url(html_path, report_name+'_report.clinical.pdf', options=options)

def _debug(debug, message, prefix=''):
    """Print the given message if debugging is true."""
    if debug:
        print('{}{}'.format(prefix, message))
        # add a newline after every message
        print('')


def _record_element_value(element, json_output):
    """Record the html element's value in the json_output."""
    element = element.strip()
    if element != '\n' and element != '':
        if json_output.get('_value'):
            json_output['_values'] = [json_output['_value']]
            json_output['_values'].append(element)
            del json_output['_value']
        elif json_output.get('_values'):
            json_output['_values'].append(element)
        else:
            json_output['_value'] = element


def _iterate(
    html_section,
    json_output,
    count,
    debug,
    capture_element_values,
    capture_element_attributes,
):
    _debug(debug, '========== Start New Iteration ==========', '    ' * count)
    _debug(debug, 'HTML_SECTION:\n{}'.format(html_section))
    _debug(debug, 'JSON_OUTPUT:\n{}'.format(json_output))
    for part in html_section:
        if not isinstance(part, str):
            # for python2 - check if part is unicode
            try:
                string_is_unicode = isinstance(part, unicode)
            # for python3 - catch error when trying to use the name 'unicode'
            except NameError:
                string_is_unicode = False
            # no matter what - keep going
            finally:
                # if part is not unicode, record it
                if not string_is_unicode:
                    if not json_output.get(part.name):
                        json_output[part.name] = list()
                    new_json_output_for_subparts = dict()
                    if part.attrs and capture_element_attributes:
                        new_json_output_for_subparts = {'_attributes': part.attrs}
                    count += 1
                    json_output[part.name].append(
                        _iterate(
                            part,
                            new_json_output_for_subparts,
                            count,
                            debug=debug,
                            capture_element_values=capture_element_values,
                            capture_element_attributes=capture_element_attributes,
                        )
                    )
                # this will only be true in python2 - handle an entry that is unicode
                else:
                    if capture_element_values:
                        _record_element_value(part, json_output)
        else:
            if capture_element_values:
                _record_element_value(part, json_output)
    return json_output


def convert(
    html_string,
    debug=False,
    capture_element_values=True,
    capture_element_attributes=True,
):
    """Convert the html string to json."""
    soup = bs4.BeautifulSoup(html_string, 'html.parser')
    children = [child for child in soup.contents]
    return _iterate(
        children,
        {},
        0,
        debug=debug,
        capture_element_values=capture_element_values,
        capture_element_attributes=capture_element_attributes,
    )