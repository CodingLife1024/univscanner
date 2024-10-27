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

u_name = "Universidad Carlos III de Madrid"
country = "Spain"

def get_faculty_data(prof, headers):
    name = prof.find('a').text.strip()
    link = prof.find('a')['href']

    if not link.startswith("http"):
        link = "https://researchportal.uc3m.es" + link

    new_r = requests.get(link, headers=headers)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    email = new_soup.find('a', href=re.compile(r'^mailto:')).text.strip() if new_soup.find('a', href=re.compile(r'^mailto:')) else "N/A"

    research = new_soup.text.strip()

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def universidad_carlos_de_madrid():
    urls = [
        "https://www.uc3m.es/ss/Satellite/Doctorado/en/Detalle/Estudio_C/1422576090112/1371210298470/Computer_Science_and_Technology#faculty_faculty",
        "https://www.uc3m.es/phdprogram/electrical-engineering-electronics-automation#faculty",
        "https://www.uc3m.es/ss/Satellite/Doctorado/en/Detalle/Estudio_C/1371323806437/1371210298470/Signal_Processing_and_Communications_Engineering#faculty_faculty"
    ]

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0'}

    all_profs = []

    for url in urls:
        r = requests.get(url, headers=headers, verify=False)
        soup = BeautifulSoup(r.text, "html.parser")

        super_class = soup.find_all('div', {'class': 'row contenidoPestanaInner'})[:2]

        for i in super_class:
            profs = i.find_all('li')
            all_profs.extend(profs)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof, headers) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversidad Carlos III de Madrid done...\n")
    return faculty_data


if __name__ == '__main__':
    universidad_carlos_de_madrid()