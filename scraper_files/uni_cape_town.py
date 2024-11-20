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

u_name = "University of Cape Town"
country = "South Africa"

def get_faculty_data(prof, headers):
    name = prof.find('h1').text.strip() if prof.find('h1') else "N/A"
    pers_link = prof.find('a', string="Website")['href'] if prof.find('a', string="Website") else prof.find('a', string=lambda x: x in ["ResearchGate profile", "Google Scholar profile"])['href']
    email = prof.find('a', href=re.compile(r'^mailto:')).text.strip() if prof.find('a', href=re.compile(r'^mailto:')) else "N/A"
    link = "https://sit.uct.ac.za" + prof.find('article')['about'] if prof.find('article') else "N/A"

    new_r = requests.get(pers_link, headers=headers)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    research = new_soup.find.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])


def uni_cape_town():
    urls = [
        "https://sit.uct.ac.za/information-systems-staff",
        "https://sit.uct.ac.za/computer-science-staff"
    ]

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0'}

    total_text = ""

    for url in urls:
        r = requests.get(url, headers=headers)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('div', {'class': 'views-row'})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof, headers) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Cape Town done...\n")
    return faculty_data


if __name__ == '__main__':
    uni_cape_town()