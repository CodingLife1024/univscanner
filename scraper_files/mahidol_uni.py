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

u_name = "Mahidol University"
country = "Thailand"

def get_faculty_data(prof):
    name = prof.find('h3').text.strip()
    link = prof.find('a').get('href')
    email = prof.find('a', {'data-md5': True}).text.strip() if prof.find('a', {'data-md5': True}) else "N/A"
    pers_link = get_scholar_profile(name)

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    research = new_soup.text
    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def mahidol_uni():
    urls = ["https://mahidol.elsevierpure.com/en/organisations/faculty-of-information-and-communication-technology/persons/",
            "https://mahidol.elsevierpure.com/en/organisations/faculty-of-science/persons/",
            "https://mahidol.elsevierpure.com/en/organisations/faculty-of-science/persons/?page=1",
            "https://mahidol.elsevierpure.com/en/organisations/faculty-of-science/persons/?page=2",
            "https://mahidol.elsevierpure.com/en/organisations/faculty-of-science/persons/?page=3",
            "https://mahidol.elsevierpure.com/en/organisations/faculty-of-science/persons/?page=4",
            "https://mahidol.elsevierpure.com/en/organisations/faculty-of-science/persons/?page=5",
            "https://mahidol.elsevierpure.com/en/organisations/faculty-of-science/persons/?page=6",]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('div', {'class': 'result-container'})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nMahidol University done...\n")
    return faculty_data


if __name__ == "__main__":
    mahidol_uni()