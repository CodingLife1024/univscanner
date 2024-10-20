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
from scraper_files.uni_glasgow import uni_glasgow

from scraper_files.georgia_inst_tech import georgia_inst_tech

from scraper_files.uni_illinois import uni_illinois

from scraper_files.durham_uni import durham_uni
from scraper_files.yonsei_uni import yonsei_uni
from scraper_files.uni_birmingham import uni_birmingham

from scraper_files.uni_southampton import uni_southampton
from scraper_files.uni_leeds import uni_leeds
from scraper_files.uni_sheffield import uni_sheffield

from scraper_files.lund_uni import lund_uni
from scraper_files.kth_royal import kth_royal
from scraper_files.uni_nottingham import uni_nottingham
from scraper_files.penn_state_uni import penn_state_uni

from scraper_files.tud import tud
from scraper_files.uni_helinski import uni_helinski
from scraper_files.washu import washu

from scraper_files.ohio_state_uni import ohio_state_uni
from scraper_files.purdue_uni import purdue_uni

from scraper_files.nagoya_uni import nagoya_uni
from scraper_files.uc_davis import uc_davis
from scraper_files.uni_oslo import uni_oslo
from scraper_files.queen_mary_uni import queen_mary_uni
from scraper_files.uni_bern import uni_bern
from scraper_files.uni_berlin import uni_berlin
from scraper_files.uni_montreal import uni_montreal


from scraper_files.uni_southern_california import uni_southern_california
from scraper_files.utrecht_uni import utrecht_uni

from scraper_files.uppsala_uni import uppsala_uni
from scraper_files.aalto_uni import aalto_uni
from scraper_files.leiden_uni import leiden_uni
from scraper_files.uni_groningen import uni_groningen
from scraper_files.frieie_uni import frieie_uni
from scraper_files.upm import upm
from scraper_files.uts_sydney import uts_sydney
from scraper_files.lancaster_uni import lancaster_uni



from scraper_files.hokkaido_uni import hokkaido_uni
from scraper_files.usm_malaysia import usm_malaysia

from scraper_files.mcmaster_uni import mcmaster_uni

from scraper_files.hanyang_uni import hanyang_uni
from scraper_files.aarhus_uni import aarhus_uni
from scraper_files.technical_uni_berlin import technical_uni_berlin

from scraper_files.uni_york import uni_york

from scraper_files.uc_santa_barbara import uc_santa_barbara
from scraper_files.uni_maryland import uni_maryland
from scraper_files.uni_pittsburgh import uni_pittsburgh
from scraper_files.michigan_state_uni import michigan_state_uni
from scraper_files.emory_college import emory_college
from scraper_files.cardiff_uni import cardiff_uni
from scraper_files.ens_lyon import ens_lyon
from scraper_files.case_western_reserve_uni import case_western_reserve_uni
from scraper_files.uni_florida import uni_florida
from scraper_files.uni_exeter import uni_exeter
from scraper_files.uni_rochester import uni_rochester
from scraper_files.uni_waterloo import uni_waterloo
from scraper_files.sapienza_uni import sapienza_uni

from scraper_files.uni_bath import uni_bath
from scraper_files.uni_tubingen import uni_tubingen


from scraper_files.uni_college_dublin import uni_college_dublin
from scraper_files.uni_minnesota import uni_minnesota

from scraper_files.uni_liverpool import uni_liverpool

from scraper_files.uni_otago import uni_otago
from scraper_files.iisc_blr import iisc_blr
from scraper_files.kfupm import kfupm
from scraper_files.uni_tech_malaysia import uni_tech_malaysia

from scraper_files.tu_wien import tu_wien
from scraper_files.uni_bergen import uni_bergen
from scraper_files.uni_gottingen import uni_gottingen
from scraper_files.uni_wollongong import uni_wollongong

from scraper_files.uni_twente import uni_twente


from scraper_files.dartmouth import dartmouth
from scraper_files.western_uni import western_uni
from scraper_files.uni_reading import uni_reading
from scraper_files.uni_aberdeen import uni_aberdeen
from scraper_files.chula_engg import chula_engg
from scraper_files.queen_mary_uni import queen_mary_uni
from scraper_files.uc_irvine import uc_irvine
from scraper_files.khalifa_uni import khalifa_uni
from scraper_files.uni_notre_dame import uni_notre_dame
from scraper_files.macquarie_uni import macquarie_uni
from scraper_files.radboud_uni import radboud_uni
from scraper_files.uni_padova import uni_padova
from scraper_files.curtin_uni import curtin_uni
from scraper_files.queensland_uni_tech import queensland_uni_tech
from scraper_files.uni_virginia import uni_virginia

from scraper_files.uni_cape_town import uni_cape_town

from scraper_files.victoria_uni_wellington import victoria_uni_wellington
from scraper_files.st_petersburg_state_uni import st_petersburg_state_uni
from scraper_files.loughbourough_uni import loughborough_uni
from scraper_files.novosibirsk_state_uni import novosibirsk_state_uni

from scraper_files.georgetown_uni import georgetown_uni
from scraper_files.telaviv_uni import telaviv_uni

from scraper_files.unicamp import unicamp
from scraper_files.maastritcht_uni import maastritcht_uni
from scraper_files.national_cheng_kung_uni import national_cheng_kung_uni
from scraper_files.kyung_hee_uni import kyung_hee_uni
from scraper_files.uni_galway import uni_galway
from scraper_files.uni_antwerp import uni_antwerp
from scraper_files.national_yang_ming_chiao_tung_uni import national_yang_ming_chiao_tung_uni
from scraper_files.uni_bonn import uni_bonn
from scraper_files.uni_leicester import uni_leicester

from scraper_files.queens_uni import queens_uni
from scraper_files.uni_calgary import uni_calgary
from scraper_files.uni_sussex import uni_sussex

from scraper_files.mahidol_uni import mahidol_uni
from scraper_files.universiti_brunei_darussalm import universiti_brunei_darussalam
from scraper_files.uni_tokyo import uni_tokyo


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
        writer.writerows(uni_glasgow)
        writer.writerows(georgia_inst_tech())
        writer.writerows(uni_illinois())
        writer.writerows(durham_uni())
        writer.writerows(yonsei_uni())
        writer.writerows(uni_birmingham())
        writer.writerows(uni_southampton())
        writer.writerows(uni_leeds())
        writer.writerows(uni_sheffield())
        writer.writerows(lund_uni())
        writer.writerows(kth_royal())
        writer.writerows(uni_nottingham())
        writer.writerows(penn_state_uni())
        writer.writerows(tud())
        writer.writerows(uni_helinski())
        writer.writerows(washu())
        writer.writerows(ohio_state_uni())
        writer.writerows(purdue_uni())
        writer.writerows(nagoya_uni())
        writer.writerows(uc_davis())
        writer.writerows(uni_oslo())
        writer.writerows(queen_mary_uni())
        writer.writerows(uni_bern())
        writer.writerows(uni_berlin())
        writer.writerows(uni_montreal())
        writer.writerows(uni_southern_california())
        writer.writerows(utrecht_uni())
        writer.writerows(uppsala_uni())
        writer.writerows(aalto_uni())
        writer.writerows(leiden_uni())
        writer.writerows(uni_groningen())
        writer.writerows(frieie_uni())
        writer.writerows(upm())
        writer.writerows(uts_sydney())
        writer.writerows(lancaster_uni())
        writer.writerows(hokkaido_uni())
        writer.writerows(usm_malaysia())
        writer.writerows(mcmaster_uni())
        writer.writerows(hanyang_uni())
        writer.writerows(aarhus_uni())
        writer.writerows(technical_uni_berlin())
        writer.writerows(uni_york())
        writer.writerows(uc_santa_barbara())
        writer.writerows(uni_maryland())
        writer.writerows(uni_pittsburgh())
        writer.writerows(michigan_state_uni())
        writer.writerows(emory_college())
        writer.writerows(cardiff_uni())
        writer.writerows(ens_lyon())
        writer.writerows(case_western_reserve_uni())
        writer.writerows(uni_florida())
        writer.writerows(uni_exeter())
        writer.writerows(uni_rochester())
        writer.writerows(uni_waterloo())
        writer.writerows(sapienza_uni())
        writer.writerows(uni_bath())
        writer.writerows(uni_tubingen())
        writer.writerows(uni_college_dublin())
        writer.writerows(uni_minnesota())
        writer.writerows(uni_liverpool())
        writer.writerows(uni_otago())
        writer.writerows(iisc_blr())
        writer.writerows(kfupm())
        writer.writerows(uni_tech_malaysia())
        writer.writerows(tu_wien())
        writer.writerows(uni_bergen())
        writer.writerows(uni_gottingen())
        writer.writerows(uni_wollongong())
        writer.writerows(uni_twente())
        writer.writerows(dartmouth())
        writer.writerows(western_uni())
        writer.writerows(uni_reading())
        writer.writerows(uni_aberdeen())
        writer.writerows(chula_engg())
        writer.writerows(queen_mary_uni())
        writer.writerows(uc_irvine())
        writer.writerows(khalifa_uni())
        writer.writerows(uni_notre_dame())
        writer.writerows(macquarie_uni())
        writer.writerows(radboud_uni())
        writer.writerows(uni_padova())
        writer.writerows(curtin_uni())
        writer.writerows(queensland_uni_tech())
        writer.writerows(uni_virginia())
        writer.writerows(uni_cape_town())
        writer.writerows(victoria_uni_wellington())
        writer.writerows(st_petersburg_state_uni())
        writer.writerows(loughborough_uni())
        writer.writerows(novosibirsk_state_uni())
        writer.writerows(georgetown_uni())
        writer.writerows(telaviv_uni())
        writer.writerows(unicamp())
        writer.writerows(maastritcht_uni())
        writer.writerows(national_cheng_kung_uni())
        writer.writerows(kyung_hee_uni())
        writer.writerows(uni_galway())
        writer.writerows(uni_antwerp())
        writer.writerows(national_yang_ming_chiao_tung_uni())
        writer.writerows(uni_bonn())
        writer.writerows(uni_leicester())
        writer.writerows(queens_uni())
        writer.writerows(uni_calgary())
        writer.writerows(uni_sussex())
        writer.writerows(mahidol_uni())
        writer.writerows(universiti_brunei_darussalam())
        writer.writerows(uni_tokyo())

if __name__ == "__main__":
    main()
