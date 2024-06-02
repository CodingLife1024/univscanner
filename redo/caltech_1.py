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

    names = soup.find_all("li", class_=['person-list__names-only__person'])

    faculty_data = []

    keywords = ["embedded systems", "operating systems", "robotics", "distributed systems", "kernel"]

    for i in names:
        print("Name:", i.get_text().strip())
        print("URL:", i.find('a').get('href'))

        indiv_url = "https://www.cms.caltech.edu" + i.find('a').get('href')


caltech()