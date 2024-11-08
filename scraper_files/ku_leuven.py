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

u_name = "Katholieke Universiteit, Leuven"
country = "Belgium"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def ku_leuven():
    global all_faculty
    links = [
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529",
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=zCEiAG_g_v8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=p7FaAXYZ__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=ufpxAIBJ__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=zkcHAH5i__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=wD8CAHl1__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=Vq8IAMCB__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=yjP3AMKP__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=dghCAfCS__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=obWkAKGX__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=XdsEAN-a__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=kxRXAC6g__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=8uovAGak__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=XjwCALyr__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=RowEAEKu__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=U5CnALSy__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=Cmf3AG23__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=KFDkADG6__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=-hQHAAW8__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=O0AAABq-__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=7d0dAT7C__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=rOsFAFjG__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=hwkRAMzI__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=TPgAAE_K__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=knhlALDL__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=N1unAe3N__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=wc5SAAzQ__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=qcgFAEnS__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=RbYOANzT__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=jNwXANPV__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=T9B_AArX__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=yjUEABzY__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=QDIiAFvZ__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=xNMaAXTb__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=5r5cAKrc__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=_xMiAMvd__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=hk4-ADHf__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=45wYAe3f__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=8z7DAHPg__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=qpgzAXrh__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=0UASAE7i__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=4CfQAE7j__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=ICJTAPPj__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=SsItACTl__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=MYcqAOjl__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=DlImANrm__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=NJ7SAMXn__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=9ycGASro__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=cUoEAObo__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=wS0QAGrp__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=VmQxAT_q__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=5pTFAPXq__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=1sQDAHXr__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8645310392855763529&after_author=Huj2APHr__8J&astart=530',
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nKatholieke Universiteit, Leuven done...\n")
    # print(len(all_faculty))
    return all_faculty

if __name__ == "__main__":
    ku_leuven()