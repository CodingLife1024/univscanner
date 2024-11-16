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

u_name = "Vrije Universiteit Brussel"
country = "Belgium"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def vrije_uni_brussel():
    global all_faculty
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3275235718540563127',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3275235718540563127&after_author=hwGHADO8__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3275235718540563127&after_author=juoEAHHZ__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3275235718540563127&after_author=nH0DAGPm__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3275235718540563127&after_author=A2dSAF_s__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3275235718540563127&after_author=H4Y5APLw__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3275235718540563127&after_author=XM8EADH1__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3275235718540563127&after_author=bo1tABb3__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3275235718540563127&after_author=eVFvAHb4__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3275235718540563127&after_author=G0oLAAH6__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3275235718540563127&after_author=pT8YALv6__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3275235718540563127&after_author=U1UCAKD7__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3275235718540563127&after_author=fdgGAEL8__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3275235718540563127&after_author=cqoQAMz8__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3275235718540563127&after_author=Nv25AJH9__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3275235718540563127&after_author=FTd1AAD-__8J&astart=150',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nVrije Universiteit Brussel done...\n")
    all_faculty = [list(item) for item in set(tuple(sublist) for sublist in all_faculty)]
    return all_faculty

if __name__ == "__main__":
    vrije_uni_brussel()