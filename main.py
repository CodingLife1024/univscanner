import csv

from redo.mit import mit
from redo.stanford import stanford
from redo.harvard import harvard
from redo.caltech import caltech
from redo.oxford import oxford
from redo.cambridge import cambridge
from redo.imperial import imperial
from redo.uchicago import uchicago
from redo.ucl_london import ucl_london
from redo.nus import nus
from redo.princeton import princeton
from redo.ntus import ntus
from redo.tsinghua import tsinghua
from redo.upenn import upenn
from redo.yale import yale
from redo.cornell import cornell
from redo.columbia import columbia
from redo.edinburgh import edinburgh

def main():
    with open('faculty_data.csv', 'w', encoding='utf-8', newline='') as file:
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

        # writer.writerows(hongkong())

        # writer.writerows(tokyo())
        # writer.writerows(john_hopkins())
        # writer.writerows(toronto())
        # writer.writerows(manchester())
        # writer.writerows(northwestern())
        # writer.writerows(uc_berkeley())
        # writer.writerows(anu())
        # writer.writerows(kings_college())
        # writer.writerows(mcgill())

        # writer.writerows(nyu())

        # writer.writerows(seoul_uni())
        # writer.writerows(kaist())


        # writer.writerows(duke())


        # writer.writerows(ubc_canada())
        # writer.writerows(uni_queensland())
        # writer.writerows(shanghai_jt())
        # writer.writerows(city_uni_hk())
        # writer.writerows(carnegie_mellon())

        # writer.writerows(zhejiang_uni())
        # writer.writerows(uscd())

        # writer.writerows(tokyo_uni_tech())
        # writer.writerows(delft_uni_tech())
        # writer.writerows(brown_uni())
        # writer.writerows(uni_warwick())
        # writer.writerows(uni_wisconsin())

if __name__ == "__main__":
    main()
