import requests
from bs4 import BeautifulSoup
import sys
import os
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile

u_name = "University of Copenhagen"
country = "Denmark"

keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

faculty_data = []

def get_name(prof):
    return prof.find('td', class_="emplistname").text.strip() if prof.find('td', class_="emplistname") else None

def get_link(prof):
    return 'https://di.ku.dk/english/staff/vip/' + prof.find('td', class_="emplistname").find('a').get('href')

def get_post(prof):
    return prof.find('td', class_="emplisttitle").text.strip() if prof.find('td', class_="emplisttitle") else None

def get_email(prof):
    email_tag = prof.find('td', class_="emplistemail").find('a').get('onclick') if prof.find('td', class_="emplistemail").find('a') else None
    email_code = email_tag.replace("this.href=", "").replace("return true;", "").strip()
    return eval(email_code[:-1])[7:]

def get_research(link):
    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")
    research_elements = new_soup.find_all('h2', class_="title") if new_soup.find('h2', class_="title") else "None"

    full_research = "".join(element.text.strip() for element in research_elements)

    return full_research

def get_faculty_data(prof):
    # Use ThreadPoolExecutor to parallelize the tasks
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for name, link, and post
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_post = executor.submit(get_post, prof)

        # Get the results
        name = future_name.result()
        link = future_link.result()
        post = future_post.result()

        if post == "Professor":
            future_email = executor.submit(get_email, prof)
            future_research = executor.submit(get_research, link)

            email = future_email.result()
            full_research = future_research.result()

            found_keyword = any(re.search(re.escape(keyword), full_research, re.IGNORECASE) for keyword in keyword_list)

            if found_keyword:
                pers_link = get_scholar_profile(name)
                faculty_data.append([u_name, country, name, email, link, pers_link])
                print([u_name, country, name, email, link, pers_link])

def uni_copenhagen():
    url = "https://di.ku.dk/english/staff/vip/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    tbody = soup.find('tbody')
    all_profs = tbody.find_all('tr')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    return faculty_data

if __name__ == '__main__':
    uni_copenhagen()