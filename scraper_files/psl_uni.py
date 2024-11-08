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

u_name = "PSL University"
country = "France"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def psl_uni():
    global all_faculty
    links = [
        "https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=psl+university",
        "https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=psl+university&before_author=6HRq_54vAAAJ&astart=10",
        "https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=psl+university&after_author=ru4tAYrN__8J&astart=20",
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nPSL University done...\n")
    # print(len(all_faculty))
    return all_faculty

if __name__ == "__main__":
    psl_uni()