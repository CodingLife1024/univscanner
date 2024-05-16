from bs4 import BeautifulSoup
import requests

# Fetch the HTML content directly
url = "https://www.eecs.mit.edu/role/faculty/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'
}
response = requests.get(url, headers=headers)
html_content = response.text

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract and print only the text of the page
text_content = soup.get_text()
print(text_content)
