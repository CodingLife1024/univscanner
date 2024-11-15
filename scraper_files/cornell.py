import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile
from components.GLOBAL_VARIABLES import keyword_list

university_name = "Cornell University"
country = "United States"

faculty_data = []

def get_name(prof):
    name_tag = prof.find('h2', class_='person__name').find('a')
    name = name_tag.text.strip()
    link = name_tag['href']
    return name, link

def get_email(prof):
    email = prof.find('div', class_='person__email').text.strip() if prof.find('div', class_='person__email') else "N/A"
    return email

def get_pers_link(name):
    return get_scholar_profile(name)


def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_name = executor.submit(get_name, prof)
        future_email = executor.submit(get_email, prof)

        name, link = future_name.result()
        email = future_email.result()

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, 'html.parser')

    depts = new_soup.find_all('li', class_=None)

    departments = ['Computer Engineering', 'Computer Systems', 'Integrated Circuits', 'Systems and Networking']

    for dept in depts:
        dd = dept.text.strip()
        if dd in departments:
            pers_link = get_scholar_profile(name)
            faculty_data.append([university_name, country, name, email, link, pers_link])
            print([university_name, country, name, email, link, pers_link])


def cornell():
    # URL of the form submission (same as the homepage in this case)
    urls = [
        "https://www.engineering.cornell.edu/faculty-directory?letter=A",
        "https://www.engineering.cornell.edu/faculty-directory?letter=B",
        "https://www.engineering.cornell.edu/faculty-directory?letter=C",
        "https://www.engineering.cornell.edu/faculty-directory?letter=D",
        "https://www.engineering.cornell.edu/faculty-directory?letter=E",
        "https://www.engineering.cornell.edu/faculty-directory?letter=F",
        "https://www.engineering.cornell.edu/faculty-directory?letter=G",
        "https://www.engineering.cornell.edu/faculty-directory?letter=H",
        "https://www.engineering.cornell.edu/faculty-directory?letter=I",
        "https://www.engineering.cornell.edu/faculty-directory?letter=J",
        "https://www.engineering.cornell.edu/faculty-directory?letter=K",
        "https://www.engineering.cornell.edu/faculty-directory?letter=L",
        "https://www.engineering.cornell.edu/faculty-directory?letter=M",
        "https://www.engineering.cornell.edu/faculty-directory?letter=N",
        "https://www.engineering.cornell.edu/faculty-directory?letter=O",
        "https://www.engineering.cornell.edu/faculty-directory?letter=P",
        "https://www.engineering.cornell.edu/faculty-directory?letter=Q",
        "https://www.engineering.cornell.edu/faculty-directory?letter=R",
        "https://www.engineering.cornell.edu/faculty-directory?letter=S",
        "https://www.engineering.cornell.edu/faculty-directory?letter=T",
        "https://www.engineering.cornell.edu/faculty-directory?letter=U",
        "https://www.engineering.cornell.edu/faculty-directory?letter=V",
        "https://www.engineering.cornell.edu/faculty-directory?letter=W",
        "https://www.engineering.cornell.edu/faculty-directory?letter=X",
        "https://www.engineering.cornell.edu/faculty-directory?letter=Y",
        "https://www.engineering.cornell.edu/faculty-directory?letter=Z"
    ]

    full_text = ""

    for link in urls:
        response = requests.get(link)
        full_text += response.text

    soup = BeautifulSoup(full_text, 'html.parser')

    faculty_data = []
    all_profs = soup.find_all('div', class_='faculty-bio-all')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print('\nCornell University done...\n')
    faculty_data = list(set(faculty_data))
    return faculty_data

if __name__ == "__main__":
    cornell()