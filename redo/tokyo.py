import requests
from bs4 import BeautifulSoup
import re

university = "University of Tokyo"
country = "Japan"

def tokyo():
    url = "https://www.i.u-tokyo.ac.jp/edu/course/cs/members_e.shtml"  # homepage url

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    r = requests.get(url, headers=headers)

    faculty_data = []

    keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer", "computer architecture", "fpga"]

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(r.text, 'html.parser')

    # Find the table
    table = soup.find('table')

    faculty_data = []

    # Iterate over the rows in the table (excluding the header row)
    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        if len(cols) == 2:
            name_col = cols[0]
            research_col = cols[1]

            # Extract the name and link
            name_tag = name_col.find('a')
            name = name_tag.get_text(strip=True)
            link = name_tag['href']

            # Extract the research area
            research_area = research_col.get_text(strip=True)

            # Append the extracted data to the list
            found_keyword = any(re.search(re.escape(keyword), research_area.lower()) for keyword in keyword_list)

            if found_keyword:
                faculty_data.append([university, country, name, 'Email not found', link, 'Personal URL not found'])
                print([university, country, name, 'Email not found', link, 'Personal URL not found', research_area])
                print()

    print()
    print("University of Tokyo done...")
    print()
    return faculty_data


if __name__ == '__main__':
    tokyo()
