import requests
from bs4 import BeautifulSoup
import re
import redo.google_scholar

u_name = "University of Wisconsin"
country = "USA"

def uni_wisconsin():
    url = "https://www.cs.wisc.edu/people/faculty/"
    faculty_data = []

    try:
        r = requests.get(url)
        r.raise_for_status()  # Raise an HTTPError for bad responses

        soup = BeautifulSoup(r.text, "html.parser")

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

                    try:
                        new_r = requests.get(link)
                        new_r.raise_for_status()  # Raise an HTTPError for bad responses

                        found_keyword = any(re.search(re.escape(keyword), new_r.text, re.IGNORECASE) for keyword in keyword_list)

                        if found_keyword:
                            scholar_profile = google_scholar.get_scholar_profile(name)
                            print([u_name, country, name, email, link, scholar_profile])
                            faculty_data.append([u_name, country, name, email, link, scholar_profile])

                    except requests.exceptions.RequestException as e:
                        print(f"Error fetching details for {name}: {e}")
                        continue

    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")

    print()
    print("University of Wisconsin done....")
    print()
    return faculty_data

uni_wisconsin()
