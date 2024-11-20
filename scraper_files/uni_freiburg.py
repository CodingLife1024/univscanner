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

u_name = "University of Freiburg"
country = "Germany"

all_faculty_uni_freiburg = []

def get_faculty_data(link, headers):
    global all_faculty_uni_freiburg
    all_faculty_uni_freiburg += search_faculty_list(link, headers, u_name, country)[0]

def uni_freiburg():
    global all_faculty_uni_freiburg
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=lgONAPdZ__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=8McBAQuF__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=l9kIAOCd__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=w-E7AB6u__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=hxKPAE-7__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=XQRCAXrC__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=VfuWAGXJ__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=thZbAALR__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=x3lAAMnU__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=7G0dACjZ__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=dNQBAHfc__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=FoQPAFff__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=HtJpAHng__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=J8LvAAjj__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=NRp8AObk__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=rGcEAC7m__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=fYoOAEnp__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=vdWSAGjq__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=JzscAAbs__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=HzetAHbt__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=4VOQAJ_u__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=J7QJAIXv__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=XB17AMLw__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=yrj4ANPx__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=SJCOAOjy__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=xKM8AMfz__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=lHUcAMf0__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=KDJ6AEv1__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=g5UEAEv2__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=1lU4AK72__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=wVqHAA33__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=VUYrAHL3__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=vl1OABj4__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=42sGAHP4__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=wv2PANX4__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=sAAeACP5__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=oP6rAI_5__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=lEaEAN75__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=Bp0bATD6__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=4ojAAHj6__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=Ljn_ALv6__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=HkncAAn7__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=oByhAE_7__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=7W1AAI77__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=nk_9AMD7__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=oK34APL7__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=7PSIAB38__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=Zt4NAFH8__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=XQwLAY38__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=beIKAcj8__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=ZaKxAeL8__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=sbXgABD9__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=36N9ACf9__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=BPsqAD39__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=ZzU_AFH9__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=U-kdAGz9__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=oUG5AIL9__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=jTUWAZj9__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=yOEMALf9__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=EEaYAND9__8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3300613556519769823&after_author=bb83Aez9__8J&astart=610',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Freiburg done...\n")
    all_faculty_uni_freiburg = [list(item) for item in set(tuple(sublist) for sublist in all_faculty_uni_freiburg)]
    return all_faculty_uni_freiburg

if __name__ == "__main__":
    uni_freiburg()