import requests
import urllib.request
import time
import urllib
import re
import csv
import time
from bs4 import BeautifulSoup

def Belarusian_State_University():
    url = "https://bsu.by/en/structure/faculties/kafedry/kafedra-kompyuternykh-tekhnologiy-i-sistem-d/head"   # homepage url
    #headers = {
    #'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    #}
    r = requests.get(url, verify=False)
    # getting the soup by parsing the html parsel to text to request r
    soup = BeautifulSoup(r.text, "html.parser")

    # file initialization to write
    filename = "Belarusian_State_University.txt"
    f = open(filename, "w")

    excel_filename = "Belarusian_State_University"
    f2 = open(excel_filename, "w")
    csvwriter = csv.writer(f2)

    overall_file = "all_emails.csv"
    f3 = open(overall_file, "a")
    csvwriter2 = csv.writer(f3)

    u_name = "Belarusian State University"
    country = "Belarus"

    garbage_emails = []
    var = [f,csvwriter, csvwriter2, u_name, country]
    print(soup)
    # d gives the array of all profs on the dept homepage
    # d = soup.find('a', {'class':"accordian-title"})
    d = soup.find('div',{"class":"list-people"})
    dd = d.find_all('div',{"class":"list-people__info"})
    print(d)
    #iterating for every prof
    #print(d)
    for i in d:
        a = i
       # if type(a)!=int  :                  # a contains the name and the homepage of prof
        link =  a.get('href')                # extracting prof page link
        name = a.get_text()
        print(name, link)              # extracting prof name
        try:
            prof_resp = requests.get(link)
            #print(prof_resp)
        except:
            continue
        email = "Not Found"

        OnlygetEmail(var, garbage_emails, name, link, email, prof_resp)


    f.close()
    f2.close()
    f3.close()
    print("Finished")





def OnlygetEmail(var, garbage_emails, name, link, email, prof_resp):
    f = var[0]
    csvwriter = var[1]
    csvwriter2 = var[2]

    u_name = var[3]
    country = var[4]

    prof_soup = BeautifulSoup(prof_resp.text, "html.parser")

    if email != 'Not Found':
        f.write(link + '\n' + name + "\t"+ email + "\n")
        csvwriter.writerow([u_name, country, name, email, link])
        csvwriter2.writerow([u_name, country, name, email, link])
    else:
        new_emails = set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", prof_resp.text))
        for eemail in garbage_emails:
            if eemail in new_emails:
                new_emails.remove(eemail)
        if len(new_emails) == 0:
            email = "Email Not Found"
            f.write(link + '\n' + name + "\t"+ email + "\n")
            csvwriter.writerow([u_name, country, name, email, link])
            csvwriter2.writerow([u_name, country, name, email, link])
        else:
            # f.write(link + '\n' + name)
            for email in new_emails:
                f.write(link + '\n' + name + '\t\t' + email + '\n')
                csvwriter.writerow([u_name, country, name, email, link])
                csvwriter2.writerow([u_name, country, name, email, link])
            # f.write("\n")


    f.write('\n\n')


if __name__ == '__main__':
    Belarusian_State_University()

