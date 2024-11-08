import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures
import pprint

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile
from components.GLOBAL_VARIABLES import keyword_list

faculty_data = []

u_name = "University of California, San Diego"
country = "United States"

def get_faculty_data(prof):
    name = prof.find('strong').text.strip()
    link = "https://cse.ucsd.edu" + prof.find('a')['href']

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.content, 'html.parser')

    email = new_soup.find('a', href=re.compile(r'mailto:')).text.strip() if new_soup.find('a', href=re.compile(r'mailto:')) else None
    full_profile = new_soup.find('a', string="Full Profile")['href'] if new_soup.find('a', string="Full Profile") else link
    pers_website = new_soup.find('a', string="Website")['href'] if new_soup.find('a', string="Website") else get_scholar_profile(name)

    print([u_name, country, name, email, full_profile, pers_website])
    faculty_data.append([u_name, country, name, email, full_profile, pers_website])

def uc_san_diego():
    urls = ["https://cse.ucsd.edu/people/faculty-profiles/faculty",
             "https://cse.ucsd.edu/people/faculty-profiles/continuing-lecturer",
             "https://cse.ucsd.edu/people/faculty-profiles/adjunct-faculty",
             "https://cse.ucsd.edu/people/faculty-profiles/continuing-lecturer"
             "https://cse.ucsd.edu/people/faculty-profiles/researcher"]

    all_profs = []

    for url in urls:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        all_profs += soup.find_all('div', class_='col-xs-6 col-sm-6 col-md-4 col-lg-3')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")


    print("\nUniversity of California, San Diego done...\n")
    return faculty_data


if __name__ == "__main__":
    uc_san_diego()
