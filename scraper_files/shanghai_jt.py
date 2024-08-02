from bs4 import BeautifulSoup
import requests
import re
from components.google_scholar import get_scholar_profile

u_name = "Shanghai Jiao Tong University"
country = "China"


def shanghai_jt():

    url = "http://www.cs.sjtu.edu.cn/en/Faculty.aspx"   # homepage url
    r = requests.get(url)                                        # request to url

    # getting the soup by parsing the html parsel to text to request r
    soup = BeautifulSoup(r.text, "html.parser")

    faculty_data = []

    departments = ["Institute of Parallel and Distributed Computing",
                   "Institute of Intelligent Human-Computer Interaction",
                   "Institute of Computer Application",
                   "Institute of Computer Architecture"]

    depts = soup.find_all('p', class_='tc f14 fb red')

    for dept in depts:
        dept_name = dept.get_text().strip()
        if dept_name in departments:
            faculties = dept.find_next('div', class_='Faculty').find_all('li')
            for faculty in faculties:
                a = faculty.find('a')
                if a:
                    name = a.get_text().strip()
                    link = 'http://www.cs.sjtu.edu.cn/en/' + a.get('href')
                    # print(name, link)

                    new_r = requests.get(link)
                    new_soup = BeautifulSoup(new_r.text, "html.parser")

                    email = new_soup.find('a', href=re.compile(r'mailto:')).get_text().strip() if new_soup.find('a', href=re.compile(r'mailto:')) else "Email not found"

                    personal_website = get_scholar_profile(name)

                    print([u_name, country, name, email, link, personal_website])
                    faculty_data.append([u_name, country, name, email, link, personal_website])

    print()
    print("Shanghai Jiao Tong University done....")
    print()
    return faculty_data
