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

u_name = "University of Auckland"
country = "New Zealand"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def uni_auckland():
    global all_faculty
    links = [
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=6458948531608421033",
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6458948531608421033&after_author=bU0uAMw6__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6458948531608421033&after_author=qFwCAFV8__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6458948531608421033&after_author=KgoiACOP__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6458948531608421033&after_author=_9gDAA6k__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6458948531608421033&after_author=5bEBAAit__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6458948531608421033&after_author=QD0BAA-4__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6458948531608421033&after_author=yCpPADK8__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6458948531608421033&after_author=eaRaAITA__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6458948531608421033&after_author=5dUDAAvF__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6458948531608421033&after_author=T1A1AZfJ__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6458948531608421033&after_author=RC0BALDN__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6458948531608421033&after_author=2NoAAMrP__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6458948531608421033&after_author=HhwBAErS__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6458948531608421033&after_author=HzX2AHrT__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6458948531608421033&after_author=QORJAFjW__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6458948531608421033&after_author=Rz4CAN7Y__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6458948531608421033&after_author=6HgAAMjc__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6458948531608421033&after_author=KfohAHrd__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6458948531608421033&after_author=bDUBAC3f__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6458948531608421033&after_author=RqsKAPrf__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6458948531608421033&after_author=7e4LAKXh__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6458948531608421033&after_author=DwIZABnj__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6458948531608421033&after_author=kPgvAMPk__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6458948531608421033&after_author=Tg0FAG7m__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6458948531608421033&after_author=_pEAALLn__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6458948531608421033&after_author=A0IPAHXp__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6458948531608421033&after_author=CzDHAeHp__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6458948531608421033&after_author=Sd9EAIHq__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6458948531608421033&after_author=n3gBACzr__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6458948531608421033&after_author=ENIHAI3r__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6458948531608421033&after_author=EwyOAP_r__8J&astart=310',
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Auckland done...\n")
    # print(len(all_faculty))
    return all_faculty

if __name__ == "__main__":
    uni_auckland()