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

u_name = "Hiroshima University"
country = "Japan"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def hiroshima_uni():
    global all_faculty
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13823484183041968306',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13823484183041968306&after_author=PSh-ADy2__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13823484183041968306&after_author=1ZWFAJrQ__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13823484183041968306&after_author=zO5qACzZ__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13823484183041968306&after_author=R4rOAGvf__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13823484183041968306&after_author=ESdtAIPi__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13823484183041968306&after_author=8PIAAGDp__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13823484183041968306&after_author=HJsTALHs__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13823484183041968306&after_author=pG2EAGjv__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13823484183041968306&after_author=N9L3AJvw__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13823484183041968306&after_author=M4vnAGby__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13823484183041968306&after_author=YeimAI3z__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13823484183041968306&after_author=K9sgAPP0__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13823484183041968306&after_author=MiWLAPP1__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13823484183041968306&after_author=Ebl5AKL2__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13823484183041968306&after_author=2bunAFj3__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13823484183041968306&after_author=tTxCAMr3__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13823484183041968306&after_author=w42QAXL4__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13823484183041968306&after_author=fjB6AGD5__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13823484183041968306&after_author=ZqRCACT6__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13823484183041968306&after_author=YJ0_AGv6__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13823484183041968306&after_author=_qEBAMH6__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13823484183041968306&after_author=w2FSAWb7__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13823484183041968306&after_author=12BDAL_7__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13823484183041968306&after_author=I_pKACf8__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13823484183041968306&after_author=oLFVAIf8__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13823484183041968306&after_author=6CoWAMf8__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13823484183041968306&after_author=kb6eACL9__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13823484183041968306&after_author=nEKqAF_9__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13823484183041968306&after_author=-t-5AJv9__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13823484183041968306&after_author=NZotAOb9__8J&astart=300',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nHiroshima University done...\n")
    all_faculty = [list(item) for item in set(tuple(sublist) for sublist in all_faculty)]
    return all_faculty

if __name__ == "__main__":
    hiroshima_uni()