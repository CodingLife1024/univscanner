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

u_name = "University of Gottingen"
country = "Germany"

def get_name(prof):
    name = prof.find('a').text.replace("Dr.", "").replace("Prof.", "").replace("Prof. Dr.", "").strip() if prof.find('a') else "N/A"
    return name

def get_link(prof):
    link = prof.find('a')['href'] if prof.find('a') else "N/A"
    return link

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)

        name = future_name.result()
        link = future_link.result()

    email = name.split(" ")[0] + "." + name.split(" ")[1] + "@cs.uni-goettingen.de"

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")
    research = new_soup.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def uni_gottingen():
    urls = ["https://www.uni-goettingen.de/en/628113.html"]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    super_class = soup.find_all('ul')[:-2]

    all_profs = []

    for i in super_class:
        all_profs.extend(i.find_all('li'))

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Gottingen done...\n")
    return faculty_data


if __name__ == '__main__':
    uni_gottingen()
