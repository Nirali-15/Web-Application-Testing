from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("http://localhost:3000")
driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/nav/div/a[5]').click()

#Login As a Seller
driver.find_element(By.NAME, "email").send_keys("admin@gmail.com")
driver.find_element(By.NAME, "password").send_keys("admin@15")

#selecting role
role_dropdown = Select(driver.find_element(By.NAME, "role"))
role_dropdown.select_by_visible_text("Seller")
checkbox = driver.find_element(By.NAME, "rememberMe")
if not checkbox.is_selected():
    checkbox.click()
driver.find_element(By.XPATH, "//button[text()='Login']").click()
time.sleep(5)

#click on Add-Product to add the products
driver.find_element(By.XPATH, '//*[@id="root"]/div/div/nav/div[2]/a[2]').click()
# Adding Product by filling all details in the form
driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/form/input[1]').send_keys("Mango")
driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/input[2]').send_keys("20")
select_element = driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/select')
dropdown = Select(select_element)
dropdown.select_by_visible_text("Fruits")
driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/input[3]').send_keys("KG")
driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/input[4]').send_keys("10")
driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/input[5]').send_keys("15/04/2025")
driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/textarea[1]').send_keys("Fresh Farm Mangoes.")
driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/textarea[2]')
driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/input[6]').send_keys("Kelapur")
driver.find_element(By.NAME, "organic").click()
upload_input = driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/input[7]')
upload_input.send_keys(r"C:\Users\alifb\Downloads\mango.jpeg")
driver.find_element(By.XPATH, "/html/body/div/div/div/div/form/button").click()
time.sleep(4)

#LOGIN AS A BUYER
driver.get("http://localhost:3000/login")
time.sleep(3)
driver.find_element(By.NAME, "email").send_keys("admin@gmail.com")
driver.find_element(By.NAME, "password").send_keys("admin@15")

#selecting role
role_dropdown = Select(driver.find_element(By.NAME, "role"))
role_dropdown.select_by_visible_text("Buyer")
checkbox = driver.find_element(By.NAME, "rememberMe")
if not checkbox.is_selected():
    checkbox.click()
driver.find_element(By.XPATH, "//button[text()='Login']").click()
time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="root"]/div/div/section[1]/div/a[1]').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div/div/input').send_keys("20")
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div/button').click()
alert = Alert(driver)
alert.accept()
time.sleep(3)

#CART
driver.get("http://localhost:3000/cart")
wait = WebDriverWait(driver, 10)
driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div/button').click()
time.sleep(4)

driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/input[1]').send_keys("Rakesh Patil")
driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/input[2]').send_keys("Bamboo FarmHouse, Near Royal Resort")
driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/input[3]').send_keys("Nashik, Maharashtra")
driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/input[4]').send_keys("420003")
driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/input[5]').send_keys("9876543210")

driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/div[7]').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/button').click()
time.sleep(10)
driver.close()
