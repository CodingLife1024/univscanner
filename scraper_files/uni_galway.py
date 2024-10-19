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

u_name = "University of Galway"
country = "Ireland"

def get_name(prof):
    try:
        name = prof.find('a', href=True).text.replace("Dr. ", "").strip()
        return name
    except:
        return "Name not found"

def get_email(prof):
    try:
        email = prof.find('a', href=re.compile(r'^mailto:')).get_text().strip() if prof.find('a', href=re.compile(r'^mailto:')) else "N/A"
        return email
    except:
        return "Email not found"

def get_link(prof):
    try:
        link = prof.find('a', href=True).get('href')
        return link
    except:
        return "Link not found"

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_email = executor.submit(get_email, prof)

        name = future_name.result()
        link = future_link.result()
        email = future_email.result()

    pers_link = prof.find('a', string="Personal Web Page").find('a').get('href') if prof.find('a', string="Personal Web Page") else get_scholar_profile(name)

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    research = new_soup.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def uni_galway():
    urls = ["https://www.universityofgalway.ie/science-engineering/school-of-computer-science/people/academicstaff/"]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('div', {'class': 'person clearfix'})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Galway done...\n")
    return faculty_data


if __name__ == '__main__':
    uni_galway()