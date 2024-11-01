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

u_name = "Indian Institute of Technology, Kanpur (IIT Kanpur)"
country = "India"

def get_faculty_data_1(prof):
    link = prof['href']
    name = prof.find('h5').text.strip()
    email = prof.find('h6').text.strip()[1:-1] + '@cse.iitk.ac.in'

    pers_link = get_scholar_profile(name)

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    research = new_soup.text.strip()

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def get_faculty_data_2(prof):
    link = prof.find('a')['href'].replace("/ee/../", "https://www.iitk.ac.in/")
    name = prof.find('a').text.strip()

    email = prof.find('a', string=re.compile(r'@')).text.strip() if prof.find('a', string=re.compile(r'@')) else "N/A"

    pers_link = prof.find('a', string="Home Page")['href'] if prof.find('a', string="Home Page") else get_scholar_profile(name)

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    research = new_soup.text.strip()

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def iit_kanpur():
    urls = [
        "https://www.cse.iitk.ac.in/pages/Faculty.html",
        "https://www.iitk.ac.in/ee/control-and-automation-faculty",
        "https://www.iitk.ac.in/ee/microelectronics-and-vlsi-faculty",
        "https://www.iitk.ac.in/ee/photonics-faculty",
        "https://www.iitk.ac.in/ee/power-engineering-faculty",
        "https://www.iitk.ac.in/ee/signal-processing-communications-networks-faculty",
        "https://www.iitk.ac.in/ee/rf-and-microwave-faculty",
    ]

    # for url 1

    r = requests.get(urls[0])
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find('ul', class_="fa-ul").find_all('a')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data_1, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    # for url 2 to 7

    total_text = ""

    for url in urls[1:]:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('div', {'class': 'col-md-6 border-bottom mb-3'})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data_2, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nIndian Institute of Technology, Kanpur (IIT Kanpur) done...\n")
    return faculty_data


if __name__ == '__main__':
    iit_kanpur()
    pprint.pprint(faculty_data)

