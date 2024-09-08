import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile

keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

faculty_data = []

u_name = "University of Waterloo"
country = "Canada"

def get_name(prof):
    name = prof.find('h2', class_="uw-contact__h2").get_text().strip() if prof.find('h2', class_="uw-contact__h2") else None
    return name

def get_link(prof):
    link = "https://cs.uwaterloo.ca" + prof.find('h2', class_="uw-contact__h2").find('a')['href'] if prof.find('h2', class_="uw-contact__h2") else None
    return link

def get_title(prof):
    title = prof.find('span', class_="uw-contact__position").get_text().strip() if prof.find('span', class_="uw-contact__position") else None
    return title

def get_email(prof):
    email_tag = prof.find('a', href=re.compile(r'^mailto:'))
    email = email_tag.get_text().strip() if email_tag else "N/A"
    return email

def get_pers_link(prof, name):
    pers_link_tag = prof.find('span', class_="uw-label", string="Link to personal webpage:")
    pers_link = pers_link_tag.find_next('a')['href'] if pers_link_tag else get_scholar_profile(name)
    return pers_link


def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for each component
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_title = executor.submit(get_title, prof)
        future_email = executor.submit(get_email, prof)

        # Collect the results as they complete
        name = future_name.result()
        link = future_link.result()
        title = future_title.result()
        email = future_email.result()

    # Skip certain titles
    if "student" in title.lower() or "emeritus" in title.lower():
        return

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    # Find research section if available
    research_section = new_soup.find('summary', class_="details__summary", string="Additional Information")
    research = research_section.find_next('div').get_text() if research_section else new_soup.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_pers_link(prof, name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])


def uni_waterloo():
    url = "https://cs.uwaterloo.ca/computer-science/contacts"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('div', class_="views-row")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("University of Waterloo done...")
    print()

    return faculty_data


if __name__ == '__main__':
    uni_waterloo()