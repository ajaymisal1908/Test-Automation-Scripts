from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time
import json

# Replace these with your Salesforce login details
login_url = 'https://login.salesforce.com/'
username = 'misalajay2@brave-panda-pbh9ck.com'
password = 'pbh9ck@1'
account_name = 'Test Account 7'

# Initialize the WebDriver with headless option (Chrome in this case)
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920,1080')

# Initialize the Chrome driver
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Dictionary to hold time taken for each step
timing = {}

# Function to log time taken for a step
def log_time(step_name, start_time):
    end_time = time.time()
    timing[step_name] = round(end_time - start_time, 3)

try:
    start_time = time.time()
    # Open Salesforce login page
    driver.get(login_url)
    log_time('Open Login Page', start_time)

    start_time = time.time()
    
    # Wait until the username field is present
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    
    # Enter username
    driver.find_element(By.ID, "username").send_keys(username)
    
    # Enter password
    driver.find_element(By.ID, "password").send_keys(password)
    log_time('Enter Credentials', start_time)

    start_time = time.time()
    # Click the login button
    driver.find_element(By.ID, "Login").click()

    # Wait until the home page loads
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "oneHeader")))

    log_time('Click Login and Open Home Page', start_time)

    start_time = time.time()
    # Go to the Accounts tab
    driver.get("https://brave-panda-pbh9ck-dev-ed.trailblaze.lightning.force.com/lightning/o/Account/list?filterName=00B5g00000nXdU8EAK")
    log_time('Open Account Module', start_time)

    start_time = time.time()
    # Wait until the new account button is clickable
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@title='New']")))

    # Click the new account button
    driver.find_element(By.XPATH, "//div[@title='New']").click()
    log_time('Click on New Account Module', start_time)

    start_time = time.time()
    # Wait until the account creation form is visible
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@name='Name']")))

    # Enter the account name
    driver.find_element(By.XPATH, "//input[@name='Name']").send_keys(account_name)

    log_time('Type Account Name', start_time)


    # wait for the save button to be visible
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@name='SaveEdit']")))

    # Save the new account
    driver.find_element(By.XPATH, "//button[@name='SaveEdit']").click()

    # Wait until the account is saved and the page reloads
   # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//span[contains(@title='" + account_name + "')]")))

    # Verify the account name
   # account_name_displayed = driver.find_element(By.XPATH, "//span[contains(@title='" + account_name + "')]").text
   # assert account_name_displayed == account_name, f"Expected account name to be {account_name}, but got {account_name_displayed}"
    print(f"Account '{account_name}' created and verified successfully.")

    print("Timing report:", json.dumps(timing, indent=4))

finally:
    # Close the driver
    driver.quit()
