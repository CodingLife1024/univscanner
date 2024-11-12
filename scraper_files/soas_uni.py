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

u_name = "School of Oriental and African Studies, London"
country = "United Kingdom"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def soas_uni():
    global all_faculty
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=4awdAFPl__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=DHFAAB7t__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=eC2EAb3w__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=2SsEANn0__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=ilNKANr2__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=2k2_AGD4__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=G3UjAEn5__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=7J4RALX6__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=mQBkAXv7__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=kO2TAPL7__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=swyXAH_8__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=HhIkAPX8__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=tpxjAID9__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=lZlkAMf9__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=2vAPAQb-__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=SX4RAVn-__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=Y_wPAaf-__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=oLoQAcn-__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=sq8AAPn-__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=vljLABL___8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=41SuAC3___8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=kuIPAVD___8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=jwD6AGv___8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=xAMNAHn___8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=JzjjAI3___8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=OExxAZz___8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=QL9VAar___8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=7nX1ALT___8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=P8-LAMP___8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=8qBKAdD___8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=c2GRANb___8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=97nTANn___8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=NF35AOL___8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=wst8Aen___8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=uEpiAez___8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=ue9vAfD___8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=jCWzAPP___8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=aNwfAfX___8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=q5QCAff___8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=gBT_APn___8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=y-hrAfr___8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3380056149308678727&after_author=-ZC_Afv___8J&astart=420',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nSchool of Oriental and African Studies, London done...\n")
    # print(len(all_faculty))
    return all_faculty

if __name__ == "__main__":
    soas_uni()