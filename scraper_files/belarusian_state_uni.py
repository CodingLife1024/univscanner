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

u_name = "Belarusian State University"
country = "Belarus"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def belarusian_state_uni():
    global all_faculty
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=5521431868896417804',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=5521431868896417804&after_author=dHxHAOHQ__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=5521431868896417804&after_author=j8B2AJno__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=5521431868896417804&after_author=aDgUALTv__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=5521431868896417804&after_author=jSt5AP7z__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=5521431868896417804&after_author=hrKGAO71__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=5521431868896417804&after_author=6zh4AG73__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=5521431868896417804&after_author=skYVAN74__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=5521431868896417804&after_author=5VJ9AHL5__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=5521431868896417804&after_author=hgR5AAr6__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=5521431868896417804&after_author=b0ujAIz6__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=5521431868896417804&after_author=G-o_APv6__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=5521431868896417804&after_author=jcd2AC_7__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=5521431868896417804&after_author=BRPhAHX7__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=5521431868896417804&after_author=gZWlAOH7__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=5521431868896417804&after_author=XnGJABL8__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=5521431868896417804&after_author=By89AE38__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=5521431868896417804&after_author=tCB5AHL8__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=5521431868896417804&after_author=2il5AJr8__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=5521431868896417804&after_author=BaM-Acn8__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=5521431868896417804&after_author=a0SlAOT8__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=5521431868896417804&after_author=Njt5AAn9__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=5521431868896417804&after_author=HL_iAB_9__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=5521431868896417804&after_author=pYmAADn9__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=5521431868896417804&after_author=iiJ5AGP9__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=5521431868896417804&after_author=dwN0AHX9__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=5521431868896417804&after_author=zsp5AJP9__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=5521431868896417804&after_author=08CIAKf9__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=5521431868896417804&after_author=t9U9ALz9__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=5521431868896417804&after_author=UVxdAMj9__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=5521431868896417804&after_author=5MV7AN39__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=5521431868896417804&after_author=8AcbAOv9__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=5521431868896417804&after_author=B0R4AP79__8J&astart=320',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nBelarusian State University done...\n")
    # print(len(all_faculty))
    return all_faculty

if __name__ == "__main__":
    belarusian_state_uni()