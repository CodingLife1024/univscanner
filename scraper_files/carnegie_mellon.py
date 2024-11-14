import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import pprint
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile
from components.GLOBAL_VARIABLES import keyword_list

u_name = "Carnegie Mellon University"
country = "United States"

faculty_data = []

def get_faculty_data(prof, headers):
    global faculty_data
    columns = prof.find_all('td')

    if len(columns) == 3:
        name = columns[1].text.strip() + " " + columns[0].text.strip()
        link = "https://csd.cmu.edu" + columns[0].find('a').get('href')

        new_r = requests.get(link, headers=headers)
        new_soup = BeautifulSoup(new_r.text, "html.parser")

        email = new_soup.find('strong', string=lambda x: "Email" in x).find_parent('p').text.replace("Email", "").replace("\n", "").strip() if new_soup.find('strong', string=lambda x: "Email" in x) else "N/A"

        pers_link = new_soup.find('a', string="Website")['href'] if new_soup.find('a', string="Website") else get_scholar_profile(name)

        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def carnegie_mellon():
    urls = [
        "https://csd.cmu.edu/research/research-areas/computer-architecture",
        "https://csd.cmu.edu/research/research-areas/distributed-systems",
        "https://csd.cmu.edu/research/research-areas/operating-systems",
        "https://csd.cmu.edu/research/research-areas/human-computer-interaction",
        "https://csd.cmu.edu/research/research-areas/robotics"
    ]

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }

    all_profs = []

    for url in urls:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")
        print("Fetching URL...", url)

        try:
            profs = soup.find('table', class_="cols-3").find_all('tr')[1:]
            all_profs.extend(profs)
        except:
            print(f"Error occurred while fetching URL: {url}")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof, headers) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nCarnegie Mellon done...\n")
    return faculty_data


if __name__ == "__main__":
    carnegie_mellon()
