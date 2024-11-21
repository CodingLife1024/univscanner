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

u_name = "American University of Sharjah"
country = "United Arab Emirates"

def get_faculty_data(prof):
    name = prof.find_next('span').text.replace('Dr.', '').replace('Mr.', '').strip()
    link = prof.find('a')['href']

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    email = new_soup.find('a', href=re.compile(r'^mailto:')).text.strip() if new_soup.find('a', href=re.compile(r'^mailto:')) else "N/A"

    research = new_soup.text.strip()

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])


def american_uni_sharjah():
    urls = [
        "https://www.aus.edu/cen/department-of-computer-science-and-engineering/faculty",
        "https://www.aus.edu/cen/department-of-computer-science-and-engineering/faculty?page=1",
        "https://www.aus.edu/cen/department-of-computer-science-and-engineering/faculty?page=2",
        "https://www.aus.edu/cen/department-of-computer-science-and-engineering/faculty?page=3",
        "https://www.aus.edu/cen/department-of-computer-science-and-engineering/faculty?page=4",
        "https://www.aus.edu/cen/department-of-computer-science-and-engineering/faculty?page=5",
        "https://www.aus.edu/cen/department-of-computer-science-and-engineering/faculty?page=6",
        "https://www.aus.edu/cen/department-of-electrical-engineering",
        "https://www.aus.edu/cen/department-of-electrical-engineering?page=1",
        "https://www.aus.edu/cen/department-of-electrical-engineering?page=2",
        "https://www.aus.edu/cen/department-of-electrical-engineering?page=3",
        "https://www.aus.edu/cen/department-of-electrical-engineering?page=4",
        "https://www.aus.edu/cen/department-of-electrical-engineering?page=5",
    ]

    total_text = ""

    all_profs = []

    for url in urls:
        r = requests.get(url)
        print("Fetching URL..." + url + "\n")
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('div', {'class': 'views-field views-field-field-image-uri'})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nAmerican University of Sharjah done...\n")

    return faculty_data

if __name__ == '__main__':
    american_uni_sharjah()
