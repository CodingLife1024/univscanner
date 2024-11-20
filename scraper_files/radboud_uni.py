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

u_name = "Radboud University"
country = "Netherlands"

def get_name(prof):
    name = prof.find('a', class_="link link--icon link--arrow-small link--icon-posafter").text.replace("\n", "").replace("Prof.", "").replace("Dr.", "").replace("Dr", "").replace("Prof", "").strip()
    name_parts = name.split("(")
    formatted_name = name_parts[1][:-1] + " " + name_parts[0][2:]
    name = formatted_name
    return name

def get_link(prof):
    link = "https://www.ru.nl" + prof.find('a', class_="link link--icon link--arrow-small link--icon-posafter")["href"]
    return link

def get_email(prof):
    email = prof.find('span', class_="spamspan").text.strip().replace("[at]", "@").replace(" ", "")
    return email

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_email = executor.submit(get_email, prof)

        name = future_name.result()
        link = future_link.result()
        email = future_email.result()

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, 'html.parser')

    research = new_soup.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def radboud_uni():
    urls = ["https://www.ru.nl/en/search/scope/staff/staff-department/858/staff-staff/professors/staff-staff/teachers",
            "https://www.ru.nl/en/search/scope/staff/staff-department/858/staff-staff/professors/staff-staff/teachers?page=1",
            "https://www.ru.nl/en/search/scope/staff/staff-department/858/staff-staff/professors/staff-staff/teachers?page=1"]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, 'html.parser')

    all_profs = soup.find_all("span", class_="field-content")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nRadboud University done...\n")
    return faculty_data

if __name__ == "__main__":
    radboud_uni()