import requests
import re
from bs4 import BeautifulSoup

def uni_cornell():
    url = "https://www.cs.cornell.edu/people/faculty"   # homepage url
    r = requests.get(url)                                        # request to url

    # getting the soup by parsing the html parsel to text to request r
    soup = BeautifulSoup(r.text, "html.parser")

    u_name = "Cornell University"
    country = "USA"

    grabage_emails = ['microservices-bench-L@list.cornell.edu']
    var = [u_name, country, grabage_emails]

    # d gives the array of all profs on the dept homepage
    d = soup.find_all('h6', {'class':"text-primary"})

    #iterating for every prof
    for i in d:
        a = i.find('a')                     # a contains the name and the homepage of prof
        link = a.get('href')                # extracting prof page link
        if link == None or link[0] == '#' or link[0:6] == 'mailto':
            continue
        name = a.get_text()                 # extracting prof name
        try:
            prof_resp = requests.get(link)          # requesting prof homepgae
        except:
            continue

        email = "Not Found"
        print(name, link)
        filterandgetEmail(var, grabage_emails, name, link, email, prof_resp)

    print("Finished")

def filterandgetEmail(var, grabage_emails, name, link, email, prof_resp):
    u_name = var[0]
    country = var[1]

    keyword_list = ['Computer Architecture','hardware and system architecture', 'hardware and architecture', 'Computerarchitectuur', 'embedded system', 'computer organization','VLSI Design', 'Computer and System',
                    'multiprocessor architecture']
    flag = 1
    prof_soup = BeautifulSoup(prof_resp.text, "html.parser")
    research_text = prof_soup.text
    for pattern in keyword_list:
        if re.search(pattern, research_text, re.IGNORECASE):
            flag = 0
            if email != 'Not Found':
                print(name, link, email)
            else:
                new_emails = set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", prof_resp.text))
                for eemail in grabage_emails:
                    if eemail in new_emails:
                        new_emails.remove(eemail)
                if len(new_emails) == 0:
                    email = "Email Not Found"
                    print(name, link, email)
                else:
                    for email in new_emails:
                        print(name, link, email)
            break

if __name__ == '__main__':
    uni_cornell()
