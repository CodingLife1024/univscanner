from bs4 import BeautifulSoup
import requests
import re

university = "Caltech"
country = "USA"

def caltech():
    url = "https://www.cms.caltech.edu/people/faculty"

    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    faculty_data = []

    keywords = []

    faculty_data = []

    extract_webpage = soup.find_all(class_='person-teaser__link', href=lambda href: href and href.startswith('/people/'))

    for element in extract_webpage:
        name = element.get_text().strip()  # Separate text content by newlines for better readability
        href = element.get('href')  # Get the href attribute value
        print("Name:", name)
        indiv_url = "https://www.cms.caltech.edu" + href
        print("URL:", indiv_url)
        print()

caltech()