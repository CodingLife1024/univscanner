import requests
import re
from bs4 import BeautifulSoup
import google_scholar
from requests.exceptions import RequestException, ChunkedEncodingError

u_name = "KAIST"
country = "South Korea"

def kaist():
    url = "https://cs.kaist.ac.kr/people/faculty"

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    faculty_data = []

    keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

    all_categories = soup.find_all('p', {'class': 'line'})

    for category in all_categories:
        category_name = category.find('span').text

        if category_name != "Emeritus":
            profs = category.find_next('ul').find_all('li')

            for prof in profs:
                name = prof.find('p', {'class': 'name'}).text.strip()
                # print(name)
                email = prof.find('span', onclick=True)
                if email:
                    onclick_text = email['onclick']

                    # Extract the email address from the onclick attribute
                    match = re.search(r"emailSend\('([^']+)'\)", onclick_text)
                    if match:
                        obfuscated_email = match.group(1)

                        # Replace the obfuscating characters
                        email = obfuscated_email.replace('^*', '@')
                        # print(email)

                link = prof.find('div', class_='item fix')['onclick'][12:-1].split(",")
                link = f"https://cs.kaist.ac.kr/people/view?idx={link[0].strip()}&kind=faculty&menu={link[1].strip()}"
                # print(link)

                new_r = requests.get(link)
                new_soup = BeautifulSoup(new_r.text, "html.parser")

                table = new_soup.find('dl', {'class': 'detail'})

                dt_elements = table.find_all('dt')
                dd_elements = table.find_all('dd')

                for dt, dd in zip(dt_elements, dd_elements):
                    if dt.get_text(strip=True) == 'Research Area':
                        research_area = dd.get_text(strip=True)
                    elif dt.get_text(strip=True) == 'Major':
                        major = dd.get_text(strip=True)
                    elif dt.get_text(strip=True) == 'Website':
                        website = dd.find('a')['href']

                # print(research_area, major, website)

                found_keyword = any(re.search(keyword, research_area.lower() + major.lower(), re.IGNORECASE) for keyword in keyword_list)

                if found_keyword:
                    faculty_data.append([u_name, country, name, email, link, website])
                    print([u_name, country, name, email, link, website])

                # print()

    print()
    print("KAIST done....")
    print()
    return faculty_data


# kaist()