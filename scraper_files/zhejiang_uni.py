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

u_name = "Zhejiang University"
country = "China"

def get_faculty_data(prof, garbage_emails):
    a = prof.find('a')
    name = (a.get_text()).strip()
    link = a.get('href')

    try:
        prof_resp = requests.get(link)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {link}: {e}")
        return

    email = "N/A"
    prof_soup = BeautifulSoup(prof_resp.text, "html.parser")
    research_text = prof_soup.text

    found_keyword = any(re.search(re.escape(keyword), research_text.lower()) for keyword in keyword_list)

    if found_keyword:
        new_emails = set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", prof_resp.text))

        for garbage_email in garbage_emails:
            if garbage_email in new_emails:
                new_emails.remove(garbage_email)

        if email != 'N/A':
            print([u_name, country, name, email, link, get_scholar_profile(name)])
            faculty_data.append([u_name, country, name, email, link, get_scholar_profile(name)])
        elif len(new_emails) == 0:
            pers_link = get_scholar_profile(name)
            print([u_name, country, name, email, link, pers_link])
            faculty_data.append([u_name, country, name, email, link, pers_link])
        else:
            for email in new_emails:
                pers_link = get_scholar_profile(name)
                print([u_name, country, name, email, link, pers_link])
                faculty_data.append([u_name, country, name, email, link, pers_link])

def zhejiang_uni():
    url_1 = "http://www.en.cs.zju.edu.cn/jsjxtjgywlaqyjs/list.htm"
    r_1 = requests.get(url_1)
    url_2 = "http://www.en.cs.zju.edu.cn/jsjrjyjs/list.htm"
    r_2 = requests.get(url_2)
    url_3 = "http://www.en.cs.zju.edu.cn/gysjyjs/list.htm"
    r_3 = requests.get(url_3)
    soup = BeautifulSoup(r_1.text + r_2.text + r_3.text, "html.parser")

    garbage_emails = ['xwmaster@zju.edu.cn']

    var = garbage_emails

    dd = soup.find('ul', {'class':"wp_article_list"})
    all_profs = dd.find_all('div', {'class':"fields pr_fields"})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof, garbage_emails) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")


    print("\nZhejiang University done...\n")
    return faculty_data


if __name__ == '__main__':
    zhejiang_uni()