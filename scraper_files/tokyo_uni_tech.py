import requests
import re
from bs4 import BeautifulSoup
from components.google_scholar import get_scholar_profile

u_name = "Tokyo University of Technology"
country = "Japan"

def tokyo_uni_tech():
    url = "http://www.cs.titech.ac.jp/people-e.html"

    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")

    keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction"]

    faculty_data = []

    dd = soup.find('div', {'class':'section'})
    d = dd.find_all('tr')

    #iterating for every prof
    for i in d:
        a = i.find('a')
        if a == None:
            continue
        name = (a.get_text()).strip()
        link = a.get('href')
        # check if link is valid on Not
        cells = i.find_all('td')
        email = cells[3].text.strip() + "titech.ac.jp" if len(cells) > 3 else "Not Found"

        if link:
            new_r = requests.get(link)
            research_text = new_r.text

            new_soup = BeautifulSoup(research_text, "html.parser")

            found_keyword = any(re.search(re.escape(keyword), research_text.lower()) for keyword in keyword_list)

            if found_keyword:
                pers_page = new_soup.find('a', string='Personal page') if research_text else get_scholar_profile(name.lower())

                print([u_name, country, name, email, link, pers_page])
                faculty_data.append([u_name, country, name, email, link, pers_page])

    print()
    print("Tokyo University of Technology done....")
    print()
    return faculty_data