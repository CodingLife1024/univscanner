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

u_name = "Universidad Carlos III de Madrid"
country = "Spain"

all_faculty_carlos = []

def get_faculty_data(link, headers):
    global all_faculty_carlos
    all_faculty_carlos += search_faculty_list(link, headers, u_name, country)[0]

def universidad_carlos_de_madrid():
    global all_faculty_carlos
    links = [
        "https://scholar.google.com/citations?view_op=view_org&org=14848478220935772690",
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=M7kKAM7X__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=P0EBAEDh__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=dTAKACDk__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=pEUEAP7m__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=mmQEAAfp__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=RStNAEzs__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=Tw2LAMDt__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=9KVHAAnv__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=Zl3uAFjw__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=v1yGACry__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=2EIBANny__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=6BCCADPz__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=gnRnABT0__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=k96AAOj0__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=35cCAHf1__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=o4iVAOz1__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=QHWBAJj2__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=r3JnAO_2__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=nGEhAEv3__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=OBxPAM33__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=GNwDADP4__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=sK5PAJb4__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=TyJSAA35__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=UO8aADf5__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=DXQEAH75__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=wY8BAMz5__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=uEKCAfb5__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=BjcAADb6__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=5YtlAFn6__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=MlxLAJb6__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=I35nAMT6__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=7aVRAO76__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=I4GtACP7__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=OSyOAGL7__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=DZcQAIr7__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=tJ9XALf7__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=g_ZmANj7__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=RKRFAA78__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=pJeEADL8__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=_kVoAF38__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=_vhPAIL8__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=U0WGAK_8__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=9hqsAL_8__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=Dl0FAN_8__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=-DcIAAb9__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=3B93ADD9__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=sUdSAFL9__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=Zqx1AF79__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=V5xnAH79__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=-RADAaP9__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=TrSUALv9__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=3fAMAdH9__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=-u9KAO_9__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14848478220935772690&after_author=6v7HAAD-__8J&astart=540',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversidad Carlos III de Madrid done...\n")
    all_faculty_carlos = [list(item) for item in set(tuple(sublist) for sublist in all_faculty_carlos)]
    return all_faculty_carlos

if __name__ == "__main__":
    universidad_carlos_de_madrid()