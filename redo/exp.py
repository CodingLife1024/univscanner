from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

def fetch_and_parse():
    url = "https://findanexpert.unimelb.edu.au/profile/1601-atif-ahmad"

    # Set up the Selenium WebDriver (using Chrome in this example)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode (without a GUI)
    service = ChromeService(executable_path="path/to/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)

    # Navigate to the page
    driver.get(url)

    # Wait for the page to load (adjust the wait time if necessary)
    time.sleep(5)

    # Extract the page source and parse it with BeautifulSoup
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")

    # Close the WebDriver session
    driver.quit()

    # Print all the text from the page
    print(soup.get_text())

fetch_and_parse()
