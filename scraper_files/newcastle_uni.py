import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile

keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

faculty_data = []

u_name = "Newcastle University"
country = "United Kingdom"

def newcastle_uni():
    url = "https://www.ncl.ac.uk/computing/people/"
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('div', class_="relatedPerson")

    for prof in all_profs:
        name = prof.find('a').text().split()
        link = prof.find('a')['href']
        email = prof.find('a', class_="relatedPersonLink relatedPersonLinkMail")['href'][7:]

        print(name, link, email)


if __name__ == "__main__":
    newcastle_uni()
