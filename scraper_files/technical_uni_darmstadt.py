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

u_name = "Technical University of Darmstadt"
country = "Germany"

def get_faculty_data(prof):
    columns = prof.find_all('td')
    name = columns[1].text.replace("Prof.", "").replace("Dr.", "").replace("Hon.", "").replace("‘in", "").strip()
    link = columns[1].find('a').get('href')

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    email = new_soup.find('span', class_="email").text.split("@")[0] + "@@cs.tu-darmstadt.de" if new_soup.find('span', class_="email") else "N/A"

    research = new_soup.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = new_soup.find('h3', string="Links").find_next('a')['href'] if new_soup.find('h3', string="Links") else get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def technical_uni_darmstadt():
    url = "https://www.informatik.tu-darmstadt.de/fb20/organisation_fb20/professuren_und_gruppenleitungen/index.en.jsp"

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0'}

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('tr', id=lambda x: x and x.startswith('contact_'))

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\n")


if __name__ == "__main__":
    technical_uni_darmstadt()