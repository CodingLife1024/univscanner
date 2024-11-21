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

u_name = "University of Milan"
country = "Italy"

all_faculty_uni_milan = []

def get_faculty_data(link, headers):
    global all_faculty_uni_milan
    all_faculty_uni_milan += search_faculty_list(link, headers, u_name, country)[0]

def uni_milan():
    global all_faculty_uni_milan
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=NG8fAGDc_v8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=iSkLAPhm__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=BBHcAH99__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=SPT_AHmX__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=CdzfALOi__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=liAAALyt__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=6j4OACS0__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=a7y7AI67__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=AggGAH7C__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=SwAMAGfG__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=whAZAETK__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=UElPATHQ__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=UXzrAIDS__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=LjMSABvU__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=p0kpAKHW__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=lTBfAOXY__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=dWM1ATHb__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=nvpGAR7d__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=spkKABTf__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=BxwTABLh__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=9ZqTAIfi__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=Gq-UAELk__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=kp0AAbjl__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=D7AiAMTm__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=_HgJAMzn__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=X8EHAGzo__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=TZnOACjp__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=iNclAPHp__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=gHpXAC_r__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=L_cSAMLr__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=urQWAVns__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=g7UdAPbs__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=2gYJAJft__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=l5QUAW_u__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=bsK8AOfu__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=IAMMAIHv__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=9UsAAELw__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=5SCAAHzw__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=H8PgAAbx__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=qoIbAHXx__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=0pUEAN3x__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=VbKdAEzy__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=225eAHXy__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=M_SIAd3y__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=BLg4AFrz__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=nQ4LAMzz__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=nMXEADL0__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=Q5VTAIb0__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=nnmnAB71__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=lgoTAFz1__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=4ZDFAI31__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=3jODAMX1__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=UY5-AP71__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=o3gVAEr2__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=o1OXAI_2__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=xvwBAMX2__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=J-kdAAj3__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=PzsNACf3__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=4PcIAFX3__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=BiIXAbb3__8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=ex8XAOj3__8J&astart=610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=WSs2AB74__8J&astart=620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=hqGBADn4__8J&astart=630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=uM2VAHL4__8J&astart=640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=2MQUALb4__8J&astart=650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=dMytAAv5__8J&astart=660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=er7DAEz5__8J&astart=670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=pxeFAXL5__8J&astart=680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=VRWOAKf5__8J&astart=690',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=6GgjAN75__8J&astart=700',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=Hv45APT5__8J&astart=710',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=fyNzAA76__8J&astart=720',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=2otTADn6__8J&astart=730',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=SdmHAXX6__8J&astart=740',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=bHl5AKP6__8J&astart=750',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=S9CAAMz6__8J&astart=760',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=oNt0Ae36__8J&astart=770',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=jRxkABH7__8J&astart=780',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=62QmACn7__8J&astart=790',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=YJ9iAFf7__8J&astart=800',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=-RStAIr7__8J&astart=810',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=T14IAKv7__8J&astart=820',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=OiL2ALr7__8J&astart=830',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=Z2LpANr7__8J&astart=840',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=llQNAPv7__8J&astart=850',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=pz1CABz8__8J&astart=860',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=soYnATH8__8J&astart=870',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=YCQBAFb8__8J&astart=880',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=liq-AHv8__8J&astart=890',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=V5XgAJD8__8J&astart=900',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=ZcsLAKv8__8J&astart=910',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=Q31HALn8__8J&astart=920',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=n8wlANr8__8J&astart=930',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=qw14APT8__8J&astart=940',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=0aI5ARH9__8J&astart=950',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=gbx9ACP9__8J&astart=960',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=2_kGADv9__8J&astart=970',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=2zeRAEz9__8J&astart=980',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=VsVGAFv9__8J&astart=990',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=Hf3zAGz9__8J&astart=1000',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=xFkMAHr9__8J&astart=1010',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=hSh-AYP9__8J&astart=1020',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=LjgeAZf9__8J&astart=1030',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=OzX1AKX9__8J&astart=1040',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=rxPNALX9__8J&astart=1050',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=7x14ANn9__8J&astart=1060',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=Hf0fAOn9__8J&astart=1070',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14073688059094240927&after_author=17BbAAD-__8J&astart=1080',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Milan done...\n")
    all_faculty_uni_milan = [list(item) for item in set(tuple(sublist) for sublist in all_faculty_uni_milan)]
    return all_faculty_uni_milan

if __name__ == "__main__":
    uni_milan()