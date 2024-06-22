import requests
from bs4 import BeautifulSoup

def exp():
    url = "https://prism-pages.vercel.app/"

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    print(soup.prettify())

exp()