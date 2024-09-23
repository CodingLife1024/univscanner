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

u_name = "Hanyang University"
country = "South Korea"

def get_name(prof):
    name = prof.find('h3', class_="name").get_text().strip()
    return name

def get_link(prof):
    link = prof.find("a", class_="small_btn")['href'] if prof.find("a", class_="small_btn") else "N/A"
    return link

def get_email(prof):
    email = prof.find("a", href=re.compile(r"^mailto:")).get_text().strip() if prof.find("a", href=re.compile(r"^mailto:")) else "N/A"
    return email

def get_research(prof):
    research = prof.find("tfoot").find("td", class_="name_in").get_text().strip() if prof.find("tfoot") else "N/A"
    return research

def get_faculty_data(prof):
    name = prof.find('td', class_="or_name").get_text().strip()
    email = prof.find("a", href=re.compile(r"^mailto:")).get_text().strip() if prof.find("a", href=re.compile(r"^mailto:")) else "N/A"
    link = prof.find("a", class_="small_btn")['href'] if prof.find("a", class_="small_btn") else "N/A"
    research = prof.find("tfoot").find("td", class_="name_in").get_text().strip() if prof.find("tfoot") else "N/A"

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def hanyang_uni():
    urls = [
        "http://cse.hanyang.ac.kr/eng/department/member.php?page=1",
        "http://cse.hanyang.ac.kr/eng/department/member.php?page=2",
    ]

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    total_text = ""

    for url in urls:
        response = requests.get(url, headers=headers)
        total_text += response.text

    soup = BeautifulSoup(total_text, "html.parser")

        # Find all professor entries
    all_profs = soup.find_all("td", valign="top", align="left", class_="organ_list", scope="row")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("Hanyang University done...")
    print()
    return faculty_data

if __name__ == '__main__':
    hanyang_uni()