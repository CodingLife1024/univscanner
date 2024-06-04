from bs4 import BeautifulSoup
import requests
import re

university = "Tsinghua University"
country = "China"

def tsinghua():
    url = "https://www.cs.tsinghua.edu.cn/csen/Faculty/Full_time_Faculty.htm"

    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    faculty_data = []

    # Find all divs with class 'card card--person'
    faculty_cards = soup.find_all('div', class_='text')

    keyword_list = ["operating system", "robotics", "kerrnel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

    for faculty in faculty_cards:
        name = faculty.find('a').text
        site = "https://www.cs.tsinghua.edu.cn/csen" + faculty.find('a')['href'][2:]
        email = faculty.find_all('p')[2].text

        # print(name)
        # print(site)
        # print(email)

        new_r = requests.get(site)
        new_soup = BeautifulSoup(new_r.text, "html.parser")

        found_keyword = any(re.search(re.escape(keyword), new_r.text) for keyword in keyword_list)

        if found_keyword :

            faculty_data.append([university, country, name, email, site])
            print([university, country, name, email, site])

    print()
    print("Tsinghua University done...")
    print()


tsinghua()