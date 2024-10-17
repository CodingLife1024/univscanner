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

u_name = "Tel Aviv University"
country = "Israel"

def get_name(prof):
    name = prof.find('div', class_='schoolStaffItemText').find('span').text.replace("Prof.", "").replace("Dr.", "").strip()
    return name

def get_email(prof):
    email = prof.find("strong", string=re.compile(r'^E-Mail')).find_parent('p').text.split(":")[1].strip()
    return email

def get_link(prof):
    link = "https://www.cs.mta.ac.il/" + prof.find("div", class_="schoolStaffItemText").find('a')['href'] if prof.find("div", class_="schoolStaffItemText").find('a') else "N/A"
    return link

def get_research(prof):
    research = prof.text
    return research

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_email = executor.submit(get_email, prof)
        future_research = executor.submit(get_research, prof)

        name = future_name.result()
        link = future_link.result()
        email = future_email.result()
        research = future_research.result()

    pers_link = prof.find('a', string='Personal site')['href'] if prof.find('a', string='Personal site') else get_scholar_profile(name)

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def telaviv_uni():
    urls = ["https://www.cs.mta.ac.il/staff_list_faculty"]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find('table').find_all('tr', id=True)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("Tel Aviv University done...")
    print()
    return faculty_data

if __name__ == '__main__':
    telaviv_uni()