import requests
from bs4 import BeautifulSoup
import sys
import os
import re
from requests.exceptions import RequestException, ChunkedEncodingError
import concurrent.futures
import pprint

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile
from components.GLOBAL_VARIABLES import keyword_list

faculty_data = []

u_name = "Seoul National University"
country = "South Korea"

def get_faculty_data(prof, headers):
    name = prof.find('a').find('span').text.strip()
    email = prof.find('a', href=re.compile(r'^mailto:')).text if prof.find('a', href=re.compile(r'^mailto:')) else "N/A"
    link = "https://cse.snu.ac.kr" + prof.find('a').get('href') if prof.find('a') else "N/A"

    if email != 'N/A':
        try:
            new_r = requests.get(link, headers=headers)
            new_r.raise_for_status()
        except (RequestException, ChunkedEncodingError) as e:
            print(f"Failed to retrieve prof page {link}: {e}")
            return

        new_soup = BeautifulSoup(new_r.text, "html.parser")
        research = new_soup.text

        found_keyword = any(re.search(keyword, research.lower(), re.IGNORECASE) for keyword in keyword_list)

        if found_keyword:
            try:
                links = new_soup.find_all('a', class_="text-link hover:underline")
                site = links[1].get('href') if len(links) > 1 else get_scholar_profile(name)
            except Exception as e:
                site = get_scholar_profile(name)

            print([u_name, country, name, email, link, site])
            faculty_data.append([u_name, country, name, email, link, site])

def seoul_uni():
    url = "https://cse.snu.ac.kr/en/people/faculty"

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
    except RequestException as e:
        print(f"Failed to retrieve main page: {e}")
        return []

    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('div', {'class':"flex flex-col items-start break-keep"})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof, headers) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nSeoul National University done...\n")
    return faculty_data


if __name__ == '__main__':
    seoul_uni()