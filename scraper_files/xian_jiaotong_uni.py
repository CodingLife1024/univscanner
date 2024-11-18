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

u_name = "Xi’an Jiaotong University"
country = "China"

all_faculty_xian_jiaotong_uni = []

def get_faculty_data(link, headers):
    global all_faculty_xian_jiaotong_uni
    all_faculty_xian_jiaotong_uni += search_faculty_list(link, headers, u_name, country)[0]

def xian_jiaotong_uni():
    global all_faculty_xian_jiaotong_uni
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=12584268802548929965',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4109524060791268206&after_author=r-IHABXK__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4109524060791268206&after_author=h18xAM_Y__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4109524060791268206&after_author=ydsVAP3i__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4109524060791268206&after_author=jskEAAPq__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4109524060791268206&after_author=EZQEAN7w__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4109524060791268206&after_author=aO0JAPH1__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4109524060791268206&after_author=UfEsAEL4__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4109524060791268206&after_author=VDADANj5__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4109524060791268206&after_author=-uUwAPf6__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4109524060791268206&after_author=N5geAKr7__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4109524060791268206&after_author=kdOgANT8__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4109524060791268206&after_author=GLNNADD9__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4109524060791268206&after_author=TxPcAKv9__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4109524060791268206&after_author=qZNLAAn-__8J&astart=140',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nXi’an Jiaotong University done...\n")
    all_faculty_xian_jiaotong_uni = [list(item) for item in set(tuple(sublist) for sublist in all_faculty_xian_jiaotong_uni)]
    return all_faculty_xian_jiaotong_uni

if __name__ == "__main__":
    xian_jiaotong_uni()