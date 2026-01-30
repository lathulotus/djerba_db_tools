# Usage:
# Run this in the directory where the html and querySchema are located
# $ module load djerba
# $python3 path/to/html_to_json.py


import os
import sys
import re
import json
from time import strftime
from pathlib import Path
from bs4 import BeautifulSoup

# Load query schema
def load_schema(filename: str="schema_query.json") -> dict:
    schema_path = Path(filename)
    if not schema_path.exists():
        raise FileNotFoundError(f"Query schema file not found in current directory.")
    return json.loads(schema_path.read_text())

# Define plugins to be extracted
EXTRACTORS = {}
def register_extractor(plugin_name):
    def wrapper(func):
        EXTRACTORS[plugin_name] = func
        return func
    return wrapper

# Robust generic extractor for plugins
def gen_extractor(plugin_name: str, soup: BeautifulSoup, schema: dict):
    pattern_props = schema["properties"]["plugins"].get("patternProperties", {})
    if pattern_props:
        plugin_schema = next(iter(pattern_props.values()))
        results_schema = plugin_schema.get("properties", {}).get("results", {})
    else:
        results_schema = {}

    results = {}
    for field, field_schema in results_schema.get("properties", {}).items():
        fieldType = field_schema.get("type", "string")
        if fieldType == "string":
            results[field] = ""
        elif fieldType == "number":
            results[field] = None
        elif fieldType == "boolean":
            results[field] = False
        elif fieldType == "object":
            results[field] = {}
        elif fieldType == "array":
            results[field] = []
        else:
            results[field] = None

    return {
        "plugin_name": plugin_name,
        "version": "",
        "priorities": {},
        "attributes": [],
        "merge_inputs": {},
        "results": results,
        "url": ""
    }

# Parse <table class="info"> blocks grouped by <h3> headers
def parse_labeled_info_tables(soup: BeautifulSoup) -> dict:
    sections = {}
    current_section = None
    for elem in soup.find_all(["h3", "table"]):
        if elem.name == "h3":
            current_section = elem.get_text(strip=True).lower().replace(" ", "_")
            sections[current_section] = {}
        elif elem.name == "table" and "info" in elem.get("class", []):
            if current_section:
                for row in elem.select("tr"):
                    cells = [c.get_text(strip=True) for c in row.select("td")]
                    if len(cells) != 2:
                        continue
                    label, value = cells
                    if label.endswith(":"):
                        key = (label[:-1]
                               .strip()
                               .lower()
                               .replace(" ", "_")
                               .replace("/", "_")
                               .replace("(", "")
                               .replace(")", ""))
                        sections[current_section][key] = value
    return sections

# Core info extractor
def extract_core_info(soup: BeautifulSoup) -> dict:
    core = {
        "author": "",
        "document_config": "",
        "report_id": "",
        "core_version": "",
        "extract_time": strftime("%Y-%m-%dT%H:%M:%S")
    }
    meta = soup.find("meta", attrs={"name": "author"})
    if meta:
        core["author"] = meta.get("content", "")
    return core

# Plugin extractors
@register_extractor("case_overview")
def extract_case_overview(soup: BeautifulSoup, schema: dict):
    sections = parse_labeled_info_tables(soup)
    results = sections.get("case_overview", {})
    return {
        "plugin_name": "case_overview",
        "version": "",
        "priorities": {},
        "attributes": [],
        "merge_inputs": {},
        "results": results,
        "url": ""
    }

@register_extractor("sample")
def extract_sample(soup: BeautifulSoup, schema: dict):
    sections = parse_labeled_info_tables(soup)
    results = sections.get("sample", {})
    return {
        "plugin_name": "sample",
        "version": "",
        "priorities": {},
        "attributes": [],
        "merge_inputs": {},
        "results": results,
        "url": ""
    }

@register_extractor("genomic_landscape")
def extract_genomic_landscape(soup: BeautifulSoup, schema: dict):
    results = {
        "genomic_landscape_info": {},
        "genomic_biomarkers": [],
        "can_report_hrd": False,
        "can_report_msi": False,
        "cant_report_hrd_reason": False,
        "ctDNA": {}
    }
    for p in soup.find_all("p"):
        text = p.get_text(" ", strip=True)
        if "Tumour Mutation Burden" not in text:
            continue

        tmb_value = re.search(r"Tumour Mutation Burden \(TMB\) was\s+([\d.]+)", text)
        if tmb_value:
            results["genomic_landscape_info"]["Tumour Mutation Burden"] = float(tmb_value.group(1))

        tmb_mutations = re.search(r"\((\d+)\s+mutations\)", text)
        if tmb_mutations:
            results["genomic_landscape_info"]["Total mutations"] = int(tmb_mutations.group(1))

        tmb_category = re.search(r"classified it as\s+([^.]+)\.", text)
        if tmb_category:
            results["genomic_landscape_info"]["TMB category"] = tmb_category.group(1).strip()

        pan_percentile = re.search(r"(\d+)(?:st|nd|rd|th) percentile of the pan-cancer cohort", text)
        if pan_percentile:
            results["genomic_landscape_info"]["Pan-cancer percentile"] = int(pan_percentile.group(1))

        can_percentile = re.search(r"(\d+)(?:st|nd|rd|th) percentile", text)
        if can_percentile:
            results["genomic_landscape_info"]["Cancer-specific percentile"] = int(can_percentile.group(1))

        if "Microsatellite Stable" in text:
            results["can_report_msi"] = True
            results["genomic_landscape_info"]["MSI status"] = "MSS"

        if "Homologous Recombination Proficiency" in text:
            results["can_report_hrd"] = True
            results["genomic_landscape_info"]["HRD status"] = "HRP"

    biomarker_table = soup.find("table", class_="variants")
    if biomarker_table:
        for row in biomarker_table.select("tr")[1:]:
            cells = [c.get_text(strip=True) for c in row.select("td")]
            if len(cells) >= 3:
                results["genomic_biomarkers"].append({
                    "biomarker": cells[0],
                    "call": cells[1],
                    "score_and_confidence": cells[2]
                })

    return {
        "plugin_name": "genomic_landscape",
        "version": "",
        "priorities": {},
        "attributes": [],
        "merge_inputs": {},
        "results": results,
        "url": ""
    }

@register_extractor("fusion")
def extract_fusion(soup: BeautifulSoup, schema: dict):
    results = {
        "rearranged_cancer_genes": None,
        "oncogenic_fusions_oncokb": None,
        "rearrangements_nccn": None
    }
    for p in soup.find_all("p"):
        strong = [s.get_text(strip=True) for s in p.find_all("strong")]
        if len(strong) >= 3:
            try:
                results["rearranged_cancer_genes"] = int(strong[0])
                results["oncogenic_fusions_oncokb"] = int(strong[1])
                results["rearrangements_nccn"] = int(strong[2])
            except ValueError:
                pass
    return {
        "plugin_name": "fusion",
        "version": "",
        "priorities": {},
        "attributes": [],
        "merge_inputs": {},
        "results": results,
        "url": ""
    }

# Supplement.body extractor
@register_extractor("supplement.body")
def extract_supplement_body(soup: BeautifulSoup, schema: dict):
    content = soup.find("div", class_="supplement-body") or soup.find("section", id="supplement")
    results = {"text": content.get_text(" ", strip=True)} if content else {}
    return {
        "plugin_name": "supplement.body",
        "version": "",
        "priorities": {},
        "attributes": [],
        "merge_inputs": {},
        "results": results,
        "url": ""
    }

# Default SNV/CNV extractors
@register_extractor("wgts.snv_indel")
def extract_snv_indel(soup: BeautifulSoup, schema: dict):
    return {
        "plugin_name": "wgts.snv_indel",
        "version": "",
        "priorities": {},
        "attributes": [],
        "merge_inputs": {},
        "results": {},
        "url": ""
    }

@register_extractor("wgts.cnv_purple")
def extract_cnv_purple(soup: BeautifulSoup, schema: dict):
    return {
        "plugin_name": "wgts.cnv_purple",
        "version": "",
        "priorities": {},
        "attributes": [],
        "merge_inputs": {},
        "results": {},
        "url": ""
    }

# HTML to JSON conversion
def html_to_json(html_file: str, schema_file: str = "schema_query.json") -> dict:
    soup = BeautifulSoup(Path(html_file).read_text(), "html.parser")
    schema = load_schema(schema_file)

    output = {
        "core": {},
        "plugins": {},
        "supplement.body": {}
    }

    # Core
    core_info = extract_core_info(soup)
    for field in schema["properties"]["core"]["properties"]:
        output["core"][field] = core_info.get(field, "")

    # Required plugins
    required_plugins = schema["properties"]["plugins"].get("required", [])
    for plugin_name in required_plugins:
        extractor = EXTRACTORS.get(plugin_name, gen_extractor)
        output["plugins"][plugin_name] = (
            extractor(plugin_name, soup, schema)
            if extractor is gen_extractor
            else extractor(soup, schema)
        )

    # Assay plugins (SNV/CNV)
    assay_plugins = ["wgts.cnv_purple", "wgts.snv_indel"]
    for plugin_name in assay_plugins:
        extractor = EXTRACTORS.get(plugin_name, gen_extractor)
        output["plugins"][plugin_name] = (
            extractor(plugin_name, soup, schema)
            if extractor is gen_extractor
            else extractor(soup, schema)
        )

    # Supplement body
    output["supplement.body"] = EXTRACTORS["supplement.body"](soup, schema)

    return output

# CLI
if len(sys.argv) < 2:
    raise RuntimeError("Usage: python3 html_to_json.py <report.html> [output.json]")

html_file = sys.argv[1]
output_file = sys.argv[2] if len(sys.argv) >= 3 else Path(html_file).with_suffix(".json").name

result = html_to_json(html_file)

with open(output_file, "w") as f:
    json.dump(result, f, indent=2)

print(f"Saved to {output_file}")
