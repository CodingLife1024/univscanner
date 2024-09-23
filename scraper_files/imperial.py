import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures
import pprint

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile
from components.GLOBAL_VARIABLES import keyword_list

faculty_data = []

u_name = "Imperial College London"
country = "United Kingdom"

def get_faculty_data(prof):
    a = prof.find('a', {'class':'name-link'})

    if a == None:
        return

    a = prof.find('a', {'class':'name-link'})
    link = a.get('href')
    name = a.get_text()

    try:
        prof_resp = requests.get(link)
    except:
        return

    a_mail = prof.find('a', {'class':'email'})
    if a_mail != None:
        email = a_mail.get('href')
        email = email[7:]
    else:
        email = "Not Found"
    prof_soup = BeautifulSoup(prof_resp.text, "html.parser")
    research_text = prof_soup.text

    found_keyword = any(re.search(re.escape(keyword), research_text) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])


def imperial():
    url = "https://www.imperial.ac.uk/computing/people/academic-staff/"   # homepage url
    r = requests.get(url)                                        # request to url

    # getting the soup by parsing the html parsel to text to request r
    soup = BeautifulSoup(r.text, "html.parser")

    # d gives the array of all profs on the dept homepage
    all_profs = soup.find_all('div', {'class':'name-wrapper'})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("Imperial College done...")
    print()
    return faculty_data

if __name__ == "__main__":
    imperial()