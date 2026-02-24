"""
Wrapper script thhat searches through CouchDB, retrieve reports, and filters for analysis.
    1. couchDB_dynamic_query.py: Run mango query using string-based filters to retrieve reports.
    2. couchDB_variant_search.py: Run variant-based filtering to output a subset of reports.
    3. couchDB_numeric_analysis.py: Run numeric filtering on reports and output subset of reports and plot.
    #4. couchDB_plot.py: plot script? not necessary if numeric analysis is run last.
Usage:
    python3 couchDB_query_pipeline.py
"""

import couchdb
import json
import os
import yaml
import argparse
from datetime import datetime, timedelta
import re
import shutil
import pandas as pd
import matplotlib.pyplot as plt

def read_login_file(file_path):
    """ Reads input file and returns dict with couchDB login info """
    params = {}
    with open(file_path, "r") as f:
        for line in f:
            if ':' in line:
                key, value = line.strip().split(':', 1)
                params[key.strip()] = value.strip()
    return params




# subprocess.run(): combine arguments, parse, pass to both scripts

# Logging/timing for each step
