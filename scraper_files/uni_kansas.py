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

u_name = "University of Kansas"
country = "United States"

def get_name(prof):
    name = prof.find('a').text.strip()
    return name

def get_email(prof):
    email_tag = prof.find('a', href=re.compile(r'^mailto:'))
    email = email_tag['href'] if email_tag else "N/A"
    return email

def get_link(prof):
    link_tag = prof.find('a')
    if link_tag:
        link = link_tag['href']
        if link.startswith("/"):
            link = "https://eecs.ku.edu" + link
        return link
    return "N/A"

def get_research(prof):
    research = prof.text if prof else ""
    return research

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_email = executor.submit(get_email, prof)
        future_research = executor.submit(get_research, prof)

        name = future_name.result()
        link = future_link.result()
        email = future_email.result()
        research = future_research.result()

    new_r = requests.get(link)

    research += new_r.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword or True:
        pers_link = prof.find('a', string=lambda x: "Website" in x).get('href') if prof.find('a', string=lambda x: "Website" in x) else get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def uni_kansas():
    url = "https://eecs.ku.edu/faculty"
    r = requests.get(url, verify=False)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('div', {'class': 'col-11 offset-2 col-sm-7 offset-sm-0 col-lg-6 offset-sm-1 pt-3 pt-sm-0'})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Kansas done...\n")
    return faculty_data


if __name__ == '__main__':
    uni_kansas()