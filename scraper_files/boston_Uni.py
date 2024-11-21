
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

u_name = "Boston University"
country = "United States"

all_faculty_boston_uni = []

def get_faculty_data(link, headers):
    global all_faculty_boston_uni
    all_faculty_boston_uni += search_faculty_list(link, headers, u_name, country)[0]

def boston_uni():
    global all_faculty_boston_uni
    links = [
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119",
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=_p-hALyN_f8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=D_6TACzx_v8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=kPiEAEsm__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=7vssAOJG__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=9PUwALxf__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=NNK7AWhz__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=yPC_AMF9__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=I3i2AIOI__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=ujr3AFSR__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=RIYLAMib__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=yvkHAFuj__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=RmUBAEar__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=TgvyAEmw__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=4QMDABiz__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=LqkRAE-3__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=V9yOAWi6__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=KQYaAYO9__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=-C2BAEnB__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=k26VAMHD__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=354TAFnH__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=bYcIAK3I__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=Xr-TAIrK__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=9p8CAEfM__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=WKIFADTN__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=rfcMANvP__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=mX39AK7Q__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=cBZxAJ_S__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=tQ8VAAvU__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=490AAEzV__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=o9oUABDX__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=IU2QAHLY__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=rm0sABLa__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=rb4eAXrb__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=WMdmAGfc__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=EhYAAEHd__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=KzEJAFfe__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=m-c4ACvf__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=s6YFAOrf__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=AE0VABTh__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=zlAGAH7i__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=eWQkAJDj__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=Y1IFAN3j__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=D_QNAGnk__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=k40UAPDk__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=J-wAAIrl__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=kcBBACHm__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=0EyUAJzm__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=m7x8AGLn__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=PtwEABXo__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=6uJ5ALro__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=hc2sABjp__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=Rp8TAIPp__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=5hojAKjq__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=JexYAOHq__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=ptHzAFLr__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=-snsALzr__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18405750730531958119&after_author=52oDAEXs__8J&astart=570',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nBoston University done...\n")
    all_faculty_boston_uni = [list(item) for item in set(tuple(sublist) for sublist in all_faculty_boston_uni)]
    return all_faculty_boston_uni

if __name__ == "__main__":
    boston_uni()
