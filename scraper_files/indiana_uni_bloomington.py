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

u_name = "Indiana University, Bloomington"
country = "United States"

all_faculty_indiana_uni_bloomington = []

def get_faculty_data(link, headers):
    global all_faculty_indiana_uni_bloomington
    all_faculty_indiana_uni_bloomington += search_faculty_list(link, headers, u_name, country)[0]

def indiana_uni_bloomington():
    global all_faculty_indiana_uni_bloomington
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=qF59AP3w_v8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=WU4AAJ45__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=2wQAAAFc__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=vlwTAA51__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=3AJhACOK__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=zVtLAcqW__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=DzAkAIif__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=o08-ASym__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=iqVAAHms__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=tihzAPiv__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=DAcGAIa2__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=VjMWAIW7__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=qkwBAG-8__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=O91PAL2___8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=718AAGHC__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=gl-8ADHF__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=Gm4HAILI__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=z0QmAG_K__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=cKgKAEzN__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=eXIYAQXP__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=y4EqAIfQ__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=4rYIAPLS__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=nMR2AVjV__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=aptbAJjX__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=vbUHAMLY__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=yfUQAWja__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=TTBtAMXb__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=vXwYAcHc__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=8uQDAMPd__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=BIs8AM_e__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=39MBAOrf__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=Hiw8Ad3g__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=9FoAAMvh__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=2zDAAVfi__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=zU-dAEfj__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=PORdAHrk__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=-CGGAIXl__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=xpgBACHm__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=3YkaALrm__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=qrABAFzn__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=FD83AP7n__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=pxIKAP7o__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=Ab4kAZnp__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=OvyBADjq__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=58tAAIjq__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=owwAABHr__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=Fix_AL_r__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=cdeTAbHs__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=ksNvAB_t__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=_1qdAI3t__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=A-M9AEju__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=EJpFAKHu__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=wE0AACLv__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=mNRbAKvv__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=GXwCABbw__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=xfunAEfw__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=5z0GAIfw__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=ZJsZAM7w__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=VdSLACPx__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=Zzx9AZ7x__8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=lAuHAPXx__8J&astart=610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=akCTADby__8J&astart=620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=luUUAY3y__8J&astart=630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=bKmXALzy__8J&astart=640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=6KoqAP3y__8J&astart=650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=yA3nAEvz__8J&astart=660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=NwlNAW_z__8J&astart=670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=XmscAKLz__8J&astart=680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=YxwBAOzz__8J&astart=690',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=5JWdAB_0__8J&astart=700',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=el6PAFL0__8J&astart=710',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=CNVVAIr0__8J&astart=720',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=PbAFANX0__8J&astart=730',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=3AfqAAn1__8J&astart=740',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=1kRbAFX1__8J&astart=750',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=zBsbAH31__8J&astart=760',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=1NpVAKf1__8J&astart=770',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=YH0BANf1__8J&astart=780',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=0kobAB32__8J&astart=790',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=QXw6AFT2__8J&astart=800',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=iNCFAIL2__8J&astart=810',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=neoWAMX2__8J&astart=820',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=jXUQAOn2__8J&astart=830',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=CGd8AAr3__8J&astart=840',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=Sc5cATL3__8J&astart=850',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=pgcmAEb3__8J&astart=860',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=IBsHAGX3__8J&astart=870',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=xGKGAJ33__8J&astart=880',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=A6MiAN73__8J&astart=890',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=2Ne9Af33__8J&astart=900',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=Y5YAABb4__8J&astart=910',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=3m_aADP4__8J&astart=920',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=sXtFAE_4__8J&astart=930',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=SSNOAH74__8J&astart=940',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=K9arALr4__8J&astart=950',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=cZQ2Adb4__8J&astart=960',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=l-6FAOv4__8J&astart=970',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=ergHASn5__8J&astart=980',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=TnLxAEb5__8J&astart=990',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=KL17AFD5__8J&astart=1000',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=bjO3AWP5__8J&astart=1010',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=FXRWAIH5__8J&astart=1020',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=mDmKAJn5__8J&astart=1030',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=znZCALb5__8J&astart=1040',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=K_u5Ab75__8J&astart=1050',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=BHQEAND5__8J&astart=1060',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=vMErAOr5__8J&astart=1070',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=Ll4AAAH6__8J&astart=1080',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=z9m7ARn6__8J&astart=1090',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=hmqwAUP6__8J&astart=1100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=ts0CAGP6__8J&astart=1110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=uhthAXb6__8J&astart=1120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=3AqHAI76__8J&astart=1130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=HvokAKv6__8J&astart=1140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=80YTALb6__8J&astart=1150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=RfuOAM76__8J&astart=1160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=1vcXAOP6__8J&astart=1170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=jEELAPv6__8J&astart=1180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=Bv56ABr7__8J&astart=1190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=AzsiADP7__8J&astart=1200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=fXQqAEf7__8J&astart=1210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=cHwHAFf7__8J&astart=1220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=56hWAG77__8J&astart=1230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=zIy2AIP7__8J&astart=1240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=8DqPAJD7__8J&astart=1250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=30cNAZ37__8J&astart=1260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=DkeMAbT7__8J&astart=1270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=qd16Acv7__8J&astart=1280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=VKe-AN_7__8J&astart=1290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=noPOAPD7__8J&astart=1300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=SQnfAPr7__8J&astart=1310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=Yj4DAAj8__8J&astart=1320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=ax8MAST8__8J&astart=1330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=kri0ADH8__8J&astart=1340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=p3Y3AT_8__8J&astart=1350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=WqiiAVL8__8J&astart=1360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=viSgAGf8__8J&astart=1370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=XC4HAHb8__8J&astart=1380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=Zb_kAID8__8J&astart=1390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=f6UuAJL8__8J&astart=1400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=tuiEAKP8__8J&astart=1410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=SSEWAK78__8J&astart=1420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=mf1SALf8__8J&astart=1430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=unSeAb_8__8J&astart=1440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=yf9SAMz8__8J&astart=1450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=dtJtANj8__8J&astart=1460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=M2mgAOD8__8J&astart=1470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=p4uNAO38__8J&astart=1480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=gOfOAPz8__8J&astart=1490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=pBxyAQH9__8J&astart=1500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=bUr5AA_9__8J&astart=1510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=RocBAB_9__8J&astart=1520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=pRwRACb9__8J&astart=1530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=Uzj7ADL9__8J&astart=1540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=wPcBAT79__8J&astart=1550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=hMAUAEn9__8J&astart=1560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=dibwAFP9__8J&astart=1570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=ylT3AGD9__8J&astart=1580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=Vp-GAGn9__8J&astart=1590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=7ZKtAXD9__8J&astart=1600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=JGkQAXf9__8J&astart=1610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=ccIpAYL9__8J&astart=1620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=GzeJAI79__8J&astart=1630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=ZdqxAJP9__8J&astart=1640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=isRpAZz9__8J&astart=1650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=pRGoAaD9__8J&astart=1660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=c2RFAK79__8J&astart=1670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=oqY5ALb9__8J&astart=1680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=50MRAb79__8J&astart=1690',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=-IICAMf9__8J&astart=1700',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=TKT3ANL9__8J&astart=1710',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=wMdQAdf9__8J&astart=1720',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=jNv_AOD9__8J&astart=1730',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=UTddAev9__8J&astart=1740',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=Gb2QAPf9__8J&astart=1750',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=5a2wAP79__8J&astart=1760',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=FqcCAAX-__8J&astart=1770',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18243465982490009522&after_author=KUhYAQn-__8J&astart=1780',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nIndiana University, Bloomington done...\n")
    all_faculty_indiana_uni_bloomington = [list(item) for item in set(tuple(sublist) for sublist in all_faculty_indiana_uni_bloomington)]
    return all_faculty_indiana_uni_bloomington

if __name__ == "__main__":
    indiana_uni_bloomington()