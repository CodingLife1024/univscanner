import requests
from bs4 import BeautifulSoup
import re
import google_scholar

u_name = "University of Queensland"
country = "Australia"

def uni_queensland():
    url = "https://eecs.uq.edu.au/about/our-people"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    faculty_data = []

    keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

    headings = soup.find_all('h3', class_=None)

    titles = ["Dr ", "Miss ", "Professor ", "Associate Professor ", "Mrs ", "Mr "]

    for heading in headings:
        # print(heading.text.strip())
        heading_text = heading.text.strip()

        if heading_text not in ["Research staff", "Professional staff", "Honorary, adjunct, emeritus staff", "Cyber security and software engineering team", "Data science team", "Engineering and Technical Support Group", "UQ Cyber Security"]:

            professor_list = heading.find_next('ul', class_="vertical-list vertical-list--ruled")

            if professor_list:
                professors = professor_list.find_all('div', class_="person--teaser")

                for professor in professors:
                    name = professor.find('a').text.strip()
                    for title in titles:
                        if name.startswith(title):
                            name = name[len(title):]
                    link = "https://eecs.uq.edu.au" + professor.find('a')['href']
                    # print(name, link)

                    new_r = requests.get(link)
                    new_soup = BeautifulSoup(new_r.content, 'html.parser')

                    email = new_soup.find('div', class_="field-name-field-uq-profile-email").text.strip()
                    # print(email)
                    personal_website = new_soup.find('a', string="View researcher profile").get('href') if new_soup.find('a', string="View researcher profile") else google_scholar.get_scholar_profile(name)
                    # print(personal_website)

                    research = new_soup.find('div', class_="field-name-field-uq-profile-researcher-bio").text.strip() if new_soup.find('div', class_="field-name-field-uq-profile-researcher-bio") else ""

                    found_keyword = any(re.search(keyword, research.lower(), re.IGNORECASE) for keyword in keyword_list)

                    if found_keyword:
                        curr = [u_name, country, name, email, link, personal_website]
                        if curr not in faculty_data:
                            print([u_name, country, name, email, link, personal_website])
                            faculty_data.append([u_name, country, name, email, link, personal_website])

    print()
    print("UQ done....")
    print()

# uni_queensland()
