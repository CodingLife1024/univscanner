import requests
from bs4 import BeautifulSoup
import re

university = "Princeton"
country = "US"

def princeton():
    url = "https://www.cs.princeton.edu/people/faculty"   # homepage url
    r = requests.get(url)                                        # request to url

    # getting the soup by parsing the html parsel to text to request r
    soup = BeautifulSoup(r.text, "html.parser")

    d = soup.find_all('div', class_='person-details')

    keyword_list = ["operating system", "robotics", "kerrnel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

    faculty_data = []

    for prof in d:
        name = prof.find('a').get_text()
        link = "https://www.cs.princeton.edu" + prof.find('a')['href']
        pers_link = prof.find('a', class_='btn btn-xs btn-default')['href'] if prof.find('a', class_='btn btn-xs btn-default') else "Not Found"
        email = link[44:] + "@cs.princeton.edu"

        # print(f"Name: {name}, Link: {link}")
        # print(f"Personal Link: {pers_link}")
        # print(f"Email: {email}")

        new_r = requests.get(link)
        new_soup = BeautifulSoup(new_r.text, "html.parser")    # getting the soup of the prof's page

        pers_r = requests.get(pers_link)
        pers_soup = BeautifulSoup(pers_r.text, "html.parser") if pers_link != "Not Found" else None

        research_text = new_soup.text
        pers_text = pers_soup.text if pers_soup else None

        found_keyword = any(re.search(re.escape(keyword), research_text + pers_text) for keyword in keyword_list)

        if found_keyword:
            print([university, country, name, email, link, pers_link])
            faculty_data.append([university, country, name, email, link, pers_link])

        print()
        print("Princeton done...")
        print()
        return faculty_data

# princeton()