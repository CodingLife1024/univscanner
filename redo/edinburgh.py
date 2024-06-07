import requests
import urllib.request
import time
import urllib
import re
from bs4 import BeautifulSoup

def uni_edinburgh():
    url = "https://www.ed.ac.uk/informatics/people/academic"   # homepage url
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    r = requests.get(url, headers=headers)                                        # request to url

    # getting the soup by parsing the html parsel to text to request r
    soup = BeautifulSoup(r.text, "html.parser")

    # d gives the array of all profs on the dept homepage
    dd = soup.find('div', {'class':"inf-people"})
    d = dd.find_all('a')

    #iterating for every prof
    for i in d:
        link = i.get('href')                # extracting prof page link
        if link is None or link.startswith('#') or link.startswith('mailto'):
            continue
        name = i.get_text()                 # extracting prof name

        try:
            prof_resp = requests.get(link, headers=headers)
        except:
            continue

        email = "Not Found"
        print(name, link)
        filterandgetEmail(name, link, email, prof_resp)


def filterandgetEmail(name, link, email, prof_resp):
    keyword_list = ['Computer Architecture','hardware and system architecture', 'hardware and architecture', 'Computerarchitectuur', 'embedded system', 'computer organization','VLSI Design', 'Computer and System',
                    'multiprocessor architecture']
    prof_soup = BeautifulSoup(prof_resp.text, "html.parser")
    research_text = prof_soup.text
    for pattern in keyword_list:
        if re.search(pattern, research_text, re.IGNORECASE):
            if email != 'Not Found':
                print("Link:", link)
                print("Name:", name)
                print("Email:", email)
            else:
                new_emails = set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", prof_resp.text))
                if len(new_emails) == 0:
                    email = "Email Not Found"
                    print("Link:", link)
                    print("Name:", name)
                    print("Email:", email)
                else:
                    for email in new_emails:
                        print("Link:", link)
                        print("Name:", name)
                        print("Email:", email)
            break

if __name__ == '__main__':
    uni_edinburgh()
