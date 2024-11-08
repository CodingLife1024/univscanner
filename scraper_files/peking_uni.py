import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures
import pprint

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.GLOBAL_VARIABLES import *
from components.gscholar_indiv_page import search_faculty_list

u_name = "Peking University"
country = "China"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def peking_uni():
    global all_faculty
    links = [
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=S-wgAAc1__8J&astart=10",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=oqACAPFs__8J&astart=20",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=anRiAL59__8J&astart=30",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=kK8BAIGS__8J&astart=40",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=aY4TAAej__8J&astart=50",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=k5UFANyw__8J&astart=60",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=V8YQAK2z__8J&astart=70",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=Uu0sAL64__8J&astart=70",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=6V5aAOS7__8J&astart=80",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=4nnNAbfD__8J&astart=90",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=s__UANLF__8J&astart=100"
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nPeking University done...\n")
    # print(len(all_faculty))
    return all_faculty

if __name__ == "__main__":
    peking_uni()