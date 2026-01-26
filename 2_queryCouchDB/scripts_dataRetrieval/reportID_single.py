# Fetch by Report ID (Single)
# Purpose: Fetch single report based on ID

# Environment
from configparser import ConfigParser
import json
import logging
import pdfkit
import os
import re
from glob import glob
from PyPDF2 import PdfMerger
import djerba.util.ini_fields as ini
from djerba.core.base import base as core_base
from djerba.core.database import database
from djerba.util.date import get_todays_date
from djerba.core.extract import extraction_setup
from djerba.core.html_cache import html_cache, DjerbaHtmlCacheError
from djerba.core.ini_generator import ini_generator
from djerba.core.json_validator import plugin_json_validator
from djerba.core.render import html_renderer, pdf_renderer
from djerba.core.loaders import \
    plugin_loader, merger_loader, helper_loader, core_config_loader
from djerba.core.workspace import workspace
from djerba.util.args import arg_processor_base
from djerba.util.logger import logger
from djerba.util.validator import path_validator
from djerba.version import get_djerba_version
import djerba.core.constants as cc
import djerba.util.constants as constants

url = os.environ["COUCH_URL"] #link to CouchDB
db = os.environ["COUCH_DB"]
user = os.environ["COUCH_USER"] #username
pwrd = os.environ["COUCH_PASS"] #password


# 

