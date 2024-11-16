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

u_name = "King Abdulaziz University"
country = "Saudi Arabia"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def king_abdulaziz_uni():
    global all_faculty
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=C-UJAHWh__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=ojkSAL3S__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=Mpj5AM3W__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=-mgjADve__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=mEO8AOzi__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=fyAAAPXl__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=1I0zAJ7o__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=f4qGAB_s__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=Vpn1AAPu__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=f0aXAB7w__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=0yoLACHy__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=2VJjAf_y__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=6V-EAK_z__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=5q4JACT1__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=8HWmAZ_1__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=JqIEAUn2__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=F6h6Afb2__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=4QKUAF73__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=NPr4ALb3__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=D2UWAPz3__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=veIpADX4__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=KuOTAK74__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=KCgcABH5__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=KGtlAHL5__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=AZRSAbD5__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=wLEHAPH5__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=KotEAD_6__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=y63nAGj6__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=ASKiAaP6__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=7jc-ANH6__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=-aXUAAX7__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=mJ1KASn7__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=VtmdAE_7__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=g3EdAHf7__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=1o-DAaz7__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=WWRBANb7__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=YpW2Afb7__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=SeW-ABH8__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=lamNADn8__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=xIZ4AFf8__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=FJWzAIT8__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=8AcXAJv8__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=c7n5ALD8__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=xQrjAND8__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=F60GAeT8__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=XvHgAP78__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=TKCIAA79__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=4PeEACf9__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=ZujYAC_9__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=73SUAUX9__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=UsdPAVz9__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=_OGwAG79__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=jceyAXn9__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=pmzrAIf9__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=8CtVAZf9__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=8mx5AK39__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=WrGPAbv9__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=9x6FAcb9__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=qrgvANL9__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=_VSkAPD9__8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6897943823519411289&after_author=B2eUAAf-__8J&astart=610',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nKing Abdulaziz University done...\n")
    all_faculty = [list(item) for item in set(tuple(sublist) for sublist in all_faculty)]
    return all_faculty

if __name__ == "__main__":
    king_abdulaziz_uni()