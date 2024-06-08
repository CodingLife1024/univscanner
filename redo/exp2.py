from bs4 import BeautifulSoup
import requests

# Fetch the HTML content directly
url = "https://www.cs.hku.hk/index.php/people/academic-staff/hubert"

response = requests.get(url)
html_content = response.text

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Get the prettified HTML content
prettified_html = soup.prettify()

# Print the prettified HTML content
print(prettified_html)

# Write the prettified HTML content to a file
with open("all_info.txt", "w", encoding="utf-8") as file:
    file.write(prettified_html)
