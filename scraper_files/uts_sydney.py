import requests
import sys
import os
import re
from bs4 import BeautifulSoup
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile

keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

faculty_data = []

u_name = "University of Technology Sydney"
country = "Australia"

def get_name(prof):
    name_tag = prof.find('a', href=True)
    name = name_tag.get_text().strip() if name_tag else None
    return name

def get_link(prof):
    name_tag = prof.find('a', href=True)
    link = name_tag['href'] if name_tag else None
    return link

def get_title(prof):
    title_tag = prof.find('td', class_=None, attrs={"data-label": ""}, string=True)
    title = title_tag.text.lower() if title_tag else ""
    return title

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for each component
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_title = executor.submit(get_title, prof)

        # Collect the results as they complete
        name = future_name.result()
        link = future_link.result()
        title = future_title.result()

    if "professor" in title or "lecturer" in title:
        name_parts = name.split(',')
        if len(name_parts) == 2:
            first_name, last_name = name_parts[1].strip(), name_parts[0].strip()
            email = f"{first_name.lower()}.{last_name.lower()}@uts.edu.au"
        else:
            email = f"{name_parts[0].strip().lower()}@uts.edu.au"

        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def uts_sydney():
    url = "https://www.uts.edu.au/about/faculty-engineering-and-information-technology/computer-science/school-computer-science-staff"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('tr')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("University of Technology Sydney done...")
    print()

    return faculty_data

if __name__ == "__main__":
    uts_sydney()
