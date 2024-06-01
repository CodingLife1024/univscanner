from bs4 import BeautifulSoup
import requests

# Fetch the HTML content directly
url = "https://seas.harvard.edu/computer-science/faculty-research"

response = requests.get(url)
html_content = response.text

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract and print only the text of the page
text_content = soup.get_text()
print(text_content)
print(text_content.parent() if text_content.parent() else "No parent found")
