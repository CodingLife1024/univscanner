from bs4 import BeautifulSoup
import requests
import re

def mit():
    url = "https://www.eecs.mit.edu/role/faculty/"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    html_content = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # d gives the array of all profs on the dept homepage
    d = soup.find_all('div', {'class':"views-field views-field-title"})

    # iterating for every prof
    for i in d:
        a = i.find('a')                     # a contains the name and the homepage of prof
        if a == None:
            continue
        link = a.get('href')                # extracting prof page link
        name = a.get_text()                 # extracting prof name
        try:
            prof_resp = requests.get(link, headers=headers)      # requesting prof homepgae
        except:
            continue
        email = "Not Found"
        print(name, email, link)
        filterandgetEmail(name, link, email, prof_resp)

    print("Finished")

def filterandgetEmail(name, link, email, prof_resp):

    keyword_list = ['Embedded System', 'Embedded system', 'embedded system']
    flag = 1
    prof_soup = BeautifulSoup(prof_resp.text, "html.parser")
    # print(prof_soup)
    research_text = prof_soup.text
    for pattern in keyword_list:
        if re.search(pattern,research_text):
            flag = 0
            if email != 'Not Found':
                print(link)
                print(name, "\t", email)
            else:
                new_emails = set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", prof_resp.text))
                if len(new_emails) == 0:
                    email = "Email Not Found"
                    print(link)
                    print(name, "\t", email)
                else:
                    for email in new_emails:
                        print(link)
                        print(name, '\t\t', email)
            print(pattern)
            print()
            break

if __name__ == '__main__':
    mit()
