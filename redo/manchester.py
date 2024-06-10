import requests
import re
from bs4 import BeautifulSoup
from google_scholar import get_scholar_profile

u_name = "University of Manchester"
country = "England"

def manchester():
    url = "https://www.cs.manchester.ac.uk/about/people/academic-and-research-staff/"

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    r = requests.get(url, headers=headers)

    # getting the soup by parsing the html parsel to text to request r
    soup = BeautifulSoup(r.text, "html.parser")

    keyword_list = ["operating system", "robotics", "kerrnel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

    dd = soup.find('div', {'class': 'tabRows'})

    d = dd.find_all('li', class_=lambda x: x in ['tabrowwhite', 'tabrowgrey'])

    faculty_data = []

    for i in d:
        name = i.find_all('div', class_="tabCol_30")[0].text[6:]
        email = ".".join(name.lower().split(" ")) + "@manchester.ac.uk"
        link = i.find_all('a', href=True)[0]['href'] if i.find_all('a', href=True) else "Not Available"

        expertise = i.find_all('div', class_="tabCol_30")[2].text[19:] if len(i.find_all('div', class_="tabCol_30")) >= 3 else "Not Available"

        # print(name, link)
        # print("Expertise: ", expertise)
        # print()

        if expertise == "Human computer systems" or expertise == "Machine learning and robotics":
            faculty_data.append([u_name, country, name, email, link, get_scholar_profile(name)])
            print([u_name, country, name, email, link, get_scholar_profile(name)])

        elif expertise == "Not Available" or expertise == "Teaching":

            if link != "Not Available":
                new_r = requests.get(link, headers=headers)
                new_soup = BeautifulSoup(new_r.text, "html.parser")

                fingerprints = ""

                new_link = new_soup.find_all('button', class_="concept-badge-large dropdown-toggle")

                for i in new_link:
                    fingerprints += i.text

                found_keyword = any(re.search(re.escape(keyword), fingerprints) for keyword in keyword_list)

                if found_keyword:
                    faculty_data.append([u_name, country, name, email, link, get_scholar_profile(name)])
                    print([u_name, country, name, email, link, get_scholar_profile(name)])
            else:
                link = get_scholar_profile(name)

                if link != None:
                    new_r = requests.get(link, headers=headers)
                    new_soup = BeautifulSoup(new_r.text, "html.parser")

                    found_keyword = any(re.search(re.escape(keyword), new_r.text) for keyword in keyword_list)
                    if found_keyword:
                        faculty_data.append([u_name, country, name, email, link, get_scholar_profile(name)])
                    print([u_name, country, name, email, link, get_scholar_profile(name)])


    print()
    print("University of Manchester done...")
    print()

    return faculty_data

# uni_menchester()