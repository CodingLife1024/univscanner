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

u_name = "University of California, Los Angeles"
country = "United States"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def uc_los_angeles():
    global all_faculty
    links = [
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=14108176128635076915",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=14108176128635076915&after_author=x_4AAJi4_f8J&astart=10",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=14108176128635076915&after_author=eyMiALom_v8J&astart=20",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=14108176128635076915&after_author=q5QAANZ0_v8J&astart=30",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=14108176128635076915&after_author=lQFgAAi1_v8J&astart=40",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=14108176128635076915&after_author=TQafABzk_v8J&astart=50",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=14108176128635076915&after_author=MHD7AODw_v8J&astart=60",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=14108176128635076915&after_author=nB0CAJQS__8J&astart=70",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=14108176128635076915&after_author=99p8AJMh__8J&astart=80",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=14108176128635076915&after_author=SN5oAGEw__8J&astart=90",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=14108176128635076915&after_author=7QxzANc7__8J&astart=100",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=14108176128635076915&after_author=CC0BABNE__8J&astart=110",
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of California, Los Angeles done...\n")
    all_faculty = [list(item) for item in set(tuple(sublist) for sublist in all_faculty)]
    return all_faculty

if __name__ == "__main__":
    uc_los_angeles()