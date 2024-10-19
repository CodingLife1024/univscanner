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

u_name = "University of Calgary"
country = "Canada"

def get_faculty_data(prof):
    columns = prof.find_all('td')
    name_parts = columns[0].text.strip().split(',')
    name = name_parts[1] + ' ' + name_parts[0]
    link = columns[0].find('a')['href']

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    email = new_soup.find('a', href=re.compile(r"^mailto:")).text.strip() if new_soup.find('a', href=re.compile(r"^mailto:")) else "N/A"
    research = new_soup.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = new_soup.find('p', string="Web presence").find_next('div').find('a')['href'] if new_soup.find('p', string="Web presence") else get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def uni_calgary():
    urls = ["https://science.ucalgary.ca/computer-science/contacts/faculty-members"]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    super_class = soup.find_all('tbody')[:-1]

    all_profs = []

    for i in super_class:
        all_profs += i.find_all('tr')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Calgary done...\n")
    return faculty_data

if __name__ == '__main__':
    uni_calgary()
