import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile
from components.GLOBAL_VARIABLES import keyword_list

university = "University of Hong Kong"
country = "Hong Kong"

faculty_data = []

def get_name(prof):
    name = prof.find('h4').get_text().split("\n")[0].strip()
    return name

def get_link(prof):
    link = prof.find('a').get('href') if prof.find('a').get('href')[0] == "/" else prof.find('a').get('href')
    # print(link)
    if link.startswith("/"):
        link = "https://www.cs.hku.hk" + link
    if link[-1] == "/":
        link = link[:-1]
    return link


def get_faculty_data(prof, headers):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)

        name = future_name.result()
        link = future_link.result()

    email = link.split("/")[-1] + "@cs.hku.hk"

    new_r = requests.get(link, headers=headers)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    pers_url = new_soup.find('div', class_='col-md-6').find('a').get('href') if new_soup.find('div', class_='col-md-6').find('a') else get_scholar_profile(name)

    if pers_url[0] == "/":
        pers_url = "https://www.cs.hku.hk" + pers_url

    if pers_url.startswith("mailto:"):
        pers_url = get_scholar_profile(name)

    desc = new_r.text

    found_keyword = any(re.search(re.escape(keyword), desc.lower()) for keyword in keyword_list)

    if found_keyword:
        faculty_data.append([university, country, name, email, link, pers_url])
        print([university, country, name, email, link, pers_url])


def hongkong():
    url = "https://www.cs.hku.hk/people/academic-staff"   # homepage url

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    r = requests.get(url)

    # getting the soup by parsing the html parsel to text to request r
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('div', class_='left col-8 col-sm-8')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof, headers) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")


    print("\nUniversity of Hong Kong done...\n")
    return faculty_data

if __name__ == "__main__":
    hongkong()