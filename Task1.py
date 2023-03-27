import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

firefox_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'
service = Service(executable_path="D:\C DRIVE STUFF\Downloads\geckodriver-v0.32.2-win32\geckodriver.exe")
options = Options()
options.add_argument("--user-data-dir=D:/Selenium Projects")
options.add_argument('-headless')
options.binary_location = firefox_path
driver = webdriver.Firefox(service=service, options=options)

driver.get("https://automationexercise.com")

login_link = driver.find_element(By.XPATH, "//a[@href='/login']")

login_link.click()
#driver.save_screenshot("login_clicked.png")

email_box = driver.find_element(By.XPATH, "/html/body/section/div/div/div[1]/div/form/input[2]")
pass_box = driver.find_element(By.XPATH, "/html/body/section/div/div/div[1]/div/form/input[3]")
login_button = driver.find_element(By.XPATH, "/html/body/section/div/div/div[1]/div/form/button")
email_box.send_keys("bweiler@qac.com")
pass_box.send_keys("password")
login_button.click()
time.sleep(5)

driver.save_screenshot("loggedin.png")


driver.quit()