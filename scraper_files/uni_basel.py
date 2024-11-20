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

u_name = "University of Basel"
country = "Switzerland"

all_faculty_uni_basel = []

def get_faculty_data(link, headers):
    global all_faculty_uni_basel
    all_faculty_uni_basel += search_faculty_list(link, headers, u_name, country)[0]

def uni_basel():
    global all_faculty_uni_basel
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=g_4sALY0__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=H6xtAIx2__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=iQwDAG6X__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=5zQVARCv__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=lzx5AUS6__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=-Xu-AIDB__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=KnvzAKzF__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=rsEaAKDP__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=yvEYALrT__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=SeeDAMDX__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=KjICAJfa__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=-FYnADzd__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=n33BAJ3f__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=om64ABHi__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=vIraAKnk__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=LtMLAKzm__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=s7-lAXvp__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=rPeFAGzr__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=nQQpAebs__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=jscVALXu__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=hUIRAL3v__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=cEC5Advw__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=jHhRAdvx__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=K-qKANny__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=NZ2oAJvz__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=QUyiAHn0__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=AxFbAN70__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=c42nAE31__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=5jY6AQb2__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=ruQCAKj2__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=NFIyADb3__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=Yv6oAIL3__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=mG5CAdv3__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=ZnceACX4__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=Q5oQAG_4__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=2wruAOT4__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=k8BDACT5__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=i6fpAIX5__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=VzQwAOH5__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=ruG0ATf6__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=tcVYAX76__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=DKqCAcL6__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=GK4ZADf7__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=FXT7AGH7__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=ucR_Aab7__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=CUwJANr7__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=vRevABj8__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=sn72AFL8__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=J4YFAHb8__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=evivAMH8__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=zR-hAO78__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=K68RAAv9__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=JjmBACj9__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=zXnUAEL9__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=M4qLAV79__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=BhcMAHb9__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=XLmhAZb9__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=opVqAbr9__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=dzbnANv9__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1863479039191187439&after_author=ADNuAP_9__8J&astart=600',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Basel done...\n")
    all_faculty_uni_basel = [list(item) for item in set(tuple(sublist) for sublist in all_faculty_uni_basel)]
    return all_faculty_uni_basel

if __name__ == "__main__":
    uni_basel()