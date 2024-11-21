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

u_name = "University of Strathclyde"
country = "United Kingdom"

all_faculty_uni_strathclyde = []

def get_faculty_data(link, headers):
    global all_faculty_uni_strathclyde
    all_faculty_uni_strathclyde += search_faculty_list(link, headers, u_name, country)[0]

def uni_strathclyde():
    global all_faculty_uni_strathclyde
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=GnzIAGaR__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=QhEBAOq2__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=XY1MAJvQ__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=rkV8AMfY__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=DV6CAKzd__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=-CEDABXh__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=m8x3AK_i__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=TpgIAQvm__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=yef-AJjn__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=zEkLAKfp__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=ATJHAMjq__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=cmQSAO3r__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=NwA8AO3s__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=VUd6AOXt__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=CNYgAMru__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=W7FZAMvv__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=J4EFAMPw__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=R8CDAI_x__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=4R6eAC7y__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=anDmAMXy__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=m-hcAEHz__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=kP0NAO_z__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=gViBAEH0__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=b00IANX0__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=JtsdASj1__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=BfEYAIr1__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=bX6kAOn1__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=t3EkADT2__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=fLsgALD2__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=UYh7AAD3__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=uYg_AFn3__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=YMoBANv3__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=B-uDAS_4__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=aPc0AJr4__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=jL96AP74__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=Rqg_AEj5__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=j17aAJL5__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=CuOTAMP5__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=2XcBACD6__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=QTkkAHX6__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=aC6TALj6__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=I3EXAPH6__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=uEsrAED7__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=ke63AH77__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=ZM0MAK37__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=EFJlANb7__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=z162AAT8__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=tviFAC78__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=V-p5AGP8__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=iuwSAJ78__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=JpmCAOf8__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=zLsTAP78__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=MvYTABj9__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=my-HADT9__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=fdzrAFP9__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=S3iBAHP9__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=RUD1AKP9__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=rVWzAMn9__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=moGDAN79__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13353641271671502880&after_author=OpU0AQH-__8J&astart=600',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Strathclyde done...\n")
    all_faculty_uni_strathclyde = [list(item) for item in set(tuple(sublist) for sublist in all_faculty_uni_strathclyde)]
    return all_faculty_uni_strathclyde

if __name__ == "__main__":
    uni_strathclyde()