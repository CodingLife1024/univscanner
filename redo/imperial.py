import requests
from bs4 import BeautifulSoup
import re

def imperial():
    url = "https://www.imperial.ac.uk/computing/people/academic-staff/"   # homepage url
    r = requests.get(url)                                        # request to url

    # getting the soup by parsing the html parsel to text to request r
    soup = BeautifulSoup(r.text, "html.parser")

    faculty_data = []

    # d gives the array of all profs on the dept homepage
    d = soup.find_all('div', {'class':'name-wrapper'})

    keyword_list = ["operating system", "robotics", "kerrnel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

    #iterating for every prof
    for i in d:
        a = i.find('a', {'class':'name-link'})

        if a == None:
            continue

        a = i.find('a', {'class':'name-link'})# a contains the name and the homepage of prof
        link = a.get('href')                # extracting prof page link
        name = a.get_text()                 # extracting prof name

        try:
            prof_resp = requests.get(link)
        except:
            continue

        a_mail = i.find('a', {'class':'email'})
        if a_mail != None:
            email = a_mail.get('href')
            email = email[7:]
        else:
            email = "Not Found"

        # Check if any of the keywords is present in the professor's webpage
        prof_soup = BeautifulSoup(prof_resp.text, "html.parser")
        research_text = prof_soup.text
        # found_keyword = any(keyword in research_text.lower() for keyword in keyword_list)

        found_keyword = any(re.search(re.escape(keyword), research_text) for keyword in keyword_list)

        # If a keyword is found, add the professor's data to faculty_data
        if found_keyword:
            faculty_data.append(["Imperial College, London", "UK", name, email, link])
            print(["Imperial College London", "UK", name, email, link])

    print()
    print("Imperial College done...")
    print()
    return faculty_data

# imperial()
