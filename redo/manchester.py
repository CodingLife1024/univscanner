import requests
import re
from bs4 import BeautifulSoup

u_name = "University of Manchester"
country = "England"

def uni_menchester():
    url = "https://www.cs.manchester.ac.uk/about/people/academic-and-research-staff/"

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    r = requests.get(url, headers=headers)

    # getting the soup by parsing the html parsel to text to request r
    soup = BeautifulSoup(r.text, "html5lib")

    garbage_emails = ['mkearns@lehman.com', 'michael.kearns@bofasecurities.com', 'lhoot@seas.upenn.edu', 'kearmic@amazon.com']
    var = [u_name, country, garbage_emails]

    # d gives the array of all profs on the dept homepage
    d = soup.find_all('li', {'class': ["tabrowwhite", "tabrowgrey"]})

    # iterating for every prof
    for i in d:
        a = i.find('a')  # a contains the name and the homepage of prof
        if a is None:
            continue
        link = a.get('href')
        name = a.get_text().strip()  # extracting prof name
        try:
            prof_resp = requests.get(link)  # requesting prof homepage
            prof_soup = BeautifulSoup(prof_resp.text, "html.parser")
        except:
            continue

        print(name, link)
        pp = prof_soup.find('a', string='Personal Website')
        if pp is None:
            continue
        link2 = pp.get('href')
        print(name, link2)

        # check if link is valid or not
        try:
            prof_resp = requests.get(link2, headers=headers)
        except:
            continue

        email = "Not Found"
        print(name, link)
        filter_and_get_email(var, name, link, email, prof_resp)

    print("Finished")


def filter_and_get_email(var, name, link, email, prof_resp):
    u_name = var[0]
    country = var[1]
    garbage_emails = var[2]

    keyword_list = ['Computer Architecture', 'hardware and system architecture', 'hardware and architecture',
                    'Computerarchitectuur', 'embedded system', 'computer organization', 'VLSI Design', 'Computer and System',
                    'multiprocessor architecture']
    flag = 1
    prof_soup = BeautifulSoup(prof_resp.text, "html.parser")
    research_text = prof_soup.text
    for pattern in keyword_list:
        if re.search(pattern, research_text, re.IGNORECASE):
            flag = 0
            if email != 'Not Found':
                print(f"{name}\t{email}\n{link}\n")
            else:
                new_emails = set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", prof_resp.text))
                for eemail in garbage_emails:
                    if eemail in new_emails:
                        new_emails.remove(eemail)
                if len(new_emails) == 0:
                    email = "Email Not Found"
                    print(f"{name}\t{email}\n{link}\n")
                else:
                    for email in new_emails:
                        print(f"{name}\t{email}\n{link}\n")
            print(pattern)
            break

if __name__ == '__main__':
    uni_menchester()
