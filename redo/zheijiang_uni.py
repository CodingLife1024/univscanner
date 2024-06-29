import requests
import re
from bs4 import BeautifulSoup
import google_scholar

u_name = "Zhejiang University"
country = "China"

def zhejiang_uni():
    url_1 = "http://www.en.cs.zju.edu.cn/jsjxtjgywlaqyjs/list.htm"
    r_1 = requests.get(url_1)
    url_2 = "http://www.en.cs.zju.edu.cn/jsjrjyjs/list.htm"
    r_2 = requests.get(url_2)
    url_3 = "http://www.en.cs.zju.edu.cn/gysjyjs/list.htm"
    r_3 = requests.get(url_3)
    soup = BeautifulSoup(r_1.text + r_2.text + r_3.text, "html.parser")

    keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction"]

    faculty_data = []

    garbage_emails = ['xwmaster@zju.edu.cn']

    var = garbage_emails

    dd = soup.find('ul', {'class':"wp_article_list"})
    d = dd.find_all('div', {'class':"fields pr_fields"})

    for i in d:
        a = i.find('a')
        name = (a.get_text()).strip()
        link = a.get('href')

        try:
            prof_resp = requests.get(link)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {link}: {e}")
            continue

        email = "Not Found"
        prof_soup = BeautifulSoup(prof_resp.text, "html.parser")
        research_text = prof_soup.text

        found_keyword = any(re.search(re.escape(keyword), research_text.lower()) for keyword in keyword_list)
        matching_keywords = [keyword for keyword in keyword_list if re.search(re.escape(keyword), research_text.lower())]

        if found_keyword or True:
            new_emails = set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", prof_resp.text))

            for garbage_email in garbage_emails:
                if garbage_email in new_emails:
                    new_emails.remove(garbage_email)

            if email != 'Not Found':
                print([u_name, country, name, email, link, google_scholar.get_scholar_profile(name)])
                faculty_data.append([u_name, country, name, email, link, google_scholar.get_scholar_profile(name)])
            elif len(new_emails) == 0:
                email = "Email Not Found"
                print([u_name, country, name, email, link, google_scholar.get_scholar_profile(name)])
                faculty_data.append([u_name, country, name, email, link, google_scholar.get_scholar_profile(name)])
            else:
                for email in new_emails:
                    print([u_name, country, name, email, link, google_scholar.get_scholar_profile(name)])
                    faculty_data.append([u_name, country, name, email, link, google_scholar.get_scholar_profile(name)])

    print()
    print("Zhejiang University done...")
    print()
    return faculty_data


# zhejiang_uni()
