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

u_name = "Chalmers University of Technology"
country = "Sweden"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def chalmers_uni():
    global all_faculty
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232'
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=SytGAEOs__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=YLklABG8__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=duIOAEPF__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=VkLrADzN__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=ubUdABXQ__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=9aq7AB_U__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=NOEOAE3W__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=dakBAOjZ__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=mzoOAD7c__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=VGIAAM3e__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=F-yEAKXi__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=0xoZAH3k__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=ekIQAHPm__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=1FSuAIfn__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=kNACAMLo__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=M0kCAIXq__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=UAIMALXr__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=WNu2ALzs__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=Ks0AAFjt__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=FlADAPLt__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=BF4PAAnv__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=TW5YAMLv__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=CewfAC7w__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=BL4QAL7w__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=y8l3AHPx__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=ixsdAMnx__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=XYsZAE3y__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=4KQNAKry__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=vToeACfz__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=PtUSAJ7z__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=XWEBAPfz__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=_sUEAIn0__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=_5a4AA71__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=8miEAE71__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=KmC4AKD1__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=W-lCAAb2__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=ovh7AEH2__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=EuwaAI72__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=heoAALv2__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=M10PAPr2__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=aoQNACX3__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=eyZUAFz3__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=4G49AL73__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=8SYEAOj3__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=lPsQARH4__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=IKyJAE_4__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=0_caAKL4__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=W60QAOP4__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=YascACX5__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=4LMGAEv5__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=Tp1nAYv5__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=kigjAKj5__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=ycQVANj5__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=Nw1KAOz5__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=5Dg5AD36__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=EFKTAF_6__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=UKIBALH6__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=uwA_ANf6__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=r11bAPP6__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=xRZ_ACf7__8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=eeCRAED7__8J&astart=610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=NBMOAFv7__8J&astart=620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=xH7iAIL7__8J&astart=630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=OPe2AKv7__8J&astart=640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=gQaHAMr7__8J&astart=650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=3POYANr7__8J&astart=660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=W7rWAPz7__8J&astart=670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=hhONADH8__8J&astart=680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=tf4RAFv8__8J&astart=690',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=YIMLAIj8__8J&astart=700',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=UrGZAaz8__8J&astart=710',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=QjFqAcT8__8J&astart=720',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=Nrk9AOP8__8J&astart=730',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=StMVAAD9__8J&astart=740',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=kEWpAB_9__8J&astart=750',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=VJ3bADT9__8J&astart=760',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=8BGRAE39__8J&astart=770',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=gcsoAFz9__8J&astart=780',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=eiFTAG79__8J&astart=790',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=noZMAH_9__8J&astart=800',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=vQ9gAJf9__8J&astart=810',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=UpmoALT9__8J&astart=820',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=PgrSAMH9__8J&astart=830',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=XFPeANf9__8J&astart=840',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=MJPHAPL9__8J&astart=850',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=XYwcAPv9__8J&astart=860',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4746383261807430232&after_author=1X5-AAb-__8J&astart=870',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nChalmers University of Technology done...\n")
    # print(len(all_faculty))
    return all_faculty

if __name__ == "__main__":
    chalmers_uni()