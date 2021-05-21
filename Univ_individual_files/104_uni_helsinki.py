import requests
import urllib.request
import time
import urllib
import re
import csv
import sys
from bs4 import BeautifulSoup

def uni_helsinki():
    url = "https://www2.helsinki.fi/en/faculty-of-science/research-and-teaching-staff-computer-science"   # homepage url
    r = requests.get(url)                                        # request to url

    # getting the soup by parsing the html parsel to text to request r
    soup = BeautifulSoup(r.text, "html5lib")
    # print(soup.prettify)

    # file initialization to write
    file_name = sys.argv[0]
    file_name = file_name[4:]

    txt_file = file_name.replace(".py", ".txt")
    f = open(txt_file, "w")

    csv_file = file_name.replace(".py", ".csv")
    f2 = open(csv_file, "w")
    csvwriter = csv.writer(f2)

    overall_file = "all_emails.csv"
    f3 = open(overall_file, "a")
    csvwriter2 = csv.writer(f3)

    u_name = "University of Helsinki"
    country = "Finland"

    grabage_emails = []

    var = [f, csvwriter, csvwriter2, u_name, country, grabage_emails]

    # d gives the array of all profs on the dept homepage
    dd = soup.find('div', {'class':'textarea'})
    d = dd.find_all('div', {'class':"expert-atom__content"})

    #iterating for every prof
    for i in d:
        a = i.find('a', {'class':' expert-atom__name-container'})
        if a == None:
            continue
        name = ((a.get_text()).strip())
        name = " ".join(name.split())
        name = name.replace('\n', "")

        link = 'https://www2.helsinki.fi' +a.get('href')

        # check if link is valid on Not
        try:    
            prof_resp = requests.get(link)        
        except:
            continue

        a_mail = i.find('div', {'class':'expert-atom-contact-details__item expert-atom-contact-details__item__mail icon--mail'})
        if a_mail != None:
            email = a_mail.get_text()
        else:
            email = "Not Found"
    
        print(name, email, link)
        filterandgetEmail(var, grabage_emails, name, link, email, prof_resp)

    f.close()
    f2.close()
    f3.close()
    print("Finished")





def filterandgetEmail(var, grabage_emails, name, link, email, prof_resp):
    f = var[0]
    csvwriter = var[1]
    csvwriter2 = var[2]

    u_name = var[3]
    country = var[4]

    keyword_list = ['Computer Architecture','hardware and system architecture', 'hardware and architecture', 'embedded system', 'computer organization','VLSI Design', 'Computer and System',
                    'multiprocessor architecture']
    flag = 1
    prof_soup = BeautifulSoup(prof_resp.text, "html.parser")
    research_text = prof_soup.text
    for pattern in keyword_list:
        if re.search(pattern, research_text, re.IGNORECASE):
            flag = 0
            if email != 'Not Found':
                f.write(link + '\n' + name + "\t"+ email + "\n")
                csvwriter.writerow([u_name, country, name, email, link])
                csvwriter2.writerow([u_name, country, name, email, link])
            else:
                new_emails = set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", prof_resp.text))
                for eemail in grabage_emails:
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
 

            f.write(pattern)
            f.write('\n\n')
            break

if __name__ == '__main__':
    uni_helsinki()
     