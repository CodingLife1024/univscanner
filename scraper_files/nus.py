import requests
from bs4 import BeautifulSoup
import sys
import os
import re
from unidecode import unidecode
import concurrent.futures
import pprint

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile
from components.GLOBAL_VARIABLES import keyword_list

faculty_data = []

university = "National University of Singapore"
country = "Singapore"

def get_faculty_data(prof):
    link = prof["href"]
    link = "https://www.comp.nus.edu.sg" + link[0:]
    if not link.endswith ("/people/"):
        # print(f"Link: {link}")
        email = link[38:] + "@comp.nus.edu.sg"
        # print(f"Email: {email}")

        new_r = requests.get(link)
        new_soup = BeautifulSoup(new_r.text, 'html.parser')

        name = new_soup.find_all("h4")[0].text if new_soup.find_all("h4") else "N/A"

        research = new_soup.get_text()

        found_keyword = any(re.search(re.escape(keyword), (research).lower()) for keyword in keyword_list)
        if found_keyword:
            pers_link = get_scholar_profile(name)
            print([university, country, unidecode(name), email, link, pers_link])
            faculty_data.append([university, country, unidecode(name), email, link, pers_link])

def nus():
    url = "https://www.comp.nus.edu.sg/cs/people/"   # homepage url
    r = requests.get(url)                                        # request to url

    # getting the soup by parsing the html parsel to text to request r
    soup = BeautifulSoup(r.text, "html.parser")

    # Extracting prof names and links
    all_profs = soup.find_all("a", href=re.compile(r"/cs/people/"))

    # Printing names and links
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nNational University of Singapore done...\n")
    return faculty_data


if __name__ == "__main__":
    nus()
