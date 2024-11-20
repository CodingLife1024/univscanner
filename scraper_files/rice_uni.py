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

u_name = "Rice University"
country = "United States"

all_faculty_rice_uni = []

def get_faculty_data(link, headers):
    global all_faculty_rice_uni
    all_faculty_rice_uni += search_faculty_list(link, headers, u_name, country)[0]

def rice_uni():
    global all_faculty_rice_uni
    links = [
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=11940724553757128128",
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=11940724553757128128&after_author=bJxCABvy_v8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=11940724553757128128&after_author=DNSTANtH__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=11940724553757128128&after_author=TDsSAFhp__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=11940724553757128128&after_author=4fZCANeQ__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=11940724553757128128&after_author=gfJGAB-f__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=11940724553757128128&after_author=4MwTALqs__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=11940724553757128128&after_author=QIcVAE-z__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=11940724553757128128&after_author=rQ08AHy7__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=11940724553757128128&after_author=rAIBAHTH__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=11940724553757128128&after_author=TCd2AcPL__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=11940724553757128128&after_author=YKsDAHXP__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=11940724553757128128&after_author=pBw-AJTS__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=11940724553757128128&after_author=aPRaAPzX__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=11940724553757128128&after_author=IFWDAOzZ__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=11940724553757128128&after_author=InEFAGTb__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=11940724553757128128&after_author=NjZfAHjd__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=11940724553757128128&after_author=JwACAAPg__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=11940724553757128128&after_author=qwQHAJ3j__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=11940724553757128128&after_author=ezAgACXl__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=11940724553757128128&after_author=gQqPAB7m__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=11940724553757128128&after_author=6zYBAN7n__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=11940724553757128128&after_author=4k4jAEbp__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=11940724553757128128&after_author=CPowACHq__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=11940724553757128128&after_author=S6w8ABnr__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=11940724553757128128&after_author=DAcoAFfs__8J&astart=250',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nRice University done...\n")
    all_faculty_rice_uni = [list(item) for item in set(tuple(sublist) for sublist in all_faculty_rice_uni)]
    return all_faculty_rice_uni

if __name__ == "__main__":
    rice_uni()