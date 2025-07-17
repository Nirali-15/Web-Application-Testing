from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("http://localhost:3000/login")
time.sleep(3)
driver.find_element(By.NAME, "email").send_keys("admin@gmail.com")
driver.find_element(By.NAME,"password").send_keys("admin@15")

#selecting role
role_dropdown = Select(driver.find_element(By.NAME, "role"))
role_dropdown.select_by_visible_text("Buyer")
checkbox=driver.find_element(By.NAME,"rememberMe")
if not checkbox.is_selected():
    checkbox.click()
driver.find_element(By.XPATH, "//button[text()='Login']").click()
time.sleep(15)
