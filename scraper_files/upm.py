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

u_name = "University Putra Malaysia"
country = "Malaysia"

def get_name(prof):
    name_tag = prof.find('a', href=True)
    name = name_tag.get_text().replace("Prof.", "").replace("Dr.", "").replace("Ts.", "").replace("Assoc.", "").replace("Gs.", "").replace("Ir.", "").strip() if name_tag else None
    return name

def get_link(prof):
    name_tag = prof.find('a', href=True)
    link = name_tag['href'] if name_tag else None
    return link

def get_research(prof):
    research = prof.text
    return research

def get_email(prof):
    email_tag = prof.find('a', href=re.compile(r"mailto:"))['href'][7:] if prof.find('a', href=re.compile(r"mailto:")) else False
    if email_tag == False:
        full_text = prof.text
        email = full_text.split("Mail :")[1].strip().split("@")[0] + "@@upm.edu.my"
        return email
    return email_tag

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for each component
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_research = executor.submit(get_research, prof)
        future_email = executor.submit(get_email, prof)

        # Collect the results as they complete
        name = future_name.result()
        link = future_link.result()
        research = future_research.result()
        email = future_email.result()

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, 'html.parser')
    research += new_soup.text

    # Check if any keyword matches the research area
    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        # Extract the resume/profile link
        resume_tag = prof.find('a', href=True, string="Profile")
        resume_link = "https://eng.upm.edu.my" + resume_tag['href'] if resume_tag else None

        # Extract the ORCID link
        orcid_tag = prof.find('a', href=re.compile(r"orcid.org"))
        orcid_link = orcid_tag['href'] if orcid_tag else None

        # Determine the personal link to be used
        pers_link = resume_link or orcid_link or get_scholar_profile(name)

        # Append the collected data
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def upm():
    url = "https://eng.upm.edu.my/department/department_of_computer_and_communication_systems_engineering/academic_staff-1897"

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}

    r = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(r.text, 'html.parser')

    all_profs = soup.find_all('td', style='background-color: #ffffff; vertical-align: top; width: 1550px; height: 168px;')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")


    print("\nUniversity Putra Malaysia done...\n")
    return faculty_data

if __name__ == '__main__':
    upm()