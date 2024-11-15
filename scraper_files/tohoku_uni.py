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

u_name = "Tohoku University"
country = "Japan"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def tohoku_uni():
    global all_faculty
    links = [
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562",
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=mWaTAJpn__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=7cqzAJeL__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=5IhDAO6j__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=ZwmLAPmv__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=PKEKAQe8__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=e7hiAd_E__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=MJQgAMDK__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=gfUpAA3P__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=Tw8WANnS__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=FB5EAHnV__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=4BhJAXnX__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=VMHOAdvZ__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=hU8AAHvc__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=GyiSAdbd__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=JOf8AB7g__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=DgvKAEnh__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=seeDAD_j__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=Adg6AAPl__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=4VLaALTl__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=nx3IAE7n__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=7LDoAIbo__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=EIkKAO3p__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=QTzCAK7q__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=p-AjAEzr__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=JonEAMXr__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=t-YQAHnt__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=ZS8NAdft__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=NdTFAYzu__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=qDhMAG_v__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=wmsEAbPv__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=WE18APXv__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=8scyAKzw__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=upSnAGrx__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=5mBdANLx__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=gfmWAILy__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=RxQuAPzy__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=4qYxAGfz__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=vrsdABP0__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=6S7HAaX0__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=qFR9ACb1__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=0l4UAJn1__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=6hIoAOv1__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=SYrZAGP2__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=67ONAcb2__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=JXNUADD3__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=uqqnAI73__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=CH-9AM33__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=Mn1lACf4__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=a-2JAWz4__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=l0dIAJv4__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=JhqUAbz4__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=eQ4tAfr4__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=5cFrADX5__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=qvRzAHr5__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=x12iAZv5__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=UHVKAMn5__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=05hFAfT5__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=ftMKARr6__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=iVIWAGj6__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=AeSFAJv6__8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=etdNAcz6__8J&astart=610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=mo2cAPn6__8J&astart=620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=ms_SABn7__8J&astart=630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=p_GgAEr7__8J&astart=640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=CXcUAHr7__8J&astart=650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=Z6vKAab7__8J&astart=660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=rV8KAcT7__8J&astart=670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=uHi-ANv7__8J&astart=680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=mWaTAJpn__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=7cqzAJeL__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=5IhDAO6j__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=ZwmLAPmv__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=PKEKAQe8__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=e7hiAd_E__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=MJQgAMDK__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=gfUpAA3P__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=Tw8WANnS__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=FB5EAHnV__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=4BhJAXnX__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=VMHOAdvZ__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=hU8AAHvc__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=GyiSAdbd__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=JOf8AB7g__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=DgvKAEnh__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=seeDAD_j__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=Adg6AAPl__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=4VLaALTl__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=nx3IAE7n__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=7LDoAIbo__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=EIkKAO3p__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=QTzCAK7q__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=p-AjAEzr__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=JonEAMXr__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=t-YQAHnt__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=ZS8NAdft__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=NdTFAYzu__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=qDhMAG_v__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=wmsEAbPv__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=WE18APXv__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=8scyAKzw__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=upSnAGrx__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=5mBdANLx__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=gfmWAILy__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=RxQuAPzy__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=4qYxAGfz__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=vrsdABP0__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=6S7HAaX0__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=qFR9ACb1__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=0l4UAJn1__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=6hIoAOv1__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=SYrZAGP2__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=67ONAcb2__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=JXNUADD3__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=uqqnAI73__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=CH-9AM33__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=Mn1lACf4__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=a-2JAWz4__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=l0dIAJv4__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=JhqUAbz4__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=eQ4tAfr4__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=5cFrADX5__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=qvRzAHr5__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=x12iAZv5__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=UHVKAMn5__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=05hFAfT5__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=ftMKARr6__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=iVIWAGj6__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=AeSFAJv6__8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=etdNAcz6__8J&astart=610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=mo2cAPn6__8J&astart=620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=ms_SABn7__8J&astart=630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=p_GgAEr7__8J&astart=640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=CXcUAHr7__8J&astart=650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=Z6vKAab7__8J&astart=660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=rV8KAcT7__8J&astart=670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17419755384042832562&after_author=uHi-ANv7__8J&astart=680',
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nTohoku University done...\n")
    all_faculty = [list(item) for item in set(tuple(sublist) for sublist in all_faculty)]
    return all_faculty

if __name__ == "__main__":
    tohoku_uni()