# Usage:
# python3 html_to_json_patch.py original.json amended.html [output.json]

import sys
import json
import re
from time import strftime
from pathlib import Path
from bs4 import BeautifulSoup


def load_schema(filename="schema_query.json"):
    path = Path(filename)
    if not path.exists():
        raise FileNotFoundError("schema_query.json not found")
    return json.loads(path.read_text())


EXTRACTORS = {}

def register_extractor(name):
    def wrap(func):
        EXTRACTORS[name] = func
        return func
    return wrap


def gen_extractor(name, soup, schema):
    props = schema["properties"]["plugins"].get("patternProperties", {})
    results_schema = (
        next(iter(props.values()))
        .get("properties", {})
        .get("results", {})
        if props else {}
    )

    results = {}
    for field, f in results_schema.get("properties", {}).items():
        t = f.get("type", "string")
        results[field] = "" if t == "string" else None

    return {
        "plugin_name": name,
        "version": "",
        "priorities": {},
        "attributes": [],
        "merge_inputs": {},
        "results": results,
        "url": ""
    }


def parse_labeled_info_tables(soup):
    sections = {}
    current = None

    for el in soup.find_all(["h3", "table"]):
        if el.name == "h3":
            current = el.get_text(strip=True).lower().replace(" ", "_")
            sections[current] = {}
        elif el.name == "table" and "info" in el.get("class", []) and current:
            for row in el.select("tr"):
                cells = [c.get_text(strip=True) for c in row.select("td")]
                if len(cells) != 2 or not cells[0].endswith(":"):
                    continue
                key = (
                    cells[0][:-1]
                    .lower()
                    .replace(" ", "_")
                    .replace("/", "_")
                    .replace("(", "")
                    .replace(")", "")
                )
                sections[current][key] = cells[1]

    return sections


def extract_core_info(soup):
    meta = soup.find("meta", attrs={"name": "author"})
    return {
        "author": meta.get("content", "") if meta else "",
        "document_config": "",
        "report_id": "",
        "core_version": "",
        "extract_time": strftime("%Y-%m-%dT%H:%M:%S")
    }


@register_extractor("case_overview")
def extract_case_overview(soup, schema):
    return {
        "plugin_name": "case_overview",
        "version": "",
        "priorities": {},
        "attributes": [],
        "merge_inputs": {},
        "results": parse_labeled_info_tables(soup).get("case_overview", {}),
        "url": ""
    }


@register_extractor("sample")
def extract_sample(soup, schema):
    return {
        "plugin_name": "sample",
        "version": "",
        "priorities": {},
        "attributes": [],
        "merge_inputs": {},
        "results": parse_labeled_info_tables(soup).get("sample", {}),
        "url": ""
    }


def html_to_json(html_file, schema_file="schema_query.json"):
    soup = BeautifulSoup(Path(html_file).read_text(), "html.parser")
    schema = load_schema(schema_file)

    out = {"core": {}, "plugins": {}}

    core = extract_core_info(soup)
    for k in schema["properties"]["core"]["properties"]:
        out["core"][k] = core.get(k, "")

    required = schema["properties"]["plugins"].get("required", [])
    for name in required:
        extractor = EXTRACTORS.get(name, gen_extractor)
        out["plugins"][name] = (
            extractor(name, soup, schema)
            if extractor is gen_extractor
            else extractor(soup, schema)
        )

    return out


def merge_results(original, amended):
    merged = json.loads(json.dumps(original))

    for name, plugin in amended.get("plugins", {}).items():
        if name not in merged.get("plugins", {}):
            continue
        orig = merged["plugins"][name]
        for k, v in plugin.get("results", {}).items():
            if v not in ("", None, [], {}):
                orig["results"][k] = v

    return merged


if len(sys.argv) < 3:
    raise RuntimeError(
        "Usage: python3 amend_json_from_html.py <original.json> <amended.html> [output.json]"
    )

orig_json = json.loads(Path(sys.argv[1]).read_text())
amended_html = sys.argv[2]

amended_extracted = html_to_json(amended_html)
amended = merge_results(orig_json, amended_extracted)

out = (
    sys.argv[3]
    if len(sys.argv) > 3
    else Path(sys.argv[1]).with_name(
        Path(sys.argv[1]).stem + "_amended.json"
    )
)

Path(out).write_text(json.dumps(amended, indent=2))
print(f"Saved to {out}")
