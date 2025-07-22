from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By

serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("http://localhost:3000/login")
time.sleep(3)
driver.find_element(By.NAME, "email").send_keys("admin@gmail.com")
driver.find_element(By.NAME,"password").send_keys("admin@15")

actual_title=driver.title
expected_title ="FarmFlow"
if actual_title == expected_title:
    print("Login Successful")
else:
    print("Login Failed")

driver.close()

