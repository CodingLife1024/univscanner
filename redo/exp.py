from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Path to the ChromeDriver executable
chrome_driver_path = "univscanner/selenium_chromedriver/chromedriver.exe"

# Create a Service object
service = Service(executable_path=chrome_driver_path)

# Create an Options object
options = Options()

# Set the User-Agent string
user_agent = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36"
options.add_argument(f"user-agent={user_agent}")

# Disable WebDriver flags
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Add a delay before navigating to the URL
time.sleep(5)

# Navigate to the specified URL
driver.get("https://findanexpert.unimelb.edu.au/profile/1601-atif-ahmad")

# Print the page source
print(driver.page_source)

# Quit the WebDriver
driver.quit()
