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

target_classes = []
target_names = ['a']

# Find all elements with the specified classes
elements_with_classes = soup.find_all(target_names, class_=target_classes)

# Extract and print the text content within each 'people-entry' class
for element in elements_with_classes:
    text_content = element.get_text(separator='\n')  # Separate text content by newlines for better readability
    print(text_content)