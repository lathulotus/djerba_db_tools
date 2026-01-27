# Ticket: 
# Converting HTMLs to JSON (only amended fields)
    # 1. Load original JSON & amended HTML
    # 2. Parce HTML for changes and extract those fields
    # 3. Patch JSON with extracted fields (-> CouchDB)


import os
import json
import sys
from time import strftime
#pip install beautifulsoup4
from bs4 import BeautifulSoup

# Extract text from HTML
def extract_html(html_file):
    """
    Extract text from amended HTML file
    - HTML (amended report) -> string (HTML as text)
    """
    with open(html_file, "r") as file:
        soup = bs4.BeautifulSoup(file, "html.parser")
    
    text = soup.get_text(separator=" ", strip=True)
    return text
