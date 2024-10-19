from bs4 import BeautifulSoup
import requests

# Fetch the HTML content directly
url = "https://www.uantwerpen.be/nl/personeel/?q=UA324"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0'}

response = requests.get(url, verify=False, headers=headers)
html_content = response.text

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Get the prettified HTML content
prettified_html = soup.prettify()

# Manually add custom indentation size
custom_indent_size = 4  # Specify your desired indent size here
indented_html = '\n'.join(' ' * custom_indent_size + line for line in prettified_html.splitlines())

# Print the indented HTML content
print(indented_html)

# Write the indented HTML content to a file
with open("all_info.txt", "w", encoding="utf-8") as file:
    file.write(indented_html)
