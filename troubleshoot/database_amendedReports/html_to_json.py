# Usage:
# Run this in the directory where the html and querySchema are located
# $ module load djerba
# $ python3 html_to_json.py report.html report.json

import os
import sys
import re
import json
from time import strftime
from pathlib import Path
from bs4 import BeautifulSoup

# Load query schema
def load_schema(filename: str="schema_query.json") -> dict:
    """
    Load JSON schema outlining JSON report structure from current directory
    """
    schema_path = Path(filename)
    if not schema_path.exists():
        raise FileNotFoundError(f"Query schema file not found in current directory.")
    return json.loads(schema_path.read_text())

# Define plugins to be extracted
EXTRACTORS={}
def register_extractor(plugin_name):
    def wrapper(func):
        EXTRACTORS[plugin_name]=func
        return func
    return wrapper

# Plugin extractor for patternProperties (wgts, tar, etc)
def gen_extractor(plugin_name: str, soup: BeautifulSoup, schema: dict):
    plugin_schema=schema["properties"]["plugins"]["patternProperties"]["^[A-Za-z_.-]+$"]
    results_schema=plugin_schema["properties"]["results"]

    results ={}
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
    
    return{
        "plugin_name": plugin_name,
        "version": "",
        "priorities": {},
        "attributes": [],
        "merge_inputs": {},
        "results": results,
        "url": "" }

# Plugin extractor for defined plugins
def parse_info_table(block: BeautifulSoup) -> dict:
    """Searches for plugins based on <table class = "info">"""
    results={}
    for table in block.select("table.info"):
        for row in table.select("tr"):
            cells = [c.get_text(strip=True) for c in row.select("td")]
            if len(cells) < 2:
                continue
            x = 0
            while x < (len(cells)-1):
                label = cells[x]
                value = cells[x+1]
                if label.endswith(":"):
                    key = (label[:-1]
                           .strip()
                           .lower()
                           .replace(" ", "_")
                           .replace("/", "_")
                           .replace("(", "")
                           .replace(")", ""))
                    results[key] = value
                x+=2
    return results

def extract_blocks(soup: BeautifulSoup, component_name: str) -> BeautifulSoup:
    """Extracts information between DJERBA_COMPONENT_START and DJERBA_COMPONENT_END"""
    start = soup.find(lambda tag: tag.name == "span" and tag.has_attr("DJERBA_COMPONENT_START") and tag["DJERBA_COMPONENT_START"] == component_name)
    end   = soup.find(lambda tag: tag.name == "span" and tag.has_attr("DJERBA_COMPONENT_END") and tag["DJERBA_COMPONENT_END"] == component_name)

    if not start or not end:
        print(f"[WARN] Component '{component_name}' not found or empty")
        return BeautifulSoup("", "html.parser")
    
    html_parts=[]
    for temp in start.next_siblings:
        if temp == end:
            break
        html_parts.append(str(temp))
    
    return BeautifulSoup("".join(html_parts), "html.parser")

# Plugin-specific extraction
@register_extractor("case_overview")
def extract_case_overview(soup:BeautifulSoup, schema:dict):
    block = extract_blocks(soup, "case_overview")
    results = parse_info_table(block)

    return {
        "plugin_name": "case_overview",
        "version": "",
        "priorities": {},
        "attributes": [],
        "merge_inputs": {},
        "results": results,
        "url": "" }

@register_extractor("sample")
def extract_sample(soup:BeautifulSoup, schema:dict):
    block = extract_blocks(soup, "sample")
    results = parse_info_table(block)
    
    return {
        "plugin_name": "sample",
        "version": "",
        "priorities": {},
        "attributes": [],
        "merge_inputs": {},
        "results": results,
        "url": "" }

@register_extractor("genomic_landscape")
def extract_genomic_landscape(soup:BeautifulSoup, schema:dict):
    block = extract_blocks(soup, "genomic_landscape")

    results = {
        "genomic_landscape_info": {},
        "genomic_biomarkers": [],
        "can_report_hrd": False,
        "can_report_msi": False,
        "cant_report_hrd_reason": False,
        "ctDNA": {} }
    
    blurb = block.find("p")
    if blurb:
        text = blurb.get_text(" ", strip=True)

        #TMB
        tmb_value = re.search(r"Tumou?r Mutation Burden \(TMB\) was\s+([\d.]+)", text, re.I)
        if tmb_value:
            results["genomic_landscape_info"]["Tumour Mutation Burden"] = float(tmb_value.group(1))
        
        tmb_mutations = re.search(r"\((\d+)\s+mutations\)", text)
        if tmb_mutations:
            results["genomic_landscape_info"]["Total mutations"] = int(tmb_mutations.group(1))

        tmb_category = re.search(r"classified it as\s+([^.]+)\.", text)
        if tmb_category:
            results["genomic_landscape_info"]["TMB category"] = tmb_category.group(1).strip()
        
        pan_percentile = re.search(r"corresponds to the (\d+)(?:st|nd|rd|th) percentile of the pan-cancer cohort", text)
        if pan_percentile:
            results["genomic_landscape_info"]["Pan-cancer percentile"] = int(pan_percentile.group(1))
        
        can_percentile = re.search(r"placed the tumour in the (\d+)(?:st|nd|rd|th) percentile of the", text)
        if can_percentile:
            results["genomic_landscape_info"]["Cancer-specific percentile"] = int(can_percentile.group(1))
        
        #MSI
        if "Microsatellite Stable" in text:
            results["can_report_msi"] = True
            results["genomic_landscape_info"]["MSI status"] = "MSS"
        
        #HRD
        if "Homologous Recombination Proficiency" in text:
            results["can_report_hrd"] = True
            results["genomic_landscape_info"]["HRD status"] = "HRP"
        
    biomarker_table = block.find("table", class_="variants")
    biomarkers = []
    if biomarker_table:
        for row in biomarker_table.select("tr")[1:]:
            cells = [c.get_text(strip=True) for c in row.select("td")]
            if len(cells) >= 3:
                biomarkers.append({
                    "biomarker": cells[0],
                    "call": cells[1],
                    "score_and_confidence": cells[2]})
    results["genomic_biomarkers"] = biomarkers

    return {
        "plugin_name": "genomic_landscape",
        "version": "",
        "priorities": {},
        "attributes": [],
        "merge_inputs": {},
        "results": results,
        "url": "" }

@register_extractor("fusion")
def extract_fusion(soup:BeautifulSoup, schema:dict):
    block = extract_blocks(soup, "fusion")

    results ={
        "rearranged_cancer_genes": None,
        "oncogenic_fusions_oncokb": None,
        "rearrangements_nccn": None }
    
    blurb = block.find("p")
    if blurb:
        strong = [s.get_text(strip=True) for s in blurb.find_all("strong")]
        if len(strong) >= 3:
            try:
                results["rearranged_cancer_genes"] = int(strong[0])
            except ValueError:
                pass
            try:
                results["oncogenic_fusions_oncokb"] = int(strong[1])
            except ValueError:
                pass
            try:
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
        "url": "" }

# HTML to JSON Conversion
def html_to_json(html_file: str, schema_file: str = "schema_query.json") -> dict:
    soup=BeautifulSoup(Path(html_file).read_text(), "html.parser")
    schema=load_schema(schema_file)

    output={
        "core": {},
        "plugins": {},
        "supplement.body": {}
    }

    #Core
    for field in schema["properties"]["core"]["properties"]:
        output["core"][field] = ""

    #Plugins from Schema
    required_plugins = schema["properties"]["plugins"]["required"]

    for plugin_name in required_plugins:
        extractor = EXTRACTORS.get(plugin_name, gen_extractor)
        output["plugins"][plugin_name] = (
            extractor(plugin_name, soup, schema)
            if extractor is gen_extractor
            else extractor(soup, schema)
            )
    
    #Assay specific plugins (wgts, tar)
    assay_plugins = ["wgts.cnv_purple", "wgts.snv_indel"]
    for plugin_name in assay_plugins:
        extractor = EXTRACTORS.get(plugin_name, gen_extractor)
        output["plugins"][plugin_name] = (
            extractor(plugin_name, soup, schema)
            if extractor is gen_extractor
            else extractor(soup, schema)
        )
    
    #Supplement.body plugin
    output["supplement.body"] = {
        "plugin_name": "supplement.body",
        "version": "",
        "priorities": {},
        "attributes": [],
        "merge_inputs": {},
        "results": {},
        "url": "" }
    
    return output

# Output the file
if len(sys.argv) < 2:
    raise RuntimeError("Usage: python3 html_to_json.py <report.html> [output.json]")

html_file = sys.argv[1]

if len(sys.argv) >= 3:
    output_file = sys.argv[2]
else:
    output_file = Path(html_file).with_suffix(".json").name

result = html_to_json(html_file)

with open(output_file, "w") as f:
    json.dump(result, f, indent=2)

print(f"Saved to {output_file}")

