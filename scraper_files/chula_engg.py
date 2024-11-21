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

u_name = "Chulalongkorn University"
country = "Thailand"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def chula_engg():
    global all_faculty
    links = [
        "https://scholar.google.com/citations?view_op=view_org&org=10884788013512991188",
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=WP4KAODP__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=7awDABDg__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=f0XFAOHj__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=o5wOAGbo__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=v3SEAGfr__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=v2FnAOrt__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=HTJiAJvw__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=dLysAMPx__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=5UwAABzz__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=e9oXAEz0__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=z6UNAez0__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=B_59AJv1__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=DJ3zADr2__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=JiJlAND2__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=6sFWAGf3__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=0gD0ANz3__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=uHTzAEr4__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=njDcAHX4__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=B_i2AMf4__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=xMBaAA35__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=8Z81AF35__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=yHFTAJP5__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=N0J7AOP5__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=61fPADf6__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=GpjzAFP6__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=9AkhAJv6__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=M8y_ANP6__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=OlqXAP_6__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=WIBgADH7__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=a7jPAHL7__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=Z0xAALb7__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=_ngwAMv7__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=0RiEAOT7__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=j1z0AAH8__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=1_imAB_8__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=X0_0ADn8__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=o1X8AFD8__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=IGL0AGb8__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=E0HzAHj8__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=lFv_AIf8__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=mGTAAJ_8__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=BTH0AMD8__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=JJ42AOb8__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=5eL1APb8__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=-BdCAAv9__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=Lvp5ACb9__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=cHo8ATf9__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=KxcbAVP9__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=yU4TAGj9__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=T_HAAIP9__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=TgFzAZ79__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=Cvf1AK_9__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=GP_AAbb9__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=Ut62AMz9__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=eHTzANH9__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=kHz7AOD9__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=BE1dAfD9__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=asWEAfj9__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10884788013512991188&after_author=mjb7AAf-__8J&astart=590',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nChulalongkorn University done...\n")
    all_faculty = [list(item) for item in set(tuple(sublist) for sublist in all_faculty)]
    return all_faculty

if __name__ == "__main__":
    chula_engg()