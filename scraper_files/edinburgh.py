import requests
from bs4 import BeautifulSoup
import re

university = "Edinburgh"
country = "UK"

def edinburgh():
    url = "https://www.ed.ac.uk/informatics/people/academic"   # homepage url

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }

    r = requests.get(url, headers=headers)  # request to url

    # getting the soup by parsing the html parse to text to request r
    soup = BeautifulSoup(r.text, "html.parser")

    faculty_data = []

    keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

    d = soup.find('div', class_="inf-people")

    # Ensure we found the right div
    for li in d.find_all('li'):
        a = li.find('a')
        if a:
            name = a.text.strip()
            link = a.get('href')
            # print(name, link)

            if link:
                new_r = requests.get(link, headers=headers)
                new_soup = BeautifulSoup(new_r.text, "html.parser")

                roles_and_positions = ""

                alls = new_soup.find('dl')
                if alls:
                    for a in alls.find_all('dd'):
                        if a:
                            text = a.text.strip()
                            if text[-9:] == "ed.ac.uk>":
                                email = text[1:-1]
                                # print(email)
                            else:
                                roles_and_positions += text + ", "

                found_keyword = any(keyword.lower() in roles_and_positions.lower() for keyword in keyword_list)

                if found_keyword:
                    last_dl = new_soup.find_all('dl')[-1]
                    pers_url = None
                    if last_dl:
                        a_tag = last_dl.find('a', string="Personal Page")
                        if a_tag:
                            pers_url = a_tag.get('href')
                        else:
                            pers_url = "Personal URL not found"

                        print([university, country, name, email, link, pers_url])
                        faculty_data.append([university, country, name, email, link, pers_url])

    print()
    print("Edinburgh done...")
    print()
    return faculty_data



if __name__ == "__main__":
    edinburgh()
