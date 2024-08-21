import csv

from scraper_files.mit import mit
from scraper_files.stanford import stanford
from scraper_files.harvard import harvard
from scraper_files.caltech import caltech
from scraper_files.oxford import oxford
from scraper_files.cambridge import cambridge
from scraper_files.imperial import imperial
from scraper_files.uchicago import uchicago
from scraper_files.ucl_london import ucl_london
from scraper_files.nus import nus
from scraper_files.princeton import princeton
from scraper_files.ntus import ntus
from scraper_files.tsinghua import tsinghua
from scraper_files.upenn import upenn
from scraper_files.yale import yale
from scraper_files.cornell import cornell
from scraper_files.columbia import columbia
from scraper_files.edinburgh import edinburgh
from scraper_files.hongkong import hongkong
from scraper_files.tokyo import tokyo
from scraper_files.john_hopkins import john_hopkins
from scraper_files.toronto import toronto
from scraper_files.manchester import manchester
from scraper_files.northwestern import northwestern
from scraper_files.uc_berkeley import uc_berkeley
from scraper_files.anu import anu
from scraper_files.kings_college import kings_college
from scraper_files.mcgill import mcgill
from scraper_files.nyu import nyu
from scraper_files.seoul_uni import seoul_uni
from scraper_files.kaist import kaist
from scraper_files.duke import duke
from scraper_files.ubc_canada import ubc_canada
from scraper_files.uni_queensland import uni_queensland
from scraper_files.shanghai_jt import shanghai_jt
from scraper_files.city_uni_hk import city_uni_hk
from scraper_files.carnegie_mellon import carnegie_mellon
from scraper_files.zhejiang_uni import zhejiang_uni
from scraper_files.ucsd import ucsd
from scraper_files.tokyo_uni_tech import tokyo_uni_tech
from scraper_files.delft_uni_tech import delft_uni_tech
from scraper_files.brown_uni import brown_uni
from scraper_files.uni_warwick import uni_warwick
from scraper_files.uni_wisconsin import uni_wisconsin
from scraper_files.national_taiwan_university import national_taiwan_university
from scraper_files.korea_uni import korea_uni
from scraper_files.uni_austin import uni_austin
from scraper_files.osaka_uni import osaka_uni
from scraper_files.uni_washington import uni_washington
from scraper_files.hong_kong_poly_uni import hong_kong_poly_uni
from scraper_files.uni_copenhagen import uni_copenhagen
from scraper_files.postech_korea import postech_korea


def main():
    with open('faculty_data.csv', 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["University", "Country", "Name", "Email", "URL", "Personal Webpage"])

        writer.writerows(mit())
        writer.writerows(stanford())
        writer.writerows(harvard())
        writer.writerows(caltech())
        writer.writerows(oxford())
        writer.writerows(cambridge())
        writer.writerows(imperial())
        writer.writerows(uchicago())
        writer.writerows(ucl_london())
        writer.writerows(nus())
        writer.writerows(princeton())
        writer.writerows(ntus())
        writer.writerows(tsinghua())
        writer.writerows(upenn())
        writer.writerows(yale())
        writer.writerows(cornell())
        writer.writerows(columbia())
        writer.writerows(edinburgh())

        writer.writerows(hongkong())

        writer.writerows(tokyo())
        writer.writerows(john_hopkins())
        writer.writerows(toronto())
        writer.writerows(manchester())
        writer.writerows(northwestern())
        writer.writerows(uc_berkeley())
        writer.writerows(anu())
        writer.writerows(kings_college())
        writer.writerows(mcgill())

        writer.writerows(nyu())

        writer.writerows(seoul_uni())
        writer.writerows(kaist())


        writer.writerows(duke())


        writer.writerows(ubc_canada())
        writer.writerows(uni_queensland())
        writer.writerows(shanghai_jt())
        writer.writerows(city_uni_hk())
        writer.writerows(carnegie_mellon())

        writer.writerows(zhejiang_uni())
        writer.writerows(ucsd())

        writer.writerows(tokyo_uni_tech())
        writer.writerows(delft_uni_tech())
        writer.writerows(brown_uni())
        writer.writerows(uni_warwick())
        writer.writerows(uni_wisconsin())
        writer.writerows(national_taiwan_university())
        writer.writerows(korea_uni())
        writer.writerows(uni_austin())
        writer.writerows(osaka_uni())
        writer.writerows(uni_washington())
        writer.writerows(hong_kong_poly_uni())
        writer.writerows(uni_copenhagen())
        writer.writerows(postech_korea())

if __name__ == "__main__":
    main()
