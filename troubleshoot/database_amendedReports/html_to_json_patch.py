"""Reads amended HTML and appends changes to existing JSON to create an amended JSON"""
# Usage: Run this in the directory containing the amended HTML and original JSON
# $ module load djerba
# $ python html_to_json_patch.py amended.html original.json

import sys
import re
import json
from pathlib import Path
from bs4 import BeautifulSoup

# Regex patterns
VERSION_REGEX = re.compile(r"v(\d+)", re.IGNORECASE)    # finds v1, v2, v3, etc
REV_INDICATOR = re.compile(r"color\s*:\s*red")          # finds red revision markers in HTML

# Load amended HTML file
def load_html(path: Path) -> BeautifulSoup:
    """Load amended HTML and parse into BeautifulSoup string"""
    return BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")

# Find revisions in amended HTML
def find_revisions(soup: BeautifulSoup) -> list:
    """Search for bold, red superscripts denoting in-line revisions"""
    revised = []
    for sup in soup.find_all("sup"):                        # all superscripts
        strong = sup.find("strong", style=REV_INDICATOR)    # bold, red superscripts
        if strong:
            revised.append(sup.parent)
    return revised

def clean_revisions(node) -> str:
    """Clean revisions by removing revision markers (<sup>)"""
    for sup in node.find_all("sup"):
        sup.decompose()
    return node.get_text(" ", strip=True)

def generate_key_variants(label: str) -> list:
    """Generate possible JSON key variants from an HTML label (some with underscores, some with spaces)"""
    base = label.rstrip(":").strip().lower()

    variants = {
        base,
        base.replace(" ", "_"),
        re.sub(r"[^\w\s%]", "", base),
        re.sub(r"[^\w\s%]", "", base).replace(" ", "_")
    }

    return list(variants)

def normalize_value(value: str):
    """Convert comma-separated values into list, otherwise return string"""
    if "," in value:
        return [v.strip() for v in value.split(",") if v.strip()]
    return value

# Revise JSON
def update_existing_key(obj, target_key, new_value):
    """Update fields with keys that exist in the original JSON (no new fields)"""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == target_key:
                obj[k] = new_value
            else:
                update_existing_key(v, target_key, new_value)
    elif isinstance(obj, list):
        for item in obj:
            update_existing_key(item, target_key, new_value)

def extract_report_id_revision(soup: BeautifulSoup) -> str | None:
    """Extract new report ID if amended in HTML"""
    for node in find_revisions(soup):
        value_td = node if node.name == "td" else node.find_parent("td")
        if not value_td:
            continue
        label_td = value_td.find_previous_sibling("td")
        if not label_td:
            continue

        label = label_td.get_text(strip=True).rstrip(":").lower()
        if label == "report id":
            return clean_revisions(value_td)
    return None

def apply_revisions(json_data: dict, soup: BeautifulSoup):
    """Patch original JSON with HTML amendments"""
    for node in find_revisions(soup):
        value_td = node if node.name == "td" else node.find_parent("td")
        if not value_td:
            continue
        label_td = value_td.find_previous_sibling("td")
        if not label_td:
            continue

        label = label_td.get_text(strip=True)
        key_variants = generate_key_variants(label)

        # exceptions: known HTML to JSON label mismatches
        if "blood_sample_id" in key_variants:
            key_variants.append("normal_id")
        elif "tumour_sample_id" in key_variants:
            key_variants.append("tumour_id")
        elif "site_of_biopsy/surgery" in key_variants:
            key_variants.append("site_of_biopsy")

        value = normalize_value(clean_revisions(value_td))

        for key in key_variants:
            update_existing_key(json_data, key, value)

def apply_report_id_updates(json_data: dict, amended_report_id: str):
    """Patch original JSON with HTML amendments specific to report IDs"""
    base_id = re.sub(r"-v\d+$", "", amended_report_id)

    update_existing_key(json_data, "_id", amended_report_id)
    update_existing_key(json_data, "report_id", amended_report_id)
    update_existing_key(json_data, "requisition_id", base_id)

    html_cache = json_data.get("html_cache")
    if isinstance(html_cache, dict) and len(html_cache) == 1:
        old_key = next(iter(html_cache))
        html_cache[f"{amended_report_id}_report.clinical"] = html_cache.pop(old_key)

def name_amended_json(amended_html: Path, amended_report_id: str | None) -> Path:
    """Write file name for amended JSON"""
    if amended_report_id:
        return amended_html.with_name(f"{amended_report_id}_report.clinical.json")
    return amended_html.with_suffix(".json")

def main():
    """Combine functions to patch JSON"""
    if len(sys.argv) != 3:
        raise RuntimeError("Usage: python html_to_json_patch.py amended.html original.json")

    amended_html = Path(sys.argv[1])
    original_json = Path(sys.argv[2])

    with open(original_json, "r", encoding="utf-8") as file:
        json_data = json.load(file)                             # load JSON into dictionary

    soup = load_html(amended_html)                              # load amended HTML
    apply_revisions(json_data, soup)                            # apply HTML revisions to JSON

    amended_report_id = extract_report_id_revision(soup)
    if amended_report_id:
        apply_report_id_updates(json_data, amended_report_id)

    output_json = name_amended_json(amended_html, amended_report_id)

    with open(output_json, "w", encoding="utf-8") as file:
        json.dump(json_data, file, indent=2)

    print(f"Amended JSON written to {output_json.name}")

if __name__ == "__main__":
    main()
