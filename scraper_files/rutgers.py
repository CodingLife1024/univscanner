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

u_name = "Rutgers-New Brunswick University"
country = "United States"

def get_faculty_data_1(prof):
    name = prof.find('a').text.strip()
    link = "https://www.cs.rutgers.edu" + prof.find('a').get('href')
    email = prof.find('a', href=re.compile(r'^mailto:')).text.strip() if prof.find('a', href=re.compile(r'^mailto:')) else "N/A"

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    research = new_soup.text.strip()

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = new_soup.find('li', class_="field-entry website ").find('a')['href'] if new_soup.find('li', class_="field-entry website ").find('a') else get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def get_faculty_data_2(prof):
    name = prof.find('a').text.strip()
    link = "https://www.cs.rutgers.edu" + prof.find('a').get('href')

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    research = new_soup.text.strip()

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        email_spans = prof.find('span',class_="detail_data").find_all('span', class_=False)
        flag = 0
        email_parts_0 = []
        email_parts_1 = []
        for det in email_spans:
            for attr_name, attr_value in det.attrs.items():
                if attr_name.startswith('data-ep'):
                    if flag == 0:
                        email_parts_0.append(attr_value)
                        flag = 1
                    else:
                        email_parts_1.append(attr_value)
                        flag = 0

        email_parts_0 = email_parts_0[:3]
        email_parts_1 = email_parts_1[:3]
        email_parts = email_parts_0.extend(email_parts_1.reverse())
        email = "".join(email_parts)
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])


def rutgers():
    urls = [
        "https://www.cs.rutgers.edu/people/professors",
        "https://www.cs.rutgers.edu/people/affiliated-faculty",
        "https://www.cs.rutgers.edu/people/lecturers",
        "https://www.cs.rutgers.edu/people/researchers"
    ]

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0'}

    # urls 1 and 2

    urlss = [urls[0], urls[1]]

    total_text_1 = ""

    for url in urlss:
        r = requests.get(url)
        total_text_1 += r.text

    soup = BeautifulSoup(total_text_1, "html.parser")

    all_profs = soup.find_all('div', {'class': 'news'})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data_1, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    # urls 3 and 4
    urlss = [urls[2], urls[3]]

    total_text_2 = ""

    for url in urlss:
        r = requests.get(url, headers=headers)
        total_text_2 += r.text

    soup = BeautifulSoup(total_text_2, "html.parser")

    all_profs = soup.find_all('div', {'class': 'news'})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data_2, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nRutgers-New Brunswick University done...\n")
    return faculty_data


if __name__ == '__main__':
    rutgers()