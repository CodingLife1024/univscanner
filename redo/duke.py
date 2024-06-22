import requests
from bs4 import BeautifulSoup
import google_scholar
import re
from requests.exceptions import RequestException, ChunkedEncodingError

u_name = "Duke University"
country = "USA"

def duke():
    url = "https://www.cs.duke.edu/people/faculty"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    faculty_data = []

    keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

    faculties = soup.find_all('div', {'class': 'grid__content'})

    for faculty in faculties:
        name_div = faculty.find('div', class_='h4')
        if name_div:
            name = name_div.text.strip()
            profile_link = name_div.find('a')['href'] if name_div.find('a') else None

        email_div = faculty.find('div', class_="views-field-field-email")
        email = email_div.text.strip() if email_div else "None"

        if email == "":
            email = "None"

        personal_page = "None"
        websites_field = faculty.find('div', class_='views-field-field-websites')
        if websites_field:
            field_content = websites_field.find('div', class_='field-content')
            if field_content:
                link = field_content.find('a')
                if link:
                    personal_page = link.get('href', "None")

        if personal_page == "" or personal_page == "None":
            personal_page = google_scholar.get_scholar_profile(name)

        if profile_link:
            new_r = requests.get(profile_link)
            new_soup = BeautifulSoup(new_r.text, "html.parser")

            overview = new_soup.find('div', class_='excerpt').text if new_soup.find('div', class_='excerpt') else new_r.text

            found_keyword = any(re.search(re.escape(keyword), overview.lower()) for keyword in keyword_list)

            if found_keyword:
                print([u_name, country, name, email, profile_link, personal_page])
                faculty_data.append([u_name, country, name, email, profile_link, personal_page])

        # print(u_name, country, name, email, profile_link, personal_page)
        # print(profile_link)
        # print()


    print()
    print("Duke University done ...")
    print()
    return faculty_data


duke()
