from bs4 import BeautifulSoup
import requests

url = "https://www.cst.cam.ac.uk/research/themes/systems-and-networking"

headers = {}
response = requests.get(url)
html_content = response.text

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all div elements
div_elements = soup.find_all('div')

for div_element in div_elements:
    # Find all <a> tags within the current div
    link_tags = div_element.find_all('a')

    for link_tag in link_tags:
        # Extract text and link URL
        text = div_element.get_text(strip=True)
        link_url = link_tag.get('href')

        # Print text and link URL
        print("Text:", text)
        print("Link URL:", link_url)
        print()
