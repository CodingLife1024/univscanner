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

u_name = "University of Sydney"
country = "United States"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def uni_sydney():
    global all_faculty
    links = [
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=FQwEAEpJ_v8J&astart=10",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=-5VQAJrP_v8J&astart=20",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=L7UGAHEP__8J&astart=30",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=-J0xAfAw__8J&astart=40",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=Z9IKAC5c__8J&astart=50",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=_J8DAOhs__8J&astart=60",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=ym2EALx6__8J&astart=70",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=B88AAKeC__8J&astart=80",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=kmF6ACyM__8J&astart=90",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=BP0mAMGU__8J&astart=100",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=C--aACqZ__8J&astart=110",
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Sydney done...\n")
    # print(len(all_faculty))
    return all_faculty

if __name__ == "__main__":
    uni_sydney()