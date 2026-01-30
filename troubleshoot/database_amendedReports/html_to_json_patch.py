# Strategy:
# Search for revision table at top of HTML report:
'''<strong style="color:red;">R1</strong>'''
# Search for superscripts where changes occur within HTML report:
'''<sup><strong style="color:red;">R1</strong></sup>'''
# Regex to obtain R with any number (account for more than 1 revision ie MOHCCNO-1480)
# Append change to original JSON
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
from pathlib import Path
from bs4 import BeautifulSoup

# Find files based on regex
BASE_DIR = Path(__file__).resolve().parent
VERSION_REGEX = re.compile(r"v(\d+)", re.IGNORECASE)    # finds v1, v2, v3, etc in file name
REV_INDICATOR = re.compile(r"color\s*:\s*red")          # finds R1, R2, R3, etc in HTML file

def find_amended_html(base_dir: Path) -> Path:
    """Find the amended HTML file with latest version in name"""
    html_files = list(base_dir.glob("*.html"))          # find all HTML files
    if not html_files:
        raise FileNotFoundError("Found no HTML files in directory.")
    
    latest_file = None
    latest_version = -1

    for file in html_files:
        match = VERSION_REGEX.search(file.name)
        if match:
            version = int(match.group(1))       # converts version to integer
            if version > latest_version:        # return latest version
                latest_version = version
                latest_file = file
    
    if not latest_file:                         # different naming convention
        raise ValueError("No HTML files contain version in their name (v1, v2, etc).")
    return latest_file                          # latest amended HTML

def find_original_json(latest_html: Path, base_dir: Path) -> Path:
    """Find the original JSON to patch"""
    base_match = re.split(r"-v|_report", latest_html.stem, maxsplit=1)[0]       # matches report ID

    candidate_json = [f for f in base_dir.glob("*.json") if f.stem.startswith(base_match)]
    if not candidate_json:
        raise FileNotFoundError(f"Found no JSON files matching base '{base_match}'")

    lowest_version = float("inf")
    original_json = None
    for file in candidate_json:
        match = VERSION_REGEX.search(file.name)            # search for version in JSON name
        version = int(match.group(1)) if match else 0
        if version < lowest_version:                    # original json is being amended
            lowest_version = version
            original_json = file
    return original_json

# Parse version from HTML name
def parse_html_version(html_path: Path) -> int:
    """Extract version number from HTML file using regex"""
    version_match = VERSION_REGEX.search(html_path.name)
    if not version_match:
        raise ValueError(f"Cannot detect version in HTML file.")
    return int(version_match.group(1))

def name_amended_json(original_json: Path, version: int) -> Path:
    """Write file name for amended JSON based on amended HTML version"""
    base = re.sub(r"v\d+", "", original_json.stem, flags=re.IGNORECASE)     # remove existing v#
    base = re.sub(r"(_report)?$", "", base, flags=re.IGNORECASE)            # remove _report
    new_name = f"{base}-v{version}_report.json"
    return original_json.with_name(new_name)

# Load amended HTML file
def load_html(path: Path) -> BeautifulSoup:
    """Load HTML file and parse using BeautifulSoup (str)"""
    return BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")

# Find revisions in amended HTML
def find_revisions(soup: BeautifulSoup) -> list:
    """Find in-line revisions using R# superscripts"""
    revised = []
    for sup in soup.find_all("sup"):                        # all superscripts
        strong = sup.find("strong", style=REV_INDICATOR)    # bold, red superscripts
        if strong:
            revised.append(sup.parent)
    return revised

def clean_revisions(node) -> str:
    """Remove HTML formatted <sup> for clean revisions"""
    for sup in node.find_all("sup"):
        sup.decompose()
    return node.get_text(" ", strip=True)

# Revise JSON
def apply_revisions(json_data: dict, soup: BeautifulSoup):
    """Patch HTML revisions to JSON fields"""
    for node in find_revisions(soup):                               # fixed function name
        value_td = node if node.name == "td" else node.find_parent("td")
        if not value_td:
            continue                                        # skip if no <td> found
        label_td = value_td.find_previous_sibling("td")     # fixed to singular
        if not label_td:
            continue
        key = label_td.get_text(strip=True).rstrip(":").lower().replace(" ","_")
        value = clean_revisions(value_td)                  # fixed function name
        json_data.setdefault("plugins", {}).setdefault("sample", {}).setdefault("results", {})[key] = value

def main():
    amended_html = find_amended_html(BASE_DIR)                  # find latest HTML
    original_json = find_original_json(amended_html, BASE_DIR)  # find original JSON
    html_version = parse_html_version(amended_html)             # extract version number from amended HTML
    with open(original_json, "r", encoding="utf-8") as file:    # fixed encoding typo
        json_data = json.load(file)                             # load JSON into dictionary
    soup = load_html(amended_html)                              # load amended HTML
    apply_revisions(json_data, soup)                            # apply HTML revisions to JSON
    output_json = name_amended_json(original_json, html_version)   # fixed function name
    with open(output_json, "w", encoding="utf-8") as file:      # fixed encoding typo
        json.dump(json_data, file, indent=2)
    print(f"Amended JSON written to {output_json.name}")        # fixed typo in variable

if __name__ == "__main__":
    main()
