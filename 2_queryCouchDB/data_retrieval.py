# Retrieve data from reports on CouchDB for querying
# Usage:

# Environment
import os
import re
import json
import requests
import logging
from glob import glob
from dotenv import load_dotenv

load_dotenv()

class CouchDBClient:
    def __init__(self):
        self.base_url = os.getenv("COUCH_URL")
        self.db_name = os.getenv("COUCH_DB")


# 

