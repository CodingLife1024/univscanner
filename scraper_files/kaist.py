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

u_name = "KAIST"
country = "South Korea"

def get_faculty_data(prof):
    category_name = prof.find('span').text

    if category_name != "Emeritus":
        profs = prof.find_next('ul').find_all('li')

        for prof in profs:
            name = prof.find('p', {'class': 'name'}).text.strip()
            email = prof.find('span', onclick=True)
            if email:
                onclick_text = email['onclick']
                match = re.search(r"emailSend\('([^']+)'\)", onclick_text)
                if match:
                    obfuscated_email = match.group(1)
                    email = obfuscated_email.replace('^*', '@')

            link = prof.find('div', class_='item fix')['onclick'][12:-1].split(",")
            link = f"https://cs.kaist.ac.kr/people/view?idx={link[0].strip()}&kind=faculty&menu={link[1].strip()}"

            new_r = requests.get(link)
            new_soup = BeautifulSoup(new_r.text, "html.parser")

            table = new_soup.find('dl', {'class': 'detail'})

            dt_elements = table.find_all('dt')
            dd_elements = table.find_all('dd')

            research = new_soup.text

            for dt, dd in zip(dt_elements, dd_elements):
                if dt.get_text(strip=True) == 'Research Area':
                    research_area = dd.get_text(strip=True)
                elif dt.get_text(strip=True) == 'Major':
                    major = dd.get_text(strip=True)
                elif dt.get_text(strip=True) == 'Website':
                    website = dd.find('a')['href']

            found_keyword = any(re.search(keyword, research, re.IGNORECASE) for keyword in keyword_list)

            if found_keyword:
                faculty_data.append([u_name, country, name, email, link, website])
                print([u_name, country, name, email, link, website])

def kaist():
    url = "https://cs.kaist.ac.kr/people/faculty"

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('p', {'class': 'line'})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nKAIST done...\n")
    return faculty_data

if __name__ == "__main__":
    kaist()