import requests
from bs4 import BeautifulSoup
import re
from components.google_scholar import get_scholar_profile

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
            name = faculty_entry.find('strong').text.strip()
            link = "https://cse.ucsd.edu" + faculty_entry.find('a')['href']

            new_r = requests.get(link)
            new_soup = BeautifulSoup(new_r.content, 'html.parser')

            email = new_soup.find('a', href=re.compile(r'mailto:')).text.strip() if new_soup.find('a', href=re.compile(r'mailto:')) else None
            full_profile = new_soup.find('a', string="Full Profile")['href'] if new_soup.find('a', string="Full Profile") else link
            pers_website = new_soup.find('a', string="Website")['href'] if new_soup.find('a', string="Website") else get_scholar_profile(name)

            print([u_name, country, name, email, full_profile, pers_website])
            faculty_data.append([u_name, country, name, email, full_profile, pers_website])

    print()
    print("USCD done....")
    print()
    return faculty_data


# ucsd()
