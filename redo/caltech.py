from bs4 import BeautifulSoup
import requests
import re

university = "Caltech"
country = "USA"

def caltech():
    url_1 = "https://www.eas.caltech.edu/people/faculty"
    url_2 = "https://www.cms.caltech.edu/people/faculty"

    response_1 = requests.get(url_1)
    response_2 = requests.get(url_2)
    html_content = response_1.text + response_2.text

    soup = BeautifulSoup(html_content, 'html.parser')

    faculty_data = []

    keywords = ["embedded systems", "operating systems", "robotics", "distributed systems", "kernel"]

    faculty_data = []

    extract_webpage = soup.find_all(class_='person-teaser__link', href=lambda href: href and href.startswith('/people/'))

    for element in extract_webpage:
        name = element.get_text().strip()  # Separate text content by newlines for better readability
        href = element.get('href')  # Get the href attribute value
        print("Name:", name)
        indiv_url = "https://www.cms.caltech.edu" + href
        print("URL:", indiv_url)
        new_response = requests.get(indiv_url)
        new_html_content = new_response.text
        new_soup = BeautifulSoup(new_html_content, 'html.parser')
        print()

caltech()