import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile
from components.GLOBAL_VARIABLES import keyword_list

faculty_data = []

u_name = "Michigan State University"
country = "United Kingdom"

def get_name(prof):
    name = prof.find('h2').text.strip()
    return name

def get_link(prof):
    link = "https://engineering.msu.edu" + prof.find('a')['href']
    return link

def get_title(prof):
    title = prof.find('p').text.strip().lower()
    return title

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_ttile = executor.submit(get_title, prof)

        name = future_name.result()
        link = future_link.result()
        title = future_ttile.result()

    if "professor" in title or "lecturer" in title:
        new_r = requests.get(link)
        new_soup = BeautifulSoup(new_r.text, "html.parser")
        research = new_soup.find('section', class_="expert-detail faculty").text if new_soup.find('section', class_="expert-detail faculty") else "N/A"
        email_tag = new_soup.find('a', href=re.compile(r'^mailto:'))
        email = email_tag.text if email_tag else "N/A"

        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)
        if found_keyword:
            pers_link = get_scholar_profile(name)
            if [u_name, country, name, email, link, pers_link] not in faculty_data:
                faculty_data.append([u_name, country, name, email, link, pers_link])
                print([u_name, country, name, email, link, pers_link])

def michigan_state_uni():
    urls = ["https://engineering.msu.edu/faculty?employments=24a15d4c-1460-48c4-8714-e44066304ad0&departments=a6ab65f8-3fbd-4da1-85f9-c5ddde8b069e|61aa9513-d18a-49bb-a644-23da88a14f4b&letter=",
            "https://engineering.msu.edu/faculty?page=2&departments=a6ab65f8-3fbd-4da1-85f9-c5ddde8b069e%7c61aa9513-d18a-49bb-a644-23da88a14f4b&offices=all&employments=24a15d4c-1460-48c4-8714-e44066304ad0&areas=all&ps=89d8ab1f-3230-4875-9070-588de69ac965",
            "https://engineering.msu.edu/faculty?page=3&departments=a6ab65f8-3fbd-4da1-85f9-c5ddde8b069e%7c61aa9513-d18a-49bb-a644-23da88a14f4b&offices=all&employments=24a15d4c-1460-48c4-8714-e44066304ad0&areas=all&ps=89d8ab1f-3230-4875-9070-588de69ac965",
            "https://engineering.msu.edu/faculty?page=4&departments=a6ab65f8-3fbd-4da1-85f9-c5ddde8b069e%7c61aa9513-d18a-49bb-a644-23da88a14f4b&offices=all&employments=24a15d4c-1460-48c4-8714-e44066304ad0&areas=all&ps=89d8ab1f-3230-4875-9070-588de69ac965",
            "https://engineering.msu.edu/faculty?page=5&departments=a6ab65f8-3fbd-4da1-85f9-c5ddde8b069e%7c61aa9513-d18a-49bb-a644-23da88a14f4b&offices=all&employments=24a15d4c-1460-48c4-8714-e44066304ad0&areas=all&ps=89d8ab1f-3230-4875-9070-588de69ac965",
            "https://engineering.msu.edu/faculty?page=6&departments=a6ab65f8-3fbd-4da1-85f9-c5ddde8b069e%7c61aa9513-d18a-49bb-a644-23da88a14f4b&offices=all&employments=24a15d4c-1460-48c4-8714-e44066304ad0&areas=all&ps=89d8ab1f-3230-4875-9070-588de69ac965",
            "https://engineering.msu.edu/faculty?page=7&departments=a6ab65f8-3fbd-4da1-85f9-c5ddde8b069e%7c61aa9513-d18a-49bb-a644-23da88a14f4b&offices=all&employments=24a15d4c-1460-48c4-8714-e44066304ad0&areas=all&ps=89d8ab1f-3230-4875-9070-588de69ac965"]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('div', class_="details")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nMichigan State University done...\n")
    return faculty_data



if __name__ == "__main__":
    michigan_state_uni()
