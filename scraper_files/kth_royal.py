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

u_name = "KTH Royal Institute of Technology"
country = "Sweden"

def get_name(prof):
    last_name = prof.find('td', {'class': 'lastname'}).get_text()
    first_name = prof.find('td', {'class': 'firstname'}).find('a').get_text()
    full_name = first_name + " " + last_name
    return full_name

def get_link(prof):
    link = prof.find('td', {'class': 'firstname'}).find('a')['href']
    return link

def get_email(prof):
    email = prof.find('td', {'class': 'email'}).get_text()
    return email

def get_title(prof):
    title = prof.find('td', {'class': 'title'}).get_text()
    return title

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for each component
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_email = executor.submit(get_email, prof)
        future_title = executor.submit(get_title, prof)

        # Collect the results as they complete
        full_name = future_name.result()
        link = future_link.result()
        email = future_email.result()
        title = future_title.result()

    # if 'STUDENT' in title or 'student' in title:
    #     continue
    # else:
    #     print([full_name, email, link])

    new_r = requests.get(link)

    research = new_r.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    pers_link = get_scholar_profile(full_name)

    if found_keyword:
        faculty_data.append([u_name, country, full_name, email, link, pers_link])
        print([u_name, country, full_name, email, link, pers_link])

def kth_royal():
    url = "https://www.kth.se/cs/contact/we-work-at-the-department-of-computer-science-1.1028302"

    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    all_profs = soup.find_all('tr')[1:]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("KTH Royal Institute of Technology done...")
    print()
    return faculty_data


if __name__ == '__main__':
    kth_royal()