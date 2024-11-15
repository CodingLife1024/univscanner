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

u_name = "PSL University"
country = "France"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def psl_uni():
    global all_faculty
    links = [
        "https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=psl+university",
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=psl+university&after_author=tP4DAGOb__8J&astart=10',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=psl+university&after_author=ru4tAYrN__8J&astart=20',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=psl+university&after_author=R1aZAOTk__8J&astart=30',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=psl+university&after_author=OtG4AUnq__8J&astart=40',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=psl+university&after_author=mx4XAI3v__8J&astart=50',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=psl+university&after_author=teIeAALz__8J&astart=60',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=psl+university&after_author=3AQsALD0__8J&astart=70',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=psl+university&after_author=Vz0eAJT2__8J&astart=80',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=psl+university&after_author=ddcRAD35__8J&astart=90',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=psl+university&after_author=wqBlAPP6__8J&astart=100',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=psl+university&after_author=cy4yARX8__8J&astart=110',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=psl+university&after_author=6mFaAA39__8J&astart=120',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=psl+university&after_author=5SEiAWT9__8J&astart=130',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=psl+university&after_author=0CAVAcz9__8J&astart=140',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=psl+university&after_author=LGGnAUf-__8J&astart=150',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=psl+university&after_author=tVgbAcP-__8J&astart=160',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=psl+university&after_author=CTurAAP___8J&astart=170',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=psl+university&after_author=Kz22AVP___8J&astart=180',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=psl+university&after_author=g7vLAID___8J&astart=190',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=psl+university&after_author=DHVNAbb___8J&astart=200',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=psl+university&after_author=E5BcAcP___8J&astart=210',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=psl+university&after_author=ZrL3ANj___8J&astart=220',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=psl+university&after_author=M9VdAeL___8J&astart=230',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=psl+university&after_author=9lBPAer___8J&astart=240',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=psl+university&after_author=7R9XAfH___8J&astart=250',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=psl+university&after_author=Kc7CAfX___8J&astart=260',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=psl+university&after_author=0BiGAfn___8J&astart=270',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=psl+university&after_author=0A95Afz___8J&astart=280',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nPSL University done...\n")
    all_faculty = [list(item) for item in set(tuple(sublist) for sublist in all_faculty)]
    return all_faculty

if __name__ == "__main__":
    psl_uni()