from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("http://localhost:3000/seller/products")
time.sleep(5)
driver.find_element(By.XPATH, '/html/body/div/div/div[4]/div[1]/div/button[2]').click()
driver.find_element(By.XPATH, '/html/body/div/div/div[4]/div[1]/div/button[1]').click()

