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

u_name = "Queensland University of Technology"
country = "Australia"

def get_name(prof):
    name = prof.find('a').text.replace("Dr", "").strip()
    return name

def get_link(prof):
    link = prof.find('a')['href']
    return link

def get_title(prof):
    title = prof.find('dd', class_="col-xs-12 font-stack-headings-small").text.strip().lower()
    return title

def get_research(prof):
    research = prof.find('dl').text.strip()
    return research

def get_email(prof):
    email = prof.find('a', href=re.compile(r"^mailto:")).text.strip()
    return email

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_title = executor.submit(get_title, prof)

        name = future_name.result()
        link = future_link.result()
        title = future_title.result()

    if ("professor" in title or "lecturer" in title) and "emerit" not in title:

        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_research = executor.submit(get_research, prof)
            future_email = executor.submit(get_email, prof)

            research = future_research.result()
            email = future_email.result()

        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

        if found_keyword:
            pers_link = get_scholar_profile(name)
            faculty_data.append([u_name, country, name, email, link, pers_link])
            print([u_name, country, name, email, link, pers_link])


def queensland_uni_tech():
    urls = ["https://www.qut.edu.au/about/our-people/academic-profiles/search?query=&profilename=&discipline=Electrical%20engineering&divfac=&school=&school_all=1",
            "https://www.qut.edu.au/about/our-people/academic-profiles/search?query=&profilename=&discipline=Electrical%20engineering&divfac=&school=&school_all=1&result_1066507_result_page=2",
            "https://www.qut.edu.au/about/our-people/academic-profiles/search?query=&profilename=&discipline=Electrical%20engineering&divfac=&school=&school_all=1&result_1066507_result_page=3",
            "https://www.qut.edu.au/about/our-people/academic-profiles/search?query=&profilename=&discipline=Electrical%20engineering&divfac=&school=&school_all=1&result_1066507_result_page=4",
            "https://www.qut.edu.au/about/our-people/academic-profiles/search?query=&profilename=&discipline=Distributed%20computing%20and%20systems%20software&divfac=&school=&school_all=1",
            "https://www.qut.edu.au/about/our-people/academic-profiles/search?query=&profilename=&discipline=Distributed%20computing%20and%20systems%20software&divfac=&school=&school_all=1&result_1066507_result_page=2",
            "https://www.qut.edu.au/about/our-people/academic-profiles/search?query=&profilename=&discipline=Software%20engineering&divfac=&school=&school_all=1",
            "https://www.qut.edu.au/about/our-people/academic-profiles/search?query=&profilename=&discipline=Software%20engineering&divfac=&school=&school_all=1&result_1066507_result_page=2"]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        print("Fetching URL... ", url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('div', class_="box-internal")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nQueensland University of Technology done...\n")
    return faculty_data

if __name__ == '__main__':
    queensland_uni_tech()