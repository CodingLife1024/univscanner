import concurrent.futures
import os
import pprint
import re
import sys

import requests
from bs4 import BeautifulSoup

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.GLOBAL_VARIABLES import *
from components.gscholar_indiv_page import search_faculty_list

u_name = "Pontifical Catholic University of Argentina"
country = "Argentina"

all_faculty_uca_argentina = []

def get_faculty_data(link, headers):
    global all_faculty_uca_argentina
    all_faculty_uca_argentina += search_faculty_list(link, headers, u_name, country)[0]

def uca_argentina():
    global all_faculty_uca_argentina
    links = [
        'https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=uca+argentina&btnG=',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=uca+argentina&after_author=9ty-ADjz__8J&astart=10',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=uca+argentina&after_author=DM23ADv5__8J&astart=20',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=uca+argentina&after_author=BsOIAU38__8J&astart=30',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=uca+argentina&after_author=Cd-3AJj9__8J&astart=40',
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nPontifical Catholic University of Argentina done...\n")
    all_faculty_uca_argentina = [list(item) for item in set(tuple(sublist) for sublist in all_faculty_uca_argentina)]
    return all_faculty_uca_argentina

if __name__ == "__main__":
    uca_argentina()