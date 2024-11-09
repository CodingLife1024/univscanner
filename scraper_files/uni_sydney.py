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

u_name = "University of Sydney"
country = "United States"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def uni_sydney():
    global all_faculty
    links = [
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969",
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=FQwEAClJ_v8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=-5VQAJrP_v8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=L7UGAHEP__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=-J0xAbsw__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=Z9IKAA1c__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=_J8DAOps__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=ym2EALl6__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=B88AAKeC__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=kmF6ACyM__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=BP0mAL-U__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=EpLwACOZ__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=e5aoAIya__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=LF0dAN6e__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=nEtYAfGk__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=8FMAADer__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=VNY-ASqv__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=ArZqABCx__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=QZcAAFmz__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=KaIEAPW1__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=zvHVAHu4__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=X81JAMK7__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=UpphAHq-__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=rUOCAMvA__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=o3IDAL_C__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=b4P0APzD__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=Eh6HALrF__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=IB8OAPPH__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=ITp1AffI__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=v4kDAELL__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=avF8AE_M__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=r5AgAL7N__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=-Fo6AHTO__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=3k8gAEvQ__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=9gZPAa7R__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=-YwBANjS__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=-5uQAPLT__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=9iwGAC3V__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=36F9AHLW__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=HtIyAFfX__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=JC0CAEzY__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=DOZtAPvY__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=sQLCAe7Z__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=mJoGAPDa__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=gJN0AJjb__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=2vEAAFzc__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=tWFlAC3d__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=tzhjANvd__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=lTwLAOLe__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=IDWCAM_f__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=onumAYHg__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=cdaaADDh__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=VOhUANbh__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=wMwDAG7i__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=hfKtAB7j__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=cC0BAPXj__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=QZ4AAAbl__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=0cYAAGLl__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=UsenAN_l__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=jCTQATHm__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=EMeDAKfm__8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=zRE4ASLn__8J&astart=610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=KnIFAKvn__8J&astart=620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=BwXnACzo__8J&astart=630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=LogJAITo__8J&astart=640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=M3oEAfvo__8J&astart=650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=h-M_AE3p__8J&astart=660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=5YRcAaLp__8J&astart=670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=_Q0HAB3q__8J&astart=680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=1FbGAGTq__8J&astart=690',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=FrqYAAPr__8J&astart=700',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=88QlAGrr__8J&astart=710',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=Zxo8AOXr__8J&astart=720',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=24qsABPs__8J&astart=730',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17869855370174230969&after_author=xCQAAGns__8J&astart=740',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Sydney done...\n")
    # print(len(all_faculty))
    return all_faculty

if __name__ == "__main__":
    uni_sydney()