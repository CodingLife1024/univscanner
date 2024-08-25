import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures
import base64

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile

keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer", "system"]

u_name = "Technical University of Denmark"
country = "Denmark"

faculty_data = []

def get_name(prof):
    name = prof.find('h3').text
    return name

def get_link(prof):
    link = prof.find('a', class_="link person")['href']
    return link

def get_email(prof):
    email_tag = prof.find('a', class_="email")['data-md5'] if prof.find('a', class_="email") else None
    if email_tag:
        email = base64.b64decode(email_tag).decode('utf-8')[7:]
    else:
        email = "N/A"
    return email

def get_research(prof):
    research = prof.text
    return research

def get_position(prof):
    position = prof.find('span', class_="minor dimmed").text if prof.find('span', class_="minor dimmed") else "N/A"
    return position

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for each component
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_email = executor.submit(get_email, prof)
        future_position = executor.submit(get_position, prof)
        future_research = executor.submit(get_research, prof)

        # Collect the results as they complete
        name = future_name.result()
        link = future_link.result()
        email = future_email.result()
        position = future_position.result()
        research = future_research.result()

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)
    pers_link = get_scholar_profile(name)
    if (found_keyword and ("Professor" in position or "Researcher" in position)):
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def tud():
    urls = ["https://orbit.dtu.dk/en/organisations/department-of-applied-mathematics-and-computer-science/persons/? page=0",
            "https://orbit.dtu.dk/en/organisations/department-of-applied-mathematics-and-computer-science/persons/?page=1",
            "https://orbit.dtu.dk/en/organisations/department-of-applied-mathematics-and-computer-science/persons/?page=2",
            "https://orbit.dtu.dk/en/organisations/department-of-applied-mathematics-and-computer-science/persons/?page=3",
            "https://orbit.dtu.dk/en/organisations/department-of-applied-mathematics-and-computer-science/persons/?page=4",
            "https://orbit.dtu.dk/en/organisations/department-of-applied-mathematics-and-computer-science/persons/?page=5",
            "https://orbit.dtu.dk/en/organisations/department-of-applied-mathematics-and-computer-science/persons/?page=6",
            "https://orbit.dtu.dk/en/organisations/department-of-applied-mathematics-and-computer-science/persons/?page=7",
            "https://orbit.dtu.dk/en/organisations/department-of-applied-mathematics-and-computer-science/persons/?page=8",
            "https://orbit.dtu.dk/en/organisations/department-of-applied-mathematics-and-computer-science/persons/?page=9",
            "https://orbit.dtu.dk/en/organisations/department-of-applied-mathematics-and-computer-science/persons/?page=10"]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")
    all_profs = soup.find_all('div', {'class': "rendering rendering_person rendering_short rendering_person_short"})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("Technical University of Denmark done...")
    print()
    return(faculty_data)

if __name__ == '__main__':
    tud()