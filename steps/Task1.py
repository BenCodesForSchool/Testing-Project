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





login_link = driver.find_element(By.XPATH, "//div[@class='shop-menu pull-right']//a[@href='/login']")

login_link.click()


email_box = driver.find_element(By.XPATH, "//*[@data-qa='login-email']")

pass_box = driver.find_element(By.XPATH, "//*[@data-qa='login-password']")
login_button = driver.find_element(By.XPATH, "//*[@data-qa='login-button']")
email_box.send_keys("bweiler@qac.com")
pass_box.send_keys("password")
login_button.click()

prod_link = driver.find_element(By.XPATH, "//div[@class='shop-menu pull-right']//a[@href='/products']")
prod_link.click()


product_search = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="search_product"]')))
search_butt = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="submit_search"]')))
product_search.send_keys("tshirts")
search_butt.click()

numShirts = 0
shirts = driver.find_elements(By.XPATH, "//div[@class='productinfo text-center']//a[contains(text(), 'Add to cart')]")

selected_shirts = random.sample(shirts, k=2)

for shirt in selected_shirts:
    shirt.click()
    numShirts += 1
    if numShirts == 1:
        continueShopping = driver.find_element(By.XPATH, "//div[@class='modal-footer']/descendant::button")
        continueShopping.click()

viewCart = driver.find_element(By.XPATH, "//div[@class='modal-body']/descendant::a")
viewCart.click()

deletes = driver.find_elements(By.CLASS_NAME, "cart_quantity_delete")
random_shirt_to_delete = random.choice(deletes)
random_shirt_to_delete.click()

checkout_butt = driver.find_element(By.XPATH, '//div[@class="col-sm-6"]/descendant::a')
checkout_butt.click()

order_butt = driver.find_element(By.XPATH, "//a[@class='btn btn-default check_out']")
order_butt.click()

nameOnCard = driver.find_element(By.XPATH, "//input[@name='name_on_card']")
nameOnCard.send_keys("Joseph Mama")

cardNumber = driver.find_element(By.XPATH, "//input[@name='card_number']")
cardNumber.send_keys("1234567891011121")

cvc = driver.find_element(By.XPATH, "//input[@name='cvc']")
cvc.send_keys("123")

ex_month = driver.find_element(By.XPATH, "//input[@name='expiry_month']")
ex_month.send_keys("03")

ex_year = driver.find_element(By.XPATH, "//input[@name='expiry_year']")
ex_year.send_keys("2023")

confirm_payment_butt = driver.find_element(By.XPATH, '//div[@class="form-row"]//button[@id="submit"]')
confirm_payment_butt.click()

invoice_butt = driver.find_element(By.XPATH, "//div[@class='row']//a[@class='btn btn-default check_out']")
invoice_butt.click()

driver.quit()