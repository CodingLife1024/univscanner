import requests
from bs4 import BeautifulSoup
import concurrent.futures
from components.google_scholar import get_scholar_profile

# University and country details
u_name = "University of Strathclyde"
country = "UK"

# Keywords list for research interests
keyword_list = [
    "operating system", "robotics", "kernel", "embedded system", 
    "hardware", "computer architecture", "distributed system", 
    "computer organization", "vlsi", "computer and system", 
    "human-computer interaction", "human computer"
]

# List to store faculty data
faculty_data = []

# Function to extract the name of the professor
def get_name(prof):
    name_tag = prof.find('span', class_='staff_name alpha')
    if name_tag:
        name = name_tag.contents[0].strip()  # Get the text before the <br> tag
        return name
    return None

# Function to extract the profile link (if available)
def get_link(prof):
    email_tag = prof.find('a', class_='staff_email')
    if email_tag:
        return email_tag['href']
    return None

# Function to extract the email of the professor
def get_email(prof):
    email_tag = prof.find('a', class_='staff_email')
    if email_tag:
        return email_tag.text.strip()
    return None

# Function to gather faculty data and append it to the list
def get_faculty_data(prof):
    name = get_name(prof)
    link = get_link(prof)
    email = get_email(prof)
    
    if name:  # Ensure that the name exists before continuing
        scholar_profile = get_scholar_profile(name)  # Fetch the Google Scholar profile
        faculty_info = [u_name, country, name, email, link, scholar_profile]
        
        print(faculty_info)
        faculty_data.append(faculty_info)

# Main function to scrape the university webpage
def univ_of_strathclyde():
    url = "https://www.strath.ac.uk/staff/?department=Computer%20and%20Information%20Sciences"
    
    try:
        r = requests.get(url)
        r.raise_for_status()  # Raise an HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []

    soup = BeautifulSoup(r.text, "html.parser")
    all_profs = soup.find_all('div', class_='staff_name')

    if not all_profs:
        print("No professors found on the webpage.")
        return []

    # Use ThreadPoolExecutor for concurrent processing
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()  # Catch any exceptions in the individual threads
            except Exception as e:
                print(f"Error occurred while processing professor data: {e}")

    print("University of Strathclyde scraping done...")
    return faculty_data

# If executed, scrape the website
if __name__ == '__main__':
    faculty_data = univ_of_strathclyde()
