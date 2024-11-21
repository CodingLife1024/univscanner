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

u_name = "University of Dundee"
country = "United Kingdom"

all_faculty_uni_dundee = []

def get_faculty_data(link, headers):
    global all_faculty_uni_dundee
    all_faculty_uni_dundee += search_faculty_list(link, headers, u_name, country)[0]

def uni_dundee():
    global all_faculty_uni_dundee
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=kfLrAGRM__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=bmDJAMGC__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=k7_JAL-q__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=G30kAO6___8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=KuMCAHzK__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=wm7IAPXT__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=f-Z2AYvX__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=cBPNAMfe__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=KwIIAETj__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=hgEfAB_p__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=gMEvAOzr__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=OyZRAYXu__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=EbWHAEbw__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=B8ZNAR7y__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=FyYYAK7z__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=0e9hANz0__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=DPgeAKX1__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=L8CPAOn2__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=XLEOAbv3__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=KF_fAEL4__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=V4AGAN34__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=J4_pAI_5__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=fzNvAOn5__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=BPwQATr6__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=wNhaANP6__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=jPpnAEf7__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=Rd7iANb7__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=rY0nACf8__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=FwHSAGn8__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=2upBAar8__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=SGNBAej8__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=Voo-ACL9__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=6AdpAFr9__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=aB1uAYH9__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=DLalAND9__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1238205835755504041&after_author=gUK4AAj-__8J&astart=360',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Dundee done...\n")
    all_faculty_uni_dundee = [list(item) for item in set(tuple(sublist) for sublist in all_faculty_uni_dundee)]
    return all_faculty_uni_dundee

if __name__ == "__main__":
    uni_dundee()