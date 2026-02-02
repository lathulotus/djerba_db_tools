"""Reads amended HTML and appends changes to existing JSON to create an amended JSON"""
# Usage: Run this in the directory containing the original JSON and amended HTML
# $ module load djerba
# $ python html_to_json_patch.py

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

def name_amended_json(amended_html: Path) -> Path:
    """Write file name for amended JSON based directly on amended HTML name"""
    return amended_html.with_suffix(".json")

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
def update_existing_key(obj, target_key, new_value):
    """Recursively update existing keys in nested dicts/lists"""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == target_key:
                obj[k] = new_value
            else:
                update_existing_key(v, target_key, new_value)
    elif isinstance(obj, list):
        for item in obj:
            update_existing_key(item, target_key, new_value)

def apply_revisions(json_data: dict, soup: BeautifulSoup):
    """Patch HTML revisions to JSON fields"""
    for node in find_revisions(soup):
        value_td = node if node.name == "td" else node.find_parent("td")
        if not value_td:
            continue
        label_td = value_td.find_previous_sibling("td")
        if not label_td:
            continue

        key = label_td.get_text(strip=True).rstrip(":").lower().replace(" ","_")

        # handle known field name exception
        if key == "blood_sample_id":
            key = "normal_id"

        value = clean_revisions(value_td)

        # update existing fields instead of appending new ones
        update_existing_key(json_data, key, value)

def main():
    amended_html = find_amended_html(BASE_DIR)                  # find latest HTML
    original_json = find_original_json(amended_html, BASE_DIR)  # find original JSON

    with open(original_json, "r", encoding="utf-8") as file:
        json_data = json.load(file)                             # load JSON into dictionary

    soup = load_html(amended_html)                              # load amended HTML
    apply_revisions(json_data, soup)                            # apply HTML revisions to JSON

    output_json = name_amended_json(amended_html)               # assign JSON based on HTML name

    with open(output_json, "w", encoding="utf-8") as file:
        json.dump(json_data, file, indent=2)

    print(f"Amended JSON written to {output_json.name}")

if __name__ == "__main__":
    main()
