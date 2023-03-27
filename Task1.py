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
options.add_argument("--user-data-dir=D:/Testing-Project")
options.add_argument('-headless')
driver = webdriver.Firefox(service=service, options=options, firefox_binary=firefox_path)

driver.get("https://automationexercise.com")

login_button = driver.find_element_by_xpath("//a[@href='/login']")

login_button.click()
driver.save_screenshot("login_clicked.png")