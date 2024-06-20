import requests
from bs4 import BeautifulSoup
import re
import json

def fetch_and_parse(url):
    # Fetch the HTML page
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract meta data
    meta_data = {meta['name']: meta['content'] for meta in soup.find_all("meta") if 'name' in meta.attrs and 'content' in meta.attrs}

    # Fetch JavaScript file
    js_url = "https://www.sydney.edu.au/engineering/about/our-people/academic-staff/xiu-wang.html//etc.clientlibs/corporate-commons/clientlibs/translation.15b6fc27cccbddb5fb7b88a7c6a2c7e4.js"
    js_response = requests.get(js_url)
    js_content = js_response.text

    # Extract JSON data from JavaScript content
    start_index = js_content.find('({')
    end_index = js_content.rfind('});')

    if start_index != -1 and end_index != -1:
        data_str = js_content[start_index:end_index + 2]
        try:
            js_data = json.loads(data_str)
        except json.JSONDecodeError:
            js_data = None
    else:
        js_data = None

    return meta_data, js_data

# Example usage
url = "https://www.sydney.edu.au/engineering/about/our-people/academic-staff/xiu-wang.html"
meta_data, js_data = fetch_and_parse(url)
print("Meta Data:", meta_data)
print("JavaScript Data:", js_data)
