import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import FirefoxProfile
import random

firefox_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'
service = Service(executable_path="D:\C DRIVE STUFF\Downloads\geckodriver-v0.32.2-win32\geckodriver.exe")
options = Options()
options.set_preference("browser.startup.homepage", "https://www.google.com/")
options.set_preference("browser.cache.disk.enable", False)
options.set_preference("browser.cache.memory.enable", False)
options.set_preference("browser.cache.offline.enable", False)
options.set_preference("network.http.use-cache", False)
options.add_argument("--user-data-dir=D:/Selenium Projects")
#options.add_argument('-headless')
options.binary_location = firefox_path
driver = webdriver.Firefox(service=service, options=options)
wait = WebDriverWait(driver, 10)
driver.install_addon(r"D:/C DRIVE STUFF/Downloads/uBlock0_1.47.4.firefox.signed.xpi", temporary=True)
driver.get("https://automationexercise.com")





login_link = driver.find_element(By.XPATH, "//a[@href='/login']")

login_link.click()


email_box = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/section/div/div/div[1]/div/form/input[2]")))
pass_box = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/section/div/div/div[1]/div/form/input[3]")))
login_button = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/section/div/div/div[1]/div/form/button")))
email_box.send_keys("bweiler@qac.com")
pass_box.send_keys("password")
login_button.click()

prod_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/products']")))
prod_link.click()
time.sleep(2)

product_search = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="search_product"]')))
search_butt = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="submit_search"]')))

product_search.send_keys("tshirts")
search_butt.click()

nummaShirts = 0
shirts = driver.find_elements(By.CLASS_NAME, "btn btn-default add-to-cart")
selected_shirts = random.sample(shirts, k=2)

for shirt in selected_shirts:
    shirt.click()
    nummaShirts += 1
    if(nummaShirts == 2):
        viewCart = webdriver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div/div[1]/div/div/div[2]/p[2]/a")
        viewCart.click()
    else:
        continueShopping = webdriver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div/div[1]/div/div/div[3]/button")
        continueShopping.click()


driver.quit()