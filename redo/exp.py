import requests
from bs4 import BeautifulSoup
import re

url = "https://www.kcl.ac.uk/people/alfie-abdul-rahman"

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

websites = soup.find('a', string=lambda text: text and ('Personal website' in text or 'Research Profile' in text))

if websites:
    print(websites['href'])