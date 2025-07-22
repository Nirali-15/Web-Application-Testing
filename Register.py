from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("http://localhost:3000/signup")

driver.find_element(By.NAME, "fullName").send_keys("admin")
driver.find_element(By.NAME, "username").send_keys("Nirali")
driver.find_element(By.NAME, "email").send_keys("admin@gmail.com")
driver.find_element(By.NAME, "phone").send_keys("9876543210")
driver.find_element(By.NAME, "password").send_keys("admin@123")
driver.find_element(By.NAME, "confirmPassword").send_keys("admin@123")
driver.find_element(By.NAME, "acceptTerms").click()
driver.find_element(By.XPATH, "//button[contains(text(), 'Sign Up')]").click()

time.sleep(5)
