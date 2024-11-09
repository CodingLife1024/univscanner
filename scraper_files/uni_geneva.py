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

u_name = "University of Geneva"
country = "Belgium"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def uni_geneva():
    global all_faculty
    links = [
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=10449475872026600560",
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10449475872026600560&after_author=1K95ABfa_v8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10449475872026600560&after_author=OxIQAGBJ__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10449475872026600560&after_author=lU6ZAMt4__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10449475872026600560&after_author=APaEAbaL__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10449475872026600560&after_author=4EJgANqX__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10449475872026600560&after_author=s_s0AIeg__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10449475872026600560&after_author=BadFAGCq__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10449475872026600560&after_author=XqBjASqw__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10449475872026600560&after_author=5Ho3ALa6__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10449475872026600560&after_author=-BOiAV7D__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10449475872026600560&after_author=ehaSAFzI__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10449475872026600560&after_author=dDwGAA_M__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10449475872026600560&after_author=TZsCADfR__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10449475872026600560&after_author=AcUWASzV__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10449475872026600560&after_author=ycstAEnX__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10449475872026600560&after_author=zX0DABzZ__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10449475872026600560&after_author=MatfAGHb__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10449475872026600560&after_author=UjzTAKHd__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10449475872026600560&after_author=adwJANHf__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10449475872026600560&after_author=ymHHABXh__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10449475872026600560&after_author=LBvLAIni__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10449475872026600560&after_author=NGgbAKHk__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10449475872026600560&after_author=dNmoAPjl__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10449475872026600560&after_author=gnt5AJvn__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10449475872026600560&after_author=8W1SAZPo__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10449475872026600560&after_author=Cfg3AD7p__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10449475872026600560&after_author=gpUTAALq__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10449475872026600560&after_author=YwtwAbrq__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10449475872026600560&after_author=8eMCAOvr__8J&astart=290',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Geneva done...\n")
    # print(len(all_faculty))
    return all_faculty

if __name__ == "__main__":
    uni_geneva()