from bs4 import BeautifulSoup
import requests
import re
import concurrent.futures

university = "Tsinghua University"
country = "China"

def fetch_faculty_data(faculty):
    keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture",
                    "distributed system", "computer organization", "vlsi", "computer and system",
                    "human-computer interaction", "human computer"]

    name = faculty.find('a').text
    site = "https://www.cs.tsinghua.edu.cn/csen" + faculty.find('a')['href'][2:]
    email = faculty.find_all('p')[2].text

    new_r = requests.get(site)
    found_keyword = any(re.search(re.escape(keyword), new_r.text) for keyword in keyword_list)

    if found_keyword:
        return [university, country, name, email, site]
    return None

def tsinghua():
    url = "https://www.cs.tsinghua.edu.cn/csen/Faculty/Full_time_Faculty.htm"

    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    faculty_cards = soup.find_all('div', class_='text')

    faculty_data = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(fetch_faculty_data, faculty_cards))

    faculty_data = [result for result in results if result]

    for data in faculty_data:
        print(data)

    print()
    print("Tsinghua University done...")
    print()
    return faculty_data
