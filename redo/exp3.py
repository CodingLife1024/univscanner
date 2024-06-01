from bs4 import BeautifulSoup
import requests

url = "https://seas.harvard.edu/person/stephanie-gil"

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'
}

response = requests.get(url)
html_content = response.text

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all <a> tags with Name: a, Class: None, ID: None, and 'rel': ['bookmark']
extract_webpage = soup.find_all('a', class_=['accordion-title'], id=None, href= '#')
for element in extract_webpage:
    text_content = element.get_text()  # Separate text content by newlines for better readability
    href = element.get('href')  # Get the href attribute value
    print("Text Content:", text_content)
    print("Href:", href)