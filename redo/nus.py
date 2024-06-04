import requests
from bs4 import BeautifulSoup
import re
from unidecode import unidecode

university = "National University of Singapore"
country = "Singapore"

def nus():
    url = "https://www.comp.nus.edu.sg/cs/people/"   # homepage url
    r = requests.get(url)                                        # request to url

    # getting the soup by parsing the html parsel to text to request r
    soup = BeautifulSoup(r.text, "html.parser")

    faculty_data = []

    keyword_list = ["operating system", "robotics", "kerrnel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

    # Extracting professor names and links
    professors = soup.find_all("a", href=re.compile(r"/cs/people/"))

    # Printing names and links
    for professor in professors:
        link = professor["href"]
        link = "https://www.comp.nus.edu.sg" + link[0:]
        if not link.endswith ("/people/"):
            # print(f"Link: {link}")
            email = link[38:] + "@comp.nus.edu.sg"
            # print(f"Email: {email}")

            new_r = requests.get(link)
            new_soup = BeautifulSoup(new_r.text, 'html.parser')

            name = new_soup.find_all("h4")[0].text if new_soup.find_all("h4") else None
            # print(name)
            # print()

            all_text = new_soup.get_text()

            found_keyword = any(re.search(re.escape(keyword), (all_text).lower()) for keyword in keyword_list)
            if found_keyword:
                print([university, country, unidecode(name), email, link])
                faculty_data.append([university, country, unidecode(name), email, link])
    print()
    print("NUS done...")
    print()

    return faculty_data



nus()
