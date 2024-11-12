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

u_name = "George Washington University"
country = "United States"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def george_washington_uni():
    global all_faculty
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=lvcSACAy__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=xAoTAFCV__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=ulIAAP-v__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=VdEGAC_B__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=bDOEAQPH__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=xk4BAO7M__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=KwwHAfrS__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=ylg2AFjX__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=JCITAHTa__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=fE58AEjc__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=zr0hACXe__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=8pmdAHHf__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=1ZoDANLi__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=S_bBAFDl__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=R-IeADHm__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=lJN4ABHo__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=Jwp_AITp__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=NpVXAAXr__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=AqkCACDs__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=P4g_AAzt__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=4OWOAPjt__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=L8IKAN3u__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=Kr4IAF7v__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=qI1PAEvw__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=H8oAAPzw__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=9I-pAF7x__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=tQhqAPjx__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=BraGAHby__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=MUeFAPny__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=sMILAGXz__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=0ousAPHz__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=-4gAAHL0__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=KecOAAP1__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=-eMWAFP1__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=npgYAdb1__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=M0N8ADb2__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=ha9fAKz2__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=tvp_AAj3__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=JZPjAFz3__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=sjhHAcf3__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=n1hEAQj4__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=qTUwADj4__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=_hx-AY34__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=p6XGAAP5__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=WysNAET5__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=zbmJAG35__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=tNLzAMz5__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=LJJZAD_6__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=CibXAIH6__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=ygBMAKr6__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=KT-QANn6__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=cRYGAAb7__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=_KmmAD37__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=hOwZAWr7__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=sj4XAJ77__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=mCIuAN37__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=Os1sAPv7__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=Ml1MAR38__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=w22cAEb8__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=i09hAGT8__8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=FcUPAXr8__8J&astart=610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=Jq2JAKT8__8J&astart=620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=np2kAL78__8J&astart=630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=fcDFAd78__8J&astart=640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=2s7bAPr8__8J&astart=650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=7fXaABD9__8J&astart=660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=9hxeAC79__8J&astart=670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=gCiUAE79__8J&astart=680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=jgG0AGL9__8J&astart=690',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=SS10AH39__8J&astart=700',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=87BKAJX9__8J&astart=710',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=JfM_AKv9__8J&astart=720',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=iZB6ALr9__8J&astart=730',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=JPOuANT9__8J&astart=740',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=Cq6zAPL9__8J&astart=750',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=nO4WAP79__8J&astart=760',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=mXKXARH-__8J&astart=770',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=Ja-EASL-__8J&astart=780',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=WEcDADP-__8J&astart=790',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=HOw9AT3-__8J&astart=800',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=wtKMAFb-__8J&astart=810',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=g3V3AXP-__8J&astart=820',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=4OJqAIH-__8J&astart=830',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=fnUQAJL-__8J&astart=840',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=RdW5AKD-__8J&astart=850',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=XZmLAKz-__8J&astart=860',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=moAKAbn-__8J&astart=870',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=o8wIAMf-__8J&astart=880',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=uMHwAND-__8J&astart=890',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=9tWcANj-__8J&astart=900',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=IYylAOH-__8J&astart=910',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=UWu7AO3-__8J&astart=920',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=8sXLAPz-__8J&astart=930',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=zTOBAAr___8J&astart=940',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=O7q-AQ____8J&astart=950',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=D97ZAB3___8J&astart=960',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=jjHeACP___8J&astart=970',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=oEkHAC____8J&astart=980',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=rlkzATb___8J&astart=990',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=hMKvAUD___8J&astart=1000',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=-rWnAEn___8J&astart=1010',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=hHaVAVD___8J&astart=1020',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=DbL9AFf___8J&astart=1030',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=8DJDAGD___8J&astart=1040',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=2TqfAWb___8J&astart=1050',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=eWJMAW____8J&astart=1060',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=zmZQAXX___8J&astart=1070',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=lxdRAHv___8J&astart=1080',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=AMOIAYL___8J&astart=1090',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=UYSWAIb___8J&astart=1100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=crWmAYj___8J&astart=1110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=URIkAYz___8J&astart=1120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=CpVqAJH___8J&astart=1130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=W0B9AZX___8J&astart=1140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=6PCsAJr___8J&astart=1150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=91X9AKD___8J&astart=1160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=77-uAKX___8J&astart=1170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=tuwkAaj___8J&astart=1180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=SVArAKv___8J&astart=1190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=ZwtzALD___8J&astart=1200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=2NC0AbH___8J&astart=1210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=lCpkAbb___8J&astart=1220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=QJ7kALr___8J&astart=1230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=R8ovAb____8J&astart=1240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=k4fNAML___8J&astart=1250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=EOK4AMb___8J&astart=1260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=WeFwAcr___8J&astart=1270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=5O3IAcz___8J&astart=1280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=WfuZAc7___8J&astart=1290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=0-g5AND___8J&astart=1300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=m2u7ANL___8J&astart=1310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=NVreANT___8J&astart=1320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=zbFxAdb___8J&astart=1330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=5JqlAdn___8J&astart=1340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=IOz_ANv___8J&astart=1350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=nl-DAdz___8J&astart=1360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=g8euAd____8J&astart=1370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=wBOyAeH___8J&astart=1380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=r7o1AeP___8J&astart=1390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=sSitAeT___8J&astart=1400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=slMyAeb___8J&astart=1410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=fCdFAef___8J&astart=1420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=PueHAej___8J&astart=1430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=EvIKAer___8J&astart=1440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=725UAev___8J&astart=1450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=lfYSAez___8J&astart=1460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=N_rNAO3___8J&astart=1470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=6wSaAO7___8J&astart=1480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=0eX3AO____8J&astart=1490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=4Kz6APD___8J&astart=1500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=7iNBAPH___8J&astart=1510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=qO8tAPL___8J&astart=1520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=Q2BMAfP___8J&astart=1530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=v3UBAfT___8J&astart=1540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=sRrBAfT___8J&astart=1550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=9jJyAfX___8J&astart=1560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=ttZ5Afb___8J&astart=1570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=F5alAff___8J&astart=1580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=802WAfj___8J&astart=1590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=Mtl1Afn___8J&astart=1600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=KLH-APr___8J&astart=1610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=eJK6Afr___8J&astart=1620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=hxlNAfv___8J&astart=1630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=c2ymAfv___8J&astart=1640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=jCAhAfz___8J&astart=1650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=3yCaAfz___8J&astart=1660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4691692344163214902&after_author=EXa3Afz___8J&astart=1670',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nGeorge Washington University done...\n")
    # print(len(all_faculty))
    return all_faculty

if __name__ == "__main__":
    george_washington_uni()