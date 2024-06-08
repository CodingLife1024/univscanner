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
import csv

def main():
    with open('faculty_data.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["University", "Country", "Name", "Email", "URL", "Personal Webpage"])

        # writer.writerows(mit())
        # writer.writerows(stanford())
        # writer.writerows(harvard())
        # writer.writerows(caltech())
        # writer.writerows(oxford())
        # writer.writerows(cambridge())
        # writer.writerows(imperial())
        # writer.writerows(uchicago())
        # writer.writerows(ucl_london())
        # writer.writerows(nus())
        # writer.writerows(princeton())
        # writer.writerows(ntus())
        # writer.writerows(tsinghua())
        # writer.writerows(upenn())
        # writer.writerows(yale())
        # writer.writerows(cornell())
        # writer.writerows(columbia())
        writer.writerows(edinburgh())

if __name__ == "__main__":
    main()
