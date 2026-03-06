import json
import os
import re
import yaml
import couchdb
from datetime import datetime
from urllib.parse import urlparse, urlunparse

def parse_version(version_str):
    """ Convert version string to a tuple of integers for comparison """
    try:
        if not version_str:
            return (0,)
        return tuple(map(int, re.sub(r'[^\d.]', '', str(version_str)).split('.')))
    except:
        return (0,)

def get_nested(data, paths):
    """ Get nested values from dict by slash-separated paths """
    if isinstance(paths, str):
        paths = [paths]
    for path in paths:
        keys = path.split('/')
        current = data
        for key in keys:
            if isinstance(current, dict):
                current = current.get(key)
            else:
                current = None
                break
        if current not in (None, "", [], {}):
            return current
    return None

def transform_value(raw_val, value_type):
    """ Convert raw string or JSON value to the appropriate type for comparison """
    if raw_val in (None, "", []):
        return None
    
    raw_str = str(raw_val).strip()
    
    try:
        if value_type == 'float':
            return float(raw_str)
        if value_type == 'int':
            return int(raw_str)
        if value_type == 'version':
            return parse_version(raw_str)
        if value_type == 'date':
            date_fmts = ["%Y-%m-%d", "%d/%m/%Y %H:%M", "%d/%m/%Y_%H:%M:%S", "%d/%m/%Y_%H:%M:%SZ"]
            for fmt in date_fmts:
                try:
                    return datetime.strptime(raw_str, fmt)
                except:
                    pass
            # Fallback if none of the formats match
            return datetime.strptime(raw_str[:10], "%Y-%m-%d")
        return raw_val
    except Exception:
        return None

def read_filters_yaml(file_path):
    """ Reads YAML file containing query filters. Supports standalone or pipeline config. """
    with open(file_path, "r") as f:
        data = yaml.safe_load(f)
    if data and "filters" in data and "dynamic" in data["filters"]:
        return data["filters"]["dynamic"]
    return data

def read_login_file(file_path):
    """ Reads input file and returns dict with couchDB login info """
    with open(file_path, "r") as f:
        data = yaml.safe_load(f)
    if data and "login_file" in data:
        return data["login_file"]
    return data

def get_couchdb_database(host, port, db_name, username=None, password=None):
    """ Connects to couchDB using login info and returns specified database object """
    try:
        url = f"http://{host}:{port}/"
        if username and password:
            scheme, netloc, path, params, query, fragment = urlparse(url)
            netloc = f"{username}:{password}@{host}:{port}"
            url = urlunparse((scheme, netloc, path, params, query, fragment))
        
        print("Connecting to CouchDB...", flush=True)
        couch = couchdb.Server(url)

        if db_name not in couch:
            raise ValueError(f"Database '{db_name}' does not exist on the server.")
        
        db = couch[db_name]
        print("Established connection.", flush=True)
        return db
    except Exception as e:
        print(f"Error connecting to couchDB: {e}")
        raise
