import requests
import re
from bs4 import BeautifulSoup

university = "University of Hong Kong"
country = "Hong Kong"

def hongkong():
    url = "https://www.cs.hku.hk/people/academic-staff"   # homepage url

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    r = requests.get(url)

    faculty_data = []

    keyword_list = ["operating system", "robotics", "kerrnel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

    # getting the soup by parsing the html parsel to text to request r
    soup = BeautifulSoup(r.text, "html.parser")

    d = soup.find_all('div', class_='left col-8 col-sm-8')
    for i in d:
        name = i.find('h4').get_text()
        # print(name)
        link = "https://www.cs.hku.hk" + i.find('a').get('href') if i.find('a').get('href')[0] == "/" else i.find('a').get('href')
        # print(link)
        if link[-1] == "/":
            link = link[:-1]
        email = link.split("/")[-1] + "@cs.hku.hk"
        # print(email)

        new_r = requests.get(link)
        new_soup = BeautifulSoup(new_r.text, "html.parser")

        try :
            pers_url = new_soup.find('div', class_='col-md-6').find('a').get('href') if new_soup.find('div', class_='col-md-6').find('a') else "Personal URL not found"
        except:
            pers_url = "Personal URL not found"

        if pers_url[0] == "/":
            pers_url = "https://www.cs.hku.hk" + pers_url

        if pers_url.startswith("mailto:"):
            pers_url = "Personal URL not found"

        # print(pers_url)

        try:
            desc = new_soup.find('div', class_='sp-column').get_text()
        except:
            desc = new_r.text

        found_keyword = any(re.search(re.escape(keyword), desc) for keyword in keyword_list)

        if found_keyword:
            faculty_data.append([university, country, name, email, link, pers_url])
            print([university, country, name, email, link, pers_url])


    print()
    print("University of Hong Kong done...")
    print()
    return faculty_data

hongkong()