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

u_name = "North Eastern University"
country = "United States"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def north_eastern_uni():
    global all_faculty
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=R_EDAL5H__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=A5t4ACCi__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=b9BsAIiw__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=NH1EAEC7__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=Cn8AAKfE__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=7VV7ABHS__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=e8wUAOjY__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=6UkhAMzd__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=eNQQACLh__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=kT19ABTk__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=YfWSAN_m__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=XywBAPzn__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=edEeAInp__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=BdEGAO7q__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=37A1ALLs__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=JrkAAKXu__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=LoMAAI_w__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=amAKALjx__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=QtcMANby__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=W94uADH0__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=g48FAAj1__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=MPYrAPP1__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=pDcpAJ32__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=m3sYAK33__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=Zr-KAHL4__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=YjkWACP5__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=oIkZAE36__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=t00FAAb7__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=IERIAFP7__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=rBofAN77__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=XBgFAD38__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=uvkjAa_8__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=wwdoAOj8__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=zQYZACf9__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=UcYvAHP9__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=55793137512334013&after_author=pCs0AN79__8J&astart=360',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nNorth Eastern University done...\n")
    all_faculty = [list(item) for item in set(tuple(sublist) for sublist in all_faculty)]
    return all_faculty

if __name__ == "__main__":
    north_eastern_uni()