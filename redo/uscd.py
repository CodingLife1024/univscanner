import requests
from bs4 import BeautifulSoup
import re
import google_scholar

u_name = "University of California San Diego"
country = "USA"


def ucsd():
    urls = ["https://cse.ucsd.edu/people/faculty-profiles/faculty",
             "https://cse.ucsd.edu/people/faculty-profiles/continuing-lecturer",
             "https://cse.ucsd.edu/people/faculty-profiles/adjunct-faculty",
             "https://cse.ucsd.edu/people/faculty-profiles/continuing-lecturer"
             "https://cse.ucsd.edu/people/faculty-profiles/researcher"]

    faculty_data = []

    keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

    for url in urls:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')

        faculty_entries = soup.find_all('div', class_='col-xs-6 col-sm-6 col-md-4 col-lg-3')

        for faculty_entry in faculty_entries:
            link = "https://cse.ucsd.edu" + faculty_entry.find('a')['href']
            name = faculty_entry.find('strong').text.strip()

            print(name, link)


ucsd()
