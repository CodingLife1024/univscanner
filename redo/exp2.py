from bs4 import BeautifulSoup
import requests

# Fetch the HTML content directly
url = "https://www.cst.cam.ac.uk/people/arb33"

headers = {}
response = requests.get(url)
html_content = response.text

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract and print text, parent details, and URLs of links
with open("all_info.txt", "w", encoding="utf-8") as file:
    for element in soup.find_all(text=True):
        if element.parent.name:
            parent = element.parent
            parent_name = parent.name
            parent_class = parent.get('class', None)
            parent_id = parent.get('id', None)
            parent_attrs = parent.attrs
            parent_details = f"Name: {parent_name}, Class: {parent_class}, ID: {parent_id}, Other Attributes: {parent_attrs}" if parent_attrs else f"Name: {parent_name}, Class: {parent_class}, ID: {parent_id}"

            if parent.name == 'a' and parent.get('href'):
                parent_details += f", URL: {parent['href']}"

            print(f"Text: {element.strip()}")
            print(f"Parent Details: {parent_details}")
            print("-----------------")

            file.write(f"Text: {element.strip()}\n")
            file.write(f"Parent Details: {parent_details}\n\n")
            file.write("-----------------\n\n")
