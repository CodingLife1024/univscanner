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

u_name = "University of Queensland"
country = "Australia"

def get_faculty_data(prof, titles):
    name = prof.find('a').text.replace("Professor", "").replace("Ms", "").replace("Associate", "").strip()
    for title in titles:
        if name.startswith(title):
            name = name[len(title):]
    link = "https://eecs.uq.edu.au" + prof.find('a')['href']
    # print(name, link)

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.content, 'html.parser')

    email = new_soup.find('div', class_="field-name-field-uq-profile-email").text.strip()
    # print(email)
    personal_website = new_soup.find('a', string="View researcher profile").get('href') if new_soup.find('a', string="View researcher profile") else get_scholar_profile(name)
    # print(personal_website)

    research = new_soup.find('div', class_="field-name-field-uq-profile-researcher-bio").text.strip() if new_soup.find('div', class_="field-name-field-uq-profile-researcher-bio") else ""

    found_keyword = any(re.search(keyword, research.lower(), re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        curr = [u_name, country, name, email, link, personal_website]
        if curr not in faculty_data:
            print([u_name, country, name, email, link, personal_website])
            faculty_data.append([u_name, country, name, email, link, personal_website])

def uni_queensland():
    url = "https://eecs.uq.edu.au/about/our-people"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    headings = soup.find_all('h3', class_=None)

    titles = ["Dr ", "Miss ", "prof ", "Associate prof ", "Mrs ", "Mr "]

    for heading in headings:
        # print(heading.text.strip())
        heading_text = heading.text.strip()

        if heading_text not in ["Research staff", "Professional staff", "Honorary, adjunct, emeritus staff", "Cyber security and software engineering team", "Data science team", "Engineering and Technical Support Group", "UQ Cyber Security"]:

            professor_list = heading.find_next('ul', class_="vertical-list vertical-list--ruled")

            if professor_list:
                all_profs = professor_list.find_all('div', class_="person--teaser")

                with concurrent.futures.ThreadPoolExecutor() as executor:
                    futures = [executor.submit(get_faculty_data, prof, titles) for prof in all_profs]
                    for future in concurrent.futures.as_completed(futures):
                        try:
                            future.result()
                        except Exception as e:
                            print(f"Error occurred: {e}")

    print("\nUniversity of Queensland done...\n")
    return faculty_data


if __name__ == "__main__":
    uni_queensland()