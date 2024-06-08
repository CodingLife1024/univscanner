import requests
import re
from bs4 import BeautifulSoup

def uni_hongkong():
    url = "https://www.cs.hku.hk/people/academic-staff"   # homepage url

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    r = requests.get(url)

    # getting the soup by parsing the html parsel to text to request r
    soup = BeautifulSoup(r.text, "html.parser")

    d = soup.find_all('div', class_='left col-8 col-sm-8')
    for i in d:
        name = i.find('h4').get_text()
        print(name)
        link = "https://www.cs.hku.hk" + i.find('a').get('href')
        print(link)
        email = link.split("/")[-1] + "@cs.hku.hk"
        print(email)

        print()

uni_hongkong()