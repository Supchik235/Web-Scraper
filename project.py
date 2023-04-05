from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

email = "example@example.com"
password = "12345"
username = "slipperypenguin"
mobile_number = "0400123456"
date_of_birth = "01/01/1990"

url = "https://betflux.com.au/registration/step-1"

chrome_path = "/Users/danielgant/Downloads/chromedriver"
service = Service(chrome_path)

driver = webdriver.Chrome(service=service)

driver.get(url)

# wait for the page to load and the elements to become visible
wait = WebDriverWait(driver, 10)
email_input = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
username_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
mobile_input = wait.until(EC.visibility_of_element_located((By.NAME, "mobile_number")))
dob_input = wait.until(EC.visibility_of_element_located((By.NAME, "date_of_birth")))

# enter the details
email_input.send_keys(email)
password_input.send_keys(password)
username_input.send_keys(username)
mobile_input.send_keys(mobile_number)
dob_input.send_keys(date_of_birth)

# wait for the user to press Enter before exiting
input("Press Enter to exit...")
driver.quit()
