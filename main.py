import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver_win32\chromedriver.exe"
USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')

ser = Service(executable_path=chrome_driver_path)

driver = webdriver.Chrome(service=ser)
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&f_WT=2&geoId=102257491&keywords=python%20developer"
           "&location=London%2C%20England%2C%20United%20Kingdom")
sign_in_btn = driver.find_element(by="xpath", value="/html/body/div[1]/header/nav/div/a[2]").click()
time.sleep(2)
username = driver.find_element(by="id", value="username")
username.send_keys(USERNAME)
password = driver.find_element(by="id", value="password")
password.send_keys(PASSWORD)
login_btn = driver.find_element(by="xpath", value='//*[@id="organic-div"]/form/div[3]/button').click()
for job_list in driver.find_elements(by="css selector", value=".job-card-container--clickable"):
    job_list.click()
    time.sleep(2)
    driver.find_element(by="xpath", value="/ html / body / div[6] / div[3] / div[3] / div[2] / div / section[2] / div / div / div[1] / div / div[1] / div / \
      div[2] / div[3] / div / button").click()


driver.quit()
