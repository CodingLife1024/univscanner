import requests
import re
from bs4 import BeautifulSoup
from unidecode import unidecode

university = "Yale University"
country = "USA"

def yale():
    url = "https://cpsc.yale.edu/people/faculty"

    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    faculty_data = []

    keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction"]

    # Find all tables containing professor information
    tables = soup.find_all('tr', class_=re.compile(r'clickable'))

    for i in tables:
        name = i.find('a', class_="username").text.strip()
        url = "https://cpsc.yale.edu" + i.find('a')['href']
        # new_r = requests.get(url)
        # new_soup = BeautifulSoup(new_r.text, 'html.parser')
        email = i.find('a', href=re.compile(r'mailto:')).text.strip()

        pers_site = i.find('a', string='Website')['href'] if i.find('a', string='Website') else "Personal Website not found"
        if pers_site != "Personal Website not found":
            try:
                new_r = requests.get(pers_site)
                new_soup = BeautifulSoup(new_r.text, 'html.parser')
                pers_text = new_soup.text

                site_r = requests.get(url)
                site_soup = BeautifulSoup(site_r.text, 'html.parser')
                site_text = site_soup.text

                found_keyword = any(re.search(re.escape(keyword), (pers_text + site_text).lower()) for keyword in keyword_list)

                if found_keyword:
                    print([university, country, unidecode(name), email, url, pers_site])
                    faculty_data.append([university, country, unidecode(name), email, url, pers_site])
            except:
                continue
    print()
    print("Yale done...")
    print()
    return faculty_data

# yale()
