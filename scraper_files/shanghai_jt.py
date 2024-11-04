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

u_name = "Shanghai Jiao Tong University"
country = "China"

def get_faculty_data(dept, departments):
    dept_name = dept.get_text().strip()
    if dept_name in departments:
        faculties = dept.find_next('div', class_='Faculty').find_all('li')
        for faculty in faculties:
            a = faculty.find('a')
            if a:
                name = a.get_text().strip()
                link = 'http://www.cs.sjtu.edu.cn/en/' + a.get('href')

                new_r = requests.get(link)
                new_soup = BeautifulSoup(new_r.text, "html.parser")

                email = new_soup.find('a', href=re.compile(r'mailto:')).get_text().strip() if new_soup.find('a', href=re.compile(r'mailto:')) else "Email not found"

                personal_website = get_scholar_profile(name)

                print([u_name, country, name, email, link, personal_website])
                faculty_data.append([u_name, country, name, email, link, personal_website])

def shanghai_jt():

    url = "http://www.cs.sjtu.edu.cn/en/Faculty.aspx"   # homepage url
    r = requests.get(url)                                        # request to url

    # getting the soup by parsing the html parsel to text to request r
    soup = BeautifulSoup(r.text, "html.parser")

    departments = ["Institute of Parallel and Distributed Computing",
                   "Institute of Intelligent Human-Computer Interaction",
                   "Institute of Computer Application",
                   "Institute of Computer Architecture"]

    depts = soup.find_all('p', class_='tc f14 fb red')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, dept, departments) for dept in depts]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nShanghai Jiao Tong University done...\n")
    return faculty_data


if __name__ == "__main__":
    shanghai_jt()