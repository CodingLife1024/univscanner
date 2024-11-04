import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile
from components.GLOBAL_VARIABLES import keyword_list

faculty_data = []

university = "Edinburgh University"
country = "United Kingdom"

def get_faculty_data(prof, headers):
    a = prof.find('a')
    if a:
        name = a.text.strip()
        link = a.get('href')

        if link:
            new_r = requests.get(link, headers=headers)
            new_soup = BeautifulSoup(new_r.text, "html.parser")

            roles_and_positions = ""

            alls = new_soup.find('dl')
            if alls:
                for a in alls.find_all('dd'):
                    if a:
                        text = a.text.strip()
                        if text[-9:] == "ed.ac.uk>":
                            email = text[1:-1]
                        else:
                            roles_and_positions += text + ", "

            found_keyword = any(keyword.lower() in roles_and_positions.lower() for keyword in keyword_list)

            if found_keyword:
                last_dl = new_soup.find_all('dl')[-1]
                pers_url = None
                if last_dl:
                    a_tag = last_dl.find('a', string="Personal Page")
                    if a_tag:
                        pers_url = a_tag.get('href')
                    else:
                        pers_url = get_scholar_profile(name)

                    print([university, country, name, email, link, pers_url])
                    faculty_data.append([university, country, name, email, link, pers_url])


def edinburgh():
    url = "https://www.ed.ac.uk/informatics/people/academic"   # homepage url

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }

    r = requests.get(url, headers=headers)  # request to url

    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find('div', class_="inf-people").find_all('li')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof, headers) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nEdinburgh University done...\n")
    return faculty_data


if __name__ == "__main__":
    edinburgh()
