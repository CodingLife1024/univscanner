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

u_name = "Chulalongkorn Engineering University"
country = "Thailand"

def get_faculty_data(prof):
    cols = prof.find_all('td')
    name = cols[0].find_all('a', string=lambda s: s is not None and s.strip())[-1].text.replace("DR.", "").replace("Dr.", "").replace("Prof.", "").replace("PROF.", "").replace("ASST.", "").strip().title()
    link = "https://www.cp.eng.chula.ac.th" + cols[0].find_all('a', string=lambda s: s is not None and s.strip())[-1]['href']
    email = cols[2].find('a', href=re.compile(r"^mailto:"))['href'].replace("mailto:", "")
    research = cols[0].text
    pers_link = cols[1].find('a')['href'] if cols[1].find('a') else get_scholar_profile(name)

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def chula_engg():
    urls = ["https://www.cp.eng.chula.ac.th/en/about/faculty/"]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find('tbody').find_all('tr')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("Chulalongkorn Engineering University done...")
    print()

    return faculty_data

if __name__ == '__main__':
    chula_engg()