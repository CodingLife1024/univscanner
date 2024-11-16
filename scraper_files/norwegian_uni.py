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

u_name = "Norwegian University of Science and Technology"
country = "South Korea"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def norwegian_uni():
    global all_faculty
    links = [
        'https://scholar.google.com/citations?view_op=view_org&org=14548340185041024401',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=Ty7SACl-__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=-auTAPyg__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=we4IAGK1__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=G4CPAD3B__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=5-0VADzH__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=N3o5ANzK__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=wo0HAELQ__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=cWHwAMLV__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=1cgcANnZ__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=wh9oANDa__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=aRshABDe__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=9GkaAB7g__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=dnpzAKvi__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=Wg-xAWvk__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=kmFaAALm__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=EMgTAFzn__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=OgdHACjo__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=1Ck5AbHo__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=HASTALfp__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=RDOEAM3q__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=fh4PALnr__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=UE13AEHs__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=arIfABft__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=lk4NAITt__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=poQIAEnu__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=Do3MAM7u__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=-DEtAHTv__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=eusBAG3w__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=QaB2AAnx__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=CAIuAHTx__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=b0QFAOTx__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=Ia7FAE_y__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=cEHdAKDy__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=_OYQAAjz__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=lTq_AEvz__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=O-sDAKfz__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=1EcFANfz__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=7JeEADj0__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=BYYhAbT0__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=PPAcAAn1__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=TUwWAHD1__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=qmQbAK_1__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=6XYaAfL1__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=sHfnAC72__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=SHAMAJT2__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=tQQVAbT2__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=k-UZAOn2__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=MtCQAAz3__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=ARNFAUH3__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=VswgAJL3__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=GrMAANH3__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=Ov4RABP4__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=cEkAADr4__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=prH3AFD4__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=HJChAIb4__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=Vi9CAab4__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=OS-TAOX4__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=oYQOAC35__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=rbDeAGL5__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=vgclAYr5__8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=S3s3AKv5__8J&astart=610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=WHe5APD5__8J&astart=620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=XkoTACP6__8J&astart=630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=fsrDAVz6__8J&astart=640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=YzNmAIb6__8J&astart=650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=8nxCALH6__8J&astart=660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=RbzjAND6__8J&astart=670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=nokkAAf7__8J&astart=680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=gskhADf7__8J&astart=690',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=TMXMAE77__8J&astart=700',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=QgIvAXP7__8J&astart=710',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=P8weAJP7__8J&astart=720',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=IEYAAbn7__8J&astart=730',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=E4yGANL7__8J&astart=740',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=A5WOAPX7__8J&astart=750',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=1VkvAAf8__8J&astart=760',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=FLMCACL8__8J&astart=770',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=2CELADf8__8J&astart=780',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=N9QXAE78__8J&astart=790',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=FGuxAGb8__8J&astart=800',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=XpkUAHn8__8J&astart=810',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=p31CAI78__8J&astart=820',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=uZcQAKX8__8J&astart=830',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=w9m3ALj8__8J&astart=840',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=MOEyANT8__8J&astart=850',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=QOpfAN38__8J&astart=860',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=43iGAPn8__8J&astart=870',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=6ACHAAr9__8J&astart=880',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=k6RQABf9__8J&astart=890',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=FskwASH9__8J&astart=900',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=M4QZATv9__8J&astart=910',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=Jh_vAFL9__8J&astart=920',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=Vwx_AFn9__8J&astart=930',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=DihgAWT9__8J&astart=940',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=qYP7AHf9__8J&astart=950',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=ch8XAYr9__8J&astart=960',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=0cmjAJL9__8J&astart=970',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=IkfUAJ79__8J&astart=980',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=TMbRAKv9__8J&astart=990',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=N_gWAL39__8J&astart=1000',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=bDUEAcf9__8J&astart=1010',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=YcqKAdH9__8J&astart=1020',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=wNWxAdz9__8J&astart=1030',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=DHeZAOP9__8J&astart=1040',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=akjmAPP9__8J&astart=1050',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=I4w0AP_9__8J&astart=1060',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14548340185041024401&after_author=qK-xAAb-__8J&astart=1070',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nNorwegian University of Science and Technology done...\n")
    all_faculty = [list(item) for item in set(tuple(sublist) for sublist in all_faculty)]
    return all_faculty

if __name__ == "__main__":
    norwegian_uni()