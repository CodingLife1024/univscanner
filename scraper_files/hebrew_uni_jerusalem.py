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

u_name = "The Hebrew University of Jerusalem"
country = "Israel"

all_faculty_hebrew_uni_jerusalem = []

def get_faculty_data(link, headers):
    global all_faculty_hebrew_uni_jerusalem
    all_faculty_hebrew_uni_jerusalem += search_faculty_list(link, headers, u_name, country)[0]

def hebrew_uni_jerusalem():
    global all_faculty_hebrew_uni_jerusalem
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=cCJBAPsd__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=bLgNAJ9e__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=63MUANh5__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=mZgKAJ-K__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=N_9eAIqh__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=HEVEANuu__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=QM4PAAu2__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=QvU2Aeq7__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=YaphADrA__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=tIaqANLD__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=MDUJAYbI__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=KMEaAJnL__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=-xhkAB_P__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=risAADLS__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=hPiFAH7U__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=5-4uAOrV__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=ouQ5AJbY__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=CVQvAMza__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=AiRGAMnb__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=9ihRAEvc__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=GOgCANzd__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=_0kAAAnf__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=Tz4SAKfg__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=2Y0hAaPh__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=FDtIAG_i__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=WvsNAAnj__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=VEEOAEfk__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=zM_2AO3k__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=DN1rAPTl__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=SdK-AB3n__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=QEQCAKzn__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=Qb0GAKTo__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=94eKAJ7p__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=Q907AF7q__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=pDQGAAvr__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=VnEBADLs__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=njsXAKrs__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=Gy2XAFnt__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=_s8OACDu__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=KE4JAQ7v__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=J2cjAEnv__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=3ExAAMHv__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=QMM0ACvw__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=NxVPAcvw__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=0EkMAD7x__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=rN-BALrx__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=tlQBAEzy__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=ZUMXAMDy__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=oo0NAWTz__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=5rxkAabz__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=QS4DAAT0__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=kkT3AGn0__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=VcLYALv0__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=GkdUACD1__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=CYLOAFj1__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=adibAL31__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=q8sFABX2__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=3xFSAI72__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=cXweAMf2__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=o96vAAH3__8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=_2wCAIr3__8J&astart=610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=7N8eAOj3__8J&astart=620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=kFJtAED4__8J&astart=630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=O29BAGb4__8J&astart=640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=A69_AJv4__8J&astart=650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=teVAAdb4__8J&astart=660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=4pvFAAD5__8J&astart=670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=LsKFACr5__8J&astart=680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=OoxaAHv5__8J&astart=690',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=yvNzAK35__8J&astart=700',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=iSjGAPD5__8J&astart=710',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=Qbq4ABj6__8J&astart=720',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=Qzs7AT76__8J&astart=730',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=rZKbAFz6__8J&astart=740',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=Og0GAIn6__8J&astart=750',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=KUECAMf6__8J&astart=760',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=znOVAPn6__8J&astart=770',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=5aOOABv7__8J&astart=780',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=1nZDADL7__8J&astart=790',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=IvhRAFL7__8J&astart=800',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=vnhkAIL7__8J&astart=810',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=PQoCAa77__8J&astart=820',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=g099AOL7__8J&astart=830',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=BmR_APn7__8J&astart=840',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=HSGzADP8__8J&astart=850',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=vXlhAFb8__8J&astart=860',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=2TcCAXn8__8J&astart=870',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=r2a2AZT8__8J&astart=880',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=71UDAKL8__8J&astart=890',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=Q394AMj8__8J&astart=900',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=2xiHAAH9__8J&astart=910',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=OL0UABr9__8J&astart=920',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=wWLcADH9__8J&astart=930',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=enFyAUj9__8J&astart=940',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=LJNLAFz9__8J&astart=950',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=19ZvAHT9__8J&astart=960',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=C9GDAIT9__8J&astart=970',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=gsa3AJr9__8J&astart=980',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=hjwgAK_9__8J&astart=990',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=XaMAALz9__8J&astart=1000',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=SgkXAcr9__8J&astart=1010',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=qIEYAOP9__8J&astart=1020',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=1dprAPH9__8J&astart=1030',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17644907110646224264&after_author=KUT5AP39__8J&astart=1040',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nThe Hebrew University of Jerusalem done...\n")
    all_faculty_hebrew_uni_jerusalem = [list(item) for item in set(tuple(sublist) for sublist in all_faculty_hebrew_uni_jerusalem)]
    return all_faculty_hebrew_uni_jerusalem

if __name__ == "__main__":
    hebrew_uni_jerusalem()