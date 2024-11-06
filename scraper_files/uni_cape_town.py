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

def get_faculty_data(prof):
    name = prof.find('h1', class_='contact--fullname').text.strip() if prof.find('h1', class_='contact--fullname') else "N/A"
    print(name)
    link = "https://sit.uct.ac.za" + prof.find('article')['about'] if prof.find('article') else "N/A"
    print(link)
    email = prof.find('a', href=re.compile(r"^mailto:")).text.strip() if prof.find('a', href=re.compile(r"^mailto:")) else "N/A"
    print(email)
    print("")

    try:
        new_r = requests.get(link)
        new_soup = BeautifulSoup(new_r.text, "html.parser")
        research = new_soup.find('div', class_="field--name-field-bio").text.strip()
        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)
        if found_keyword or True:
            pers_link = get_scholar_profile(name)
            faculty_data.append([u_name, country, name, email, link, pers_link])
            print([u_name, country, name, email, link, pers_link])
    except Exception as e:
        print(f"Error occurred: {e}")


def uni_cape_town():
    urls = ["https://sit.uct.ac.za/information-systems-staff",
            "https://sit.uct.ac.za/computer-science-staff"]

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0'}

    total_text = ""

    for url in urls:
        r = requests.get(url, headers=headers, verify=False)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('div', {'class': 'views-row'})

    print(all_profs[1])

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Cape Town done...\n")
    return faculty_data


if __name__ == '__main__':
    uni_cape_town()