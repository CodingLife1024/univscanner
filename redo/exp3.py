from bs4 import BeautifulSoup
import requests

# Fetch the HTML content directly
url = "https://www.eecs.mit.edu/people/faculty"

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'
}

response = requests.get(url, headers=headers)
html_content = response.text

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all <a> tags with Name: a, Class: None, ID: None, and 'rel': ['bookmark']
extract_webpage = soup.find_all('a', class_=None, id=None, rel=['bookmark'])
extract_email = soup.find_all('a', class_=None, id=None, href=lambda href: href and href.startswith('mailto:'))
extract_research = soup.find_all('a', class_=None, id=None, href=lambda href: href and href.startswith('/people/?fwp_research'))

for element in extract_email:
    text_content = element.get_text(separator='\n')  # Separate text content by newlines for better readability
    href = element.get('href')  # Get the href attribute value
    print("Text Content:", text_content)
    print("Href:", href)
    print()  # Print an empty line for readability