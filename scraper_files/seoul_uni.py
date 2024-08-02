import requests
import re
from bs4 import BeautifulSoup
import redo.google_scholar
from requests.exceptions import RequestException, ChunkedEncodingError

u_name = "Seoul National University"
country = "South Korea"

def seoul_uni():
    url = "https://cse.snu.ac.kr/en/people/faculty"

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
    except RequestException as e:
        print(f"Failed to retrieve main page: {e}")
        return []

    soup = BeautifulSoup(r.text, "html.parser")

    faculty_data = []

    keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer", "computer architecture", "fpga"]

    professors = soup.find_all('div', {'class':"flex flex-col items-start break-keep"})

    for professor in professors:
        name = professor.find('span', {'class':"text-[18px] font-bold"}).get_text()
        email_tag = professor.find('a', href=re.compile(r'^mailto:'))
        email = email_tag.get_text() if email_tag else 'Not Found'
        link = "https://cse.snu.ac.kr" + professor.find('a', class_="relative flex w-full cursor-pointer flex-row gap-2 pb-2.5 flex-col").get('href')

        if email != 'Not Found':
            # print(name, email, link)
            try:
                new_r = requests.get(link, headers=headers)
                new_r.raise_for_status()
            except (RequestException, ChunkedEncodingError) as e:
                print(f"Failed to retrieve professor page {link}: {e}")
                continue

            new_soup = BeautifulSoup(new_r.text, "html.parser")

            research = new_soup.text

            found_keyword = any(re.search(keyword, research.lower(), re.IGNORECASE) for keyword in keyword_list)

            if found_keyword:
                try:
                    links = new_soup.find_all('a', class_="text-link hover:underline")
                    site = links[1].get('href') if len(links) > 1 else google_scholar.get_scholar_profile(name)
                except Exception as e:
                    site = google_scholar.get_scholar_profile(name)

                print([u_name, country, name, email, link, site])
                faculty_data.append([u_name, country, name, email, link, site])

    print()
    print("Seoul National University done....")
    print()
    return faculty_data

# seoul_uni()
