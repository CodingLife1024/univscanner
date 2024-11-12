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

u_name = "Friedrich Alexander Universität Erlangen Nürnberg"
country = "Germany"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def uni_erlangen_nuremberg():
    global all_faculty
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=xKkYAKpQ__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=7TqIAISh__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=2HmnAemt__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=nTIYAB26__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=yewfABW___8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=ePeDAFXJ__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=shcjABzO__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=OiokAF3T__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=8pMiAM7Y__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=_mAFAHPd__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=5a0iAF3g__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=ydACAPnh__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=_KbGANXj__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=8AdeAX_l__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=bHhEAFXo__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=6ipBANHp__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=26YRAQrs__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=YAT5AAfu__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=oxuMAFrv__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=nd4OAG3w__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=_qOYAdLx__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=aXqDALjy__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=1LMFAJTz__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=MoMUAE30__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=t_OTAOf0__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=A5QeAKj1__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=fW8EAJL2__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=9lmEACX3__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=oq4CAL_3__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=rQ0RARb4__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=nwzWAFr4__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=YkKWAM34__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=gyPeAET5__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=UBLQAKn5__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=LMuHACP6__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=aJSXAFz6__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=Se7HAfj6__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=mGBjADn7__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=_1ZVAWT7__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=iNmBAJT7__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=SnopALz7__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=FNEEAAH8__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=_1o8AC78__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=jPlSAFr8__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=WTtMAHj8__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=tJGlAaP8__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=ec-KAMb8__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=i2edAO_8__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=1qryAAn9__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=GkSxACX9__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=sRZwAE_9__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=pCpVAHX9__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=QLitAY79__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=RITHAJ_9__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=UXqWAK39__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=tKEOAMH9__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=-05AANn9__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=DFc_APD9__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3435058929645828923&after_author=8YC9Afr9__8J&astart=590',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nFriedrich Alexander Universität Erlangen Nürnberg done...\n")
    # print(len(all_faculty))
    return all_faculty

if __name__ == "__main__":
    uni_erlangen_nuremberg()