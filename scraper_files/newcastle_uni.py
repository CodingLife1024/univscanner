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

u_name = "Newcastle University"
country = "United Kingdom"

all_faculty_newcastle_uni = []

def get_faculty_data(link, headers):
    global all_faculty_newcastle_uni
    all_faculty_newcastle_uni += search_faculty_list(link, headers, u_name, country)[0]

def newcastle_uni():
    global all_faculty_newcastle_uni
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=cCPmAGg0__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=3IxxAaFl__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=13IUAMl9__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=c5EhAD2M__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=27gSALCY__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=koUwAQSh__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=W2oDAHSo__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=z2IGALqv__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=EuIAAG64__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=fcznAMO6__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=0HVDACzC__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=Q5QuAefI__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=OwYLAEXK__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=5xskAL7O__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=7tQAADzR__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=_msUADnT__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=7XcmAGrV__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=rVuHAPXW__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=5D5nAHDY__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=dqR-AGba__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=RyYOALTb__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=A3w0ACPd__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=MNXUAATe__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=KEANAKPf__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=qsKMAPTg__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=Ym16AMjh__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=YCZJAezi__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=OG5YABTk__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=-Ct5AMjk__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=RLazAM7m__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=VyuSABPo__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=XVazAI7o__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=R8GaAF3p__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=aYFXAcDp__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=ddmwADTq__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=XtUdAP3q__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=cR0VAM7r__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=lzLfAHvs__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=xRxJAELt__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=URc-AHjt__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=xRATAYDu__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=-ZqNAHTv__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=ZmkKAdrv__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=SEoQABPw__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=J1WRAKXw__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=6bcRABXx__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=McazAGLx__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=LPSlALHx__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=PeXnAALy__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=YAg3AE7y__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=HfsDAJfy__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=2L0tAALz__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=86JEAUrz__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=xDxNAI7z__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=ZkSUANfz__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=Xr5HAC_0__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=udqiAE_0__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=boFfAIf0__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=MhmoAN30__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=joQBAEn1__8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=Vi0tAIb1__8J&astart=610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=v3fkAKv1__8J&astart=620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=bvFWAN_1__8J&astart=630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=Hrh6ACv2__8J&astart=640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=MV-QAGv2__8J&astart=650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=6X4BALH2__8J&astart=660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=UwyTAO_2__8J&astart=670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=_WvDACH3__8J&astart=680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=I9p9AFL3__8J&astart=690',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=gFqDAIX3__8J&astart=700',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=Vs9VALf3__8J&astart=710',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=IuOoAOj3__8J&astart=720',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=iJulAA74__8J&astart=730',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=CqU7AUL4__8J&astart=740',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=RMu_AHX4__8J&astart=750',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=QzsAAI_4__8J&astart=760',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=m_6PANX4__8J&astart=770',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=EUg1AAf5__8J&astart=780',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=WPSGAD_5__8J&astart=790',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=WuwQAFv5__8J&astart=800',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=l4PlAH75__8J&astart=810',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=Fx7JAJ35__8J&astart=820',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=h00vAb75__8J&astart=830',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=bHitAOT5__8J&astart=840',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=e6pUARj6__8J&astart=850',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=y0IIADn6__8J&astart=860',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=nDMBAFz6__8J&astart=870',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=tLbFAIH6__8J&astart=880',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=fKyuAJj6__8J&astart=890',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=JgZ1Aan6__8J&astart=900',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=QfZwAcv6__8J&astart=910',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=QfZHAOX6__8J&astart=920',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=UKZRAPH6__8J&astart=930',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=sHaKAAT7__8J&astart=940',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=wHGxACT7__8J&astart=950',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=U4wkAD37__8J&astart=960',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=k-EWAFP7__8J&astart=970',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=RYbxAGP7__8J&astart=980',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=EicsAIX7__8J&astart=990',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=tv8FAKL7__8J&astart=1000',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=EDGEALv7__8J&astart=1010',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=TYa2ANX7__8J&astart=1020',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=3-oiAOv7__8J&astart=1030',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=raeEAAb8__8J&astart=1040',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=Xjz1ABv8__8J&astart=1050',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=ngjJAC_8__8J&astart=1060',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=UVHqADr8__8J&astart=1070',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=TXkhAEb8__8J&astart=1080',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=RFwMAGb8__8J&astart=1090',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=yDOuAHb8__8J&astart=1100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=Dd09AJL8__8J&astart=1110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=415WAK78__8J&astart=1120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=b9MkAb38__8J&astart=1130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=HO5KANz8__8J&astart=1140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=_5KpAO_8__8J&astart=1150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=Cd8UAAL9__8J&astart=1160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=Ea-RABz9__8J&astart=1170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=QKQFAC_9__8J&astart=1180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=buqEAED9__8J&astart=1190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=0Kw8AU79__8J&astart=1200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=tQqGAFj9__8J&astart=1210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=_qlkAGb9__8J&astart=1220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=fuI4AXL9__8J&astart=1230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=Y3kBAIL9__8J&astart=1240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=jaeyAJD9__8J&astart=1250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=7a4SAJn9__8J&astart=1260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=3VjuAKX9__8J&astart=1270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=pRFqAa_9__8J&astart=1280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=d-ECAbX9__8J&astart=1290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=HAvsAL_9__8J&astart=1300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=pP1tAM39__8J&astart=1310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=7K4IAdf9__8J&astart=1320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=1Ey9AOv9__8J&astart=1330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=1R2zAPz9__8J&astart=1340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7687019144636890226&after_author=4TiSAQT-__8J&astart=1350',
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nNewcastle University done...\n")
    all_faculty_newcastle_uni = [list(item) for item in set(tuple(sublist) for sublist in all_faculty_newcastle_uni)]
    return all_faculty_newcastle_uni

if __name__ == "__main__":
    newcastle_uni()