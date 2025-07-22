from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("http://localhost:3000/seller/add-product")
time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/form/input[1]').send_keys("Mango")
driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/input[2]').send_keys("20")
select_element = driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/select')
dropdown = Select(select_element)
dropdown.select_by_visible_text("Fruits")
driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/input[3]').send_keys("KG")
driver.find_element(By.XPATH,'/html/body/div/div/div/div/form/input[4]').send_keys("10")
driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/input[5]').send_keys("15/04/2025")
driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/textarea[1]').send_keys("Fresh Farm Mangoes.")
driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/textarea[2]')
driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/input[6]').send_keys("Kelapur")

driver.find_element(By.NAME, "organic").click()
upload_input=driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/input[7]')
upload_input.send_keys(r"C:\users\alifb\Downloads\mango.jpeg")
driver.find_element(By.XPATH, "/html/body/div/div/div/div/form/button").click()
time.sleep(4)
driver.close()