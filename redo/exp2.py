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

# Extract and print only the text of the page along with its parent details
with open("all_text.txt", "w", encoding="utf-8") as file:
    for element in soup.find_all(text=True):
        if element.parent.name and not element.parent.name.startswith('script') and element.strip() != "":
            parent = element.parent
            parent_name = parent.name
            parent_class = parent.get('class', None)
            parent_id = parent.get('id', None)
            parent_attrs = parent.attrs
            parent_details = f"Name: {parent_name}, Class: {parent_class}, ID: {parent_id}, Other Attributes: {parent_attrs}" if parent_attrs else f"Name: {parent_name}, Class: {parent_class}, ID: {parent_id}"

            print(f"Text: {element.strip()}")
            print(f"Parent Details: {parent_details}")
            print("-----------------")

            file.write(f"Text: {element.strip()}\n")
            file.write(f"Parent Details: {parent_details}\n\n")
            file.write("-----------------\n\n\n")