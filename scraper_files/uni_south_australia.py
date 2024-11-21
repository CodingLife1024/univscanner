import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures
import pprint

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile
from components.GLOBAL_VARIABLES import keyword_list

faculty_data = []

u_name = "University of South Australia"
country = "Australia"

def get_faculty_data(prof):
    link = prof['data-fb-result']
    name = prof.find('h3').text.replace("Dr", "").replace("Professor", "").replace("Associate", "").strip()
    email = prof.find('a', href=re.compile(r'^mailto:')).text.strip() if prof.find('a', href=re.compile(r'^mailto:')) else "N/A"
    pers_link = get_scholar_profile(name)

    position = prof.find('ul', class_="list-unstyled", id="staff-position").text.lower()

    if "professor" in position or "lecturer" in position:
        new_r = requests.get(link)
        new_soup = BeautifulSoup(new_r.text, "html.parser")

        research = new_soup.text

        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

        if found_keyword:
            faculty_data.append([u_name, country, name, email, link, pers_link])
            print([u_name, country, name, email, link, pers_link])

def uni_south_australia():
    global faculty_data
    urls = [
        "https://search.unisa.edu.au/s/search.html?query=Computer+science&collection=people"
        "https://search.unisa.edu.au/s/search.html?query=Computer+science&collection=people&start_rank=11"
        "https://search.unisa.edu.au/s/search.html?clicked_fluster=electrical+engineering&cluster0=Electrical&query=%60Electrical+Engineering%60&collection=people",
        "https://search.unisa.edu.au/s/search.html?clicked_fluster=electrical+engineering&cluster0=Electrical&query=%60Electrical+Engineering%60&collection=people&start_rank=11",
        'https://search.unisa.edu.au/s/search.html?clicked_fluster=electrical+engineering&cluster0=Electrical&query=%60Electrical+Engineering%60&collection=people&start_rank=21'
        "https://search.unisa.edu.au/s/search.html?clicked_fluster=electrical+engineering&cluster0=Electrical&query=%60Electrical+Engineering%60&collection=people&start_rank=31",
        "https://search.unisa.edu.au/s/search.html?clicked_fluster=electrical+engineering&cluster0=Electrical&query=%60Electrical+Engineering%60&collection=people&start_rank=41",
        "https://search.unisa.edu.au/s/search.html?clicked_fluster=electrical+engineering&cluster0=Electrical&query=%60Electrical+Engineering%60&collection=people&start_rank=51",
        "https://search.unisa.edu.au/s/search.html?clicked_fluster=electrical+engineering&cluster0=Electrical&query=%60Electrical+Engineering%60&collection=people&start_rank=61",
        "https://search.unisa.edu.au/s/search.html?clicked_fluster=electrical+engineering&cluster0=Electrical&query=%60Electrical+Engineering%60&collection=people&start_rank=71",
        "https://search.unisa.edu.au/s/search.html?clicked_fluster=electrical+engineering&cluster0=Electrical&query=%60Electrical+Engineering%60&collection=people&start_rank=81",
        "https://search.unisa.edu.au/s/search.html?clicked_fluster=electrical+engineering&cluster0=Electrical&query=%60Electrical+Engineering%60&collection=people&start_rank=91"
        "https://search.unisa.edu.au/s/search.html?clicked_fluster=electrical+and+electronic&cluster0=Electrical&query=%60Electrical+and+Electronic%60&collection=people",
        "https://search.unisa.edu.au/s/search.html?clicked_fluster=electrical+and+electronic&cluster0=Electrical&query=%60Electrical+and+Electronic%60&collection=people&start_rank=11",
        "https://search.unisa.edu.au/s/search.html?clicked_fluster=electrical+and+electronic&cluster0=Electrical&query=%60Electrical+and+Electronic%60&collection=people&start_rank=21",
        "https://search.unisa.edu.au/s/search.html?clicked_fluster=electrical+and+electronic&cluster0=Electrical&query=%60Electrical+and+Electronic%60&collection=people&start_rank=31",
        "https://search.unisa.edu.au/s/search.html?clicked_fluster=electrical+and+electronic&cluster0=Electrical&query=%60Electrical+and+Electronic%60&collection=people&start_rank=41",
        "https://search.unisa.edu.au/s/search.html?clicked_fluster=electrical+and+electronic&cluster0=Electrical&query=%60Electrical+and+Electronic%60&collection=people&start_rank=51",
        "https://search.unisa.edu.au/s/search.html?clicked_fluster=electrical+and+electronic&cluster0=Electrical&query=%60Electrical+and+Electronic%60&collection=people&start_rank=61",
        "https://search.unisa.edu.au/s/search.html?clicked_fluster=electrical+and+electronic&cluster0=Electrical&query=%60Electrical+and+Electronic%60&collection=people&start_rank=71",
        "https://search.unisa.edu.au/s/search.html?clicked_fluster=electrical+and+electronic&cluster0=Electrical&query=%60Electrical+and+Electronic%60&collection=people&start_rank=81",
        "https://search.unisa.edu.au/s/search.html?clicked_fluster=electrical+and+electronic&cluster0=Electrical&query=%60Electrical+and+Electronic%60&collection=people&start_rank=91"
    ]

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0'}

    all_profs = []

    for url in urls:
        r = requests.get(url, headers=headers, verify=False)
        soup = BeautifulSoup(r.text, "html.parser")
        print("Fetching URL..." + url + "\n")
        super_class = soup.find('ol', {'class': 'list-unstyled', 'id': 'search-results'})
        if super_class:
            all_profs += super_class.find_all('li', {'data-fb-result': True})
        else:
            print("No data found for URL..." + url + "\n")
        print("Fetched from URL..." + url + "\n")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of South Australia done...\n")
    faculty_data = [list(item) for item in set(tuple(sublist) for sublist in faculty_data)]
    return faculty_data


if __name__ == '__main__':
    uni_south_australia()