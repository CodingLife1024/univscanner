import requests
from bs4 import BeautifulSoup
import re
import google_scholar

u_name = "University of Wisconsin"
country = "USA"

def uni_wisconsin():
    url = "https://www.cs.wisc.edu/people/faculty/"

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    faculty_data = []

    keyword_list = [
        "operating system", "robotics", "kernel", "embedded system", "hardware",
        "computer architecture", "distributed system", "computer organization",
        "vlsi", "computer and system", "human-computer interaction", "human computer"
    ]

    faculty_tag = soup.find_all('h2', class_=None, id=None)

    for tag in faculty_tag:
        if tag.text != "Emeritus Faculty" and tag.text != "In Memoriam":
            all_faculty = tag.find_next('div', class_="faculty-list")
            faculty_list = all_faculty.find_all('div', class_="faculty-member")

            for faculty in faculty_list:
                name = faculty.find('h3').text.strip()
                link = faculty.find('a')['href']
                email_tag = faculty.find_all('a', href=True)

                email = "Email not found"
                for tag in email_tag:
                    if tag["href"].startswith("mailto:"):
                        email = tag["href"][7:]
                        break

                new_r = requests.get(link)

                found_keyword = any(re.search(re.escape(keyword), new_r.text, re.IGNORECASE) for keyword in keyword_list)

                if found_keyword:
                    print([u_name, country, name, email, link, google_scholar.get_scholar_profile(name)])
                    faculty_data.append([u_name, country, name, email, link, google_scholar.get_scholar_profile(name)])

    print()
    print("University of Wisconsin done....")
    print()
    return faculty_data


uni_wisconsin()