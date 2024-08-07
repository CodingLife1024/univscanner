import requests
from bs4 import BeautifulSoup

university = "Columbia University"
country = "USA"

def columbia():
    url = "https://www.cs.columbia.edu/people/faculty/"   # homepage url
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    r = requests.get(url, headers=headers)


    faculty_data = []

    # getting the soup by parsing the html parsel to text to request r
    soup = BeautifulSoup(r.text, "html.parser")

    keyword_list = ["operating system", "robotics", "kerrnel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

    # d gives the array of all profs on the dept homepage
    d = soup.find_all('div', class_="faculty-details")

    #iterating for every prof
    for i in d:
        name = i.find('span', class_="faculty-name").get_text().strip()  # extracting prof name
        url = i.find('span', class_="faculty-name").find('a')['href']  # extracting prof page link
        email = i.find('a', href=lambda href: href and href.startswith("mailto:"))
        interests = i.find('div', class_="faculty-interests").get_text().strip() if i.find('div', class_="faculty-interests") else "Not Found"

        if email is not None:
            email = email.get_text().strip()
        else:
            email = "Not Found"

        found_keyword = any(keyword.lower() in interests.lower() for keyword in keyword_list)

        pers_links = i.find('div', class_="faculty-links").find_all('a')
        if pers_links:
            pers_links = [link['href'] for link in pers_links][0]
        else:
            pers_links = "Not Found"

        if found_keyword:
            print([university, country, name, email, url, pers_links])
            faculty_data.append([university, country, name, email, url, pers_links])

    print()
    print("Columbia done...")
    print()

    return faculty_data

# columbia()