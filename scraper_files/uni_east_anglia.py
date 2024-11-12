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

u_name = "University of East Anglia (UEA)"
country = "United Kingdom"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def uni_east_anglia():
    global all_faculty
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=DbYcAERK__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=38UQAGmH__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=c7QAAE-u__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=U7cAAEDC__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=6q9KAMnM__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=WB2FALvR__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=LCuFACPZ__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=ykwyAcDb__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=gGnUABje__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=p4dgALzg__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=HEYPAILj__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=YOocAK3m__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=71X1AHHp__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=mb08AEXr__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=nNTIAI3s__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=Aw7vAJft__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=wLAlAOXu__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=cz2HAJXw__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=0suKAHDx__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=IK8NAObx__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=BSE_Adby__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=Af8EAOnz__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=Qho2AFX1__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=rSxNAPb1__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=4RQPAPj2__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=uAsuAaL3__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=hGg7AAP4__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=aLSnAWH4__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=IIAQAAD5__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=wek3AGr5__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=zhMsAPT5__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=tbPBAGH6__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=TEKKAPH6__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=k_0HAFT7__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=ikcCAL37__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=pekZABn8__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=NirrAEr8__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=hnUAALb8__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=c6QGAM_8__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=NjpBAf_8__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=thQVADf9__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=nuYwAYT9__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=cbxBAMP9__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=kZmXAOn9__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=pz-vABP-__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=rtJaADT-__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=JfUKAFj-__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=dmB8AGn-__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=PbqeAHn-__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=D2PMAJX-__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=LtcHALP-__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=YmF0AMz-__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=2Vo6AOD-__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=pCJ2APj-__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=I-OaAAv___8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=z_UaASD___8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=x_XNATP___8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=PHneAEf___8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=nsvVAF____8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=ZdiiAXP___8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=_WPYAH____8J&astart=610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=-N04AY____8J&astart=620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=3AxkAZj___8J&astart=630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=EpnZAKL___8J&astart=640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=rORqAar___8J&astart=650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=-dSEALH___8J&astart=660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=-wY4ALn___8J&astart=670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=EPf2AMH___8J&astart=680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=I2s9Acj___8J&astart=690',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=1OI9Ac____8J&astart=700',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=NnOnANX___8J&astart=710',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=DjstAd3___8J&astart=720',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=tXGHAeL___8J&astart=730',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=mXgJAef___8J&astart=740',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=Q2v9AOz___8J&astart=750',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=BhOGAe____8J&astart=760',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=7AMnAfL___8J&astart=770',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=oBf0APX___8J&astart=780',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=fPMSAfj___8J&astart=790',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=VpgwAPr___8J&astart=800',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=qsg_Afv___8J&astart=810',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9538045978089347208&after_author=WG-FAfz___8J&astart=820',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of East Anglia (UEA) done...\n")
    # print(len(all_faculty))
    return all_faculty

if __name__ == "__main__":
    uni_east_anglia()