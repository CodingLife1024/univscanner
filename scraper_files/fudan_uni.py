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
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13545734643759689096&after_author=uTUQAANb__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13545734643759689096&after_author=KfUJANSZ__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13545734643759689096&after_author=rhIuAN2p__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13545734643759689096&after_author=8EM9AL-1__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13545734643759689096&after_author=d4t9AGS-__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13545734643759689096&after_author=G4MhAPzE__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13545734643759689096&after_author=HLmBAH3L__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13545734643759689096&after_author=6tzwAGfQ__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13545734643759689096&after_author=fPCUACHU__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13545734643759689096&after_author=VBiBAOLX__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13545734643759689096&after_author=PfF8AMnZ__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13545734643759689096&after_author=OkVbAeXb__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13545734643759689096&after_author=ycawAD3e__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13545734643759689096&after_author=R6SuAG7g__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13545734643759689096&after_author=UM4AAKTi__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13545734643759689096&after_author=wiZQAIPk__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13545734643759689096&after_author=DAkrAEjn__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13545734643759689096&after_author=VlcDAFPo__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13545734643759689096&after_author=HrsTAP3p__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13545734643759689096&after_author=W1IYAMvq__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13545734643759689096&after_author=70I1ACrs__8J&astart=210',
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nFudan University done...\n")
    all_faculty = [list(item) for item in set(tuple(sublist) for sublist in all_faculty)]
    return all_faculty

if __name__ == "__main__":
    fudan_uni()