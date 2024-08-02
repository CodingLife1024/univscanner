from bs4 import BeautifulSoup
import requests

# Fetch the HTML content directly
url = "https://scholars.duke.edu/person/rongge"

response = requests.get(url)
html_content = response.text

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Get the prettified HTML content with a custom indent size
custom_indent_size = 4  # Specify your desired indent size here

prettified_html = soup.prettify()

# Print the prettified HTML content
print(prettified_html)

# Write the prettified HTML content to a file
with open("all_info.txt", "w", encoding="utf-8") as file:
    file.write(prettified_html)
