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

u_name = "Indian Institute of Technology, Mumbai"
country = "India"

all_faculty_iit_bombay = []

def get_faculty_data(link, headers):
    global all_faculty_iit_bombay
    all_faculty_iit_bombay += search_faculty_list(link, headers, u_name, country)[0]

def iit_bombay():
    global all_faculty_iit_bombay
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=t4MYALa8__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=awVMAU7P__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=gQIJAOvV__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=UvgTAAvd__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=DIywAPzg__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=-T0GABPk__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=rjY3AELp__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=k9OfAfnq__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=3-y6AOHs__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=bmAwAeft__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=9lMGACHv__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=Wo8CAArw__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=m8QlAEPx__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=7a0BAAby__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=6moPADzz__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=VGD4APHz__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=29goAJ_0__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=9EcoADP1__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=YWJqAKz1__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=1wiEAGf2__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=SKAGABD3__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=U5QyAJX3__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=RSf9AAL4__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=jW4BAG74__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=W203AKn4__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=WucmANv4__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=7WwGAGr5__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=Ra6wAM_5__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=I9z3ABv6__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=p6yPAW36__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=hFUgAK_6__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=asElANX6__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=DLAeACf7__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=ew5bAHf7__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=TTf4ALn7__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=r5nZAO77__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=TbsvACL8__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=JqOSATr8__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=oSABAHH8__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=gzUCAJL8__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=vNH5ALP8__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=UbATANb8__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=dG4kAfj8__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=XgtdABT9__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=VFmOADL9__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=e6cYAFT9__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=5FzPAG_9__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=2mvaAJL9__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=jt6HAKn9__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=PzZkAMP9__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=yMQIANf9__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=szAdAOn9__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15559271020991466530&after_author=w-_SAPz9__8J&astart=530',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nIndian Institute of Technology, Mumbai done...\n")
    all_faculty_iit_bombay = [list(item) for item in set(tuple(sublist) for sublist in all_faculty_iit_bombay)]
    return all_faculty_iit_bombay

if __name__ == "__main__":
    iit_bombay()