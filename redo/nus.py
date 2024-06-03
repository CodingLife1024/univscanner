import requests
from bs4 import BeautifulSoup
import re

def nus():
    url = "https://www.comp.nus.edu.sg/cs/people/"   # homepage url
    r = requests.get(url)                                        # request to url

    # getting the soup by parsing the html parsel to text to request r
    soup = BeautifulSoup(r.text, "html.parser")

    # Extracting professor names and links
    professors = soup.find_all("a", href=re.compile(r"/cs/people/"))

    # Printing names and links
    for professor in professors:
        name = professor.get_text(strip=True)
        link = professor["href"]
        link = "https://www.comp.nus.edu.sg" + link[:-1]
        if not link.endswith ("/people"):
            print(f"Name: {name}, Link: {link}")



nus()
