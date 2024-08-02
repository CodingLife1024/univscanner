import requests
import re
from bs4 import BeautifulSoup
import redo.google_scholar

university = "Chinese University of Hong Kong"
country = "Hong Kong"

def chinese_uni_hk():
    url = "https://www.cse.cuhk.edu.hk/research/computer-engineering/"

    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36'}

    r = requests.get(url, headers=headers, verify=False)

    soup = BeautifulSoup(r.text, "html.parser")

    faculty_data = []

    faculty_list = soup.find_all('div', class_='sptp-member border-bg-around-member')

    for faculty in faculty_list:
        name = faculty.find('h2').get_text()
        link = "https://www.cse.cuhk.edu.hk" + faculty.find('a').get('href')
        if link[-1] == "/":
            link = link[:-1]
        email = "Not Found"

        print(name, email, link)


chinese_uni_hk()