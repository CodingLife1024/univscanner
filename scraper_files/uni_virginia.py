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

u_name = "University of Virginia"
country = "United States"


def get_faculty_data(prof):
    name = prof.find('a', class_="contact_block_name_link").text.replace("\ufeff", "").strip()
    link = "https://engineering.virginia.edu" + prof.find('a', class_="contact_block_name_link")['href']
    research = prof.find('div', class_="people_list_item_body").text.strip()

    pers_link = prof.find('div', class_="people_list_item_links").find_all('a')[1]['href'] if len(prof.find('div', class_="people_list_item_links").find_all('a')) > 1 else get_scholar_profile(name)

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        new_r = requests.get(link)
        new_soup = BeautifulSoup(new_r.text, "html.parser")
        email = new_soup.find('a', href=re.compile(r"^mailto:")).text.strip()

        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def uni_virginia():
    urls = ["https://engineering.virginia.edu/department/computer-science/faculty",
            "https://engineering.virginia.edu/department/computer-science/faculty?page=1",
            "https://engineering.virginia.edu/department/computer-science/faculty?page=2",
            "https://engineering.virginia.edu/department/computer-science/faculty?page=3",
            "https://engineering.virginia.edu/department/computer-science/faculty?page=4",
            "https://engineering.virginia.edu/department/computer-science/faculty?page=5",
            "https://engineering.virginia.edu/department/computer-science/faculty?page=6",
            "https://engineering.virginia.edu/department/computer-science/faculty?page=7",
            "https://engineering.virginia.edu/department/computer-science/faculty?page=8"]


    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('li', {'class': 'people_list_row'})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Virginia done...\n")
    return faculty_data

if __name__ == '__main__':
    uni_virginia()

