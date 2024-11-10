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

u_name = "University of Gothenburg"
country = "Sweden"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def uni_gothenburg():
    global all_faculty
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=p0PpABNJ__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=QvNbADBs__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=l135AN6J__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=kGzFAIym__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=1F2cAOS1__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=S4MjACi___8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=9HYdACTG__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=buEEAM3J__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=rfyXAOnM__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=uWQdAD7Q__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=lyoZAGvT__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=4XNyAWbV__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=XfkHAY7X__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=OwwBAJba__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=5g1wANfc__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=v8xsAB_e__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=ro9mAMvf__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=euAJATri__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=DAjAAB_k__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=LsO0ASPl__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=5NVpAAHn__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=GuFVAETo__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=hF8CAA7p__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=LJChAPDp__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=KacnAObq__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=2ob7AMXr__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=Q86NAZvs__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=wckBAHHt__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=nmoKAPDt__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=lb5EAO_u__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=yebwAF3v__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=dzUGAPfv__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=VtwGAM3w__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=El5LAI3x__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=xYAeADXy__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=6aY8AKvy__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=P9UHAAPz__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=mPiXAG_z__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=6HJaAfvz__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=UA0eAH70__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=2SdEAPH0__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=aHCtACn1__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=_7dAAIH1__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=fAB4AMz1__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=l4GNABP2__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=7z1lAGb2__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=iE8NALr2__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=rN8mAf72__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=IMkCAFb3__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=7OqYALT3__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=B4gzAOb3__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=aWK2ADD4__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=JeoaAH_4__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=VzYLAKr4__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=FgUHAen4__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=0t9-AQ_5__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=dBSQAEL5__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=jXFaAWv5__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=7Sa8ALD5__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=HNGtANv5__8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=j_46ABr6__8J&astart=610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=wraWAC36__8J&astart=620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=ijwgAWH6__8J&astart=630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=pkjgAKb6__8J&astart=640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=CUwIALb6__8J&astart=650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=-NYYAND6__8J&astart=660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=PvO9AOj6__8J&astart=670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=3DcoAfv6__8J&astart=680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=yoWZACj7__8J&astart=690',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=8zTLAF77__8J&astart=700',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=7PqCAHb7__8J&astart=710',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=LskTAKX7__8J&astart=720',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=9coeAMz7__8J&astart=730',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=wCzMAeH7__8J&astart=740',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=kDZrAPX7__8J&astart=750',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=-B9BABH8__8J&astart=760',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=87YAACr8__8J&astart=770',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=KyyHADX8__8J&astart=780',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=G_hTAU_8__8J&astart=790',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=wITRAGb8__8J&astart=800',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=GFJ7AIv8__8J&astart=810',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=wzwXAab8__8J&astart=820',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=3vZ0AMf8__8J&astart=830',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=bU9YANv8__8J&astart=840',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=N60GAfT8__8J&astart=850',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=swtSAPr8__8J&astart=860',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=U04LAAf9__8J&astart=870',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=sb1RABv9__8J&astart=880',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=ZOgpADP9__8J&astart=890',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=ULL3AEP9__8J&astart=900',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=jQCeAFj9__8J&astart=910',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=dritAG39__8J&astart=920',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=Nuo7AIL9__8J&astart=930',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=eW6WAZX9__8J&astart=940',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=W_oeAKv9__8J&astart=950',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=5-YZAL_9__8J&astart=960',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=20ZtANf9__8J&astart=970',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=XPOAAOb9__8J&astart=980',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=mUMdAfb9__8J&astart=990',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=16819010087144438317&after_author=zrcTAf_9__8J&astart=1000',
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Gothenburg done...\n")
    # print(len(all_faculty))
    return all_faculty

if __name__ == "__main__":
    uni_gothenburg()