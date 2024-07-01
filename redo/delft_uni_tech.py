import requests
import re
from bs4 import BeautifulSoup
import google_scholar

def delft_uni_tech():
    url = "https://www.tudelft.nl/en/eemcs/the-faculty/professors"   # homepage url
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")

    keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction"]

    faculty_data = []

    dd = soup.find('article', {'class':'md-9'})

    