from bs4 import BeautifulSoup
import requests

# Fetch the HTML content directly
url = "https://www.sheffield.ac.uk/cs/people/academic"

response = requests.get(url)
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
