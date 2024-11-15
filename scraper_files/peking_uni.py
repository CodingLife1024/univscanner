import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures
import pprint

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.GLOBAL_VARIABLES import *
from components.gscholar_indiv_page import search_faculty_list

u_name = "Peking University"
country = "China"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def peking_uni():
    global all_faculty
    links = [
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184",
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=S-wgAPQ0__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=oqACANps__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=anRiAL59__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=kK8BAHaS__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=aY4TAP6i__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=k5UFANew__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=Uu0sAL64__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=6V5aANm7__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=K8RUAa3D__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=s__UANLF__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=yHAMAOjH__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=qSDaAJvJ__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=DDEBALHL__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=P40QAGzN__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=GCwAAF_Q__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=jIJlAJLU__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=9pIBAKTW__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=drs2AHfZ__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=6dQCAIXa__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=gydAAGvb__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=UqFqAPzc__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=fNIBAPfe__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=PH0gAK_f__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=gyFZANTg__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=CtS3AMPh__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=OTuKAJfi__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=Ki-vAbzj__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=51wSAGTk__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=wC05AOTl__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=xswcAEfm__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=Wp8BAc7m__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=jRswAHDn__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=e6EUADTo__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=oDpDAAfp__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=7FZjAI7p__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=F8YxAZPq__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=IA_0ANjq__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=Q8ToAEHr__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=XhKJABDs__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10725744176602846184&after_author=AoxlAF3s__8J&astart=400',
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nPeking University done...\n")
    # print(len(all_faculty))
    all_faculty = [list(item) for item in set(tuple(sublist) for sublist in all_faculty)]
    return all_faculty

if __name__ == "__main__":
    peking_uni()