import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile

u_name = "KU Leuven"
country = "Belgium"

faculty_data = []

keyword_list = [
    "operating system", "robotics", "kernel", "embedded system",
    "hardware", "computer architecture", "distributed system",
    "computer organization", "vlsi", "computer and system",
    "human-computer interaction", "human computer"
]

def ku_leuven():
    url = "https://www.esat.kuleuven.be/psi/people/"
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")
    all_profs = soup.find_all('div', class_='ppl-detail__item')