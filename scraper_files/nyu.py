import re
import requests
from bs4 import BeautifulSoup
from components.google_scholar import get_scholar_profile

u_name = 'New York University'
country = 'USA'

def nyu():
    url = 'https://cs.nyu.edu/dynamic/people/faculty/type/20/'

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

    faculty_data = []

    faculty_list = soup.find_all('li', class_='col-sm-6')

    for faculty in faculty_list:
        name_tag = faculty.find('p', class_='name bold')
        if name_tag:
            name = name_tag.get_text(strip=True)
            website_tag = name_tag.find('a')
            website = website_tag['href'] if website_tag else None

            email_tag = faculty.find(string=re.compile(r'Email:'))
            if email_tag:
                email = email_tag.split('Email: ')[1].split(' ')[0] + "@cs.nyu.edu"
            else:
                email = None

            if website:
                try:
                    new_r = requests.get(website, headers=headers)
                    new_soup = BeautifulSoup(new_r.text, 'html.parser')
                    research_interests = new_soup.text

                    found_keyword = any(re.search(re.escape(keyword), research_interests.lower()) for keyword in keyword_list)

                    if found_keyword:
                        print([u_name, country, name, email, website, get_scholar_profile(name)])
                        faculty_data.append([u_name, country, name, email, website, get_scholar_profile(name)])

                except requests.exceptions.SSLError as e:
                    print(f"SSL error for {website}: {e}")

    print()
    print("New York University done....")
    print()
    return faculty_data

# nyu()
