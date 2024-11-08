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

u_name = "Fudan University"
country = "China"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def fudan_uni():
    global all_faculty
    links = [
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=13545734643759689096",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=13545734643759689096&after_author=uTUQABBb__8J&astart=10",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=13545734643759689096&after_author=KfUJANSZ__8J&astart=20",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=13545734643759689096&after_author=rhIuAOep__8J&astart=30",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=13545734643759689096&after_author=8EM9AMi1__8J&astart=40",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=13545734643759689096&after_author=sTy7AGi-__8J&astart=50",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=13545734643759689096&after_author=G4MhAPrE__8J&astart=60",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=13545734643759689096&after_author=HLmBAIDL__8J&astart=70",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=13545734643759689096&after_author=6tzwAHfQ__8J&astart=80",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=13545734643759689096&after_author=fPCUACHU__8J&astart=90",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=13545734643759689096&after_author=VBiBAOLX__8J&astart=100",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=13545734643759689096&after_author=PfF8AMnZ__8J&astart=110"
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nFudan University done...\n")
    # print(len(all_faculty))
    return all_faculty

if __name__ == "__main__":
    fudan_uni()