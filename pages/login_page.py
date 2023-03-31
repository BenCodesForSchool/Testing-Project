from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import time

class LoginPage:
    #Finding the email and password text boxes, as well as the login button and the link to the products section of the website
    EMAIL_INPUT = (By.XPATH, "//*[@data-qa='login-email']")
    PASSWORD_INPUT = (By.XPATH, '//*[@data-qa="login-password"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-qa="login-button"]')
    PRODUCTS_LINK =prod_link = (By.XPATH, "//div[@class='shop-menu pull-right']//a[@href='/products']")
    PESKY_IFRAME = (By.XPATH, "//iframe[contains(@name, 'aswift') and contains(@style, 'visibility: visible')]")
    DISMISS_BUTTON = (By.XPATH, "//div[@id='dismiss-button']")
    AD_IFRAME = (By.ID, "ad_iframe")

    def __init__(self, driver):
        self.driver = driver
    #Filling credentials based on specified inputs, clicking the login button
    def login(self, email, password):
        email_input = self.driver.find_element(*self.EMAIL_INPUT)
        password_input = self.driver.find_element(*self.PASSWORD_INPUT)
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)

        email_input.send_keys(email)
        password_input.send_keys(password)
        login_button.click()
    #Clicking the link to go to the products page
    def go_to_products_page(self):
        products_link = self.driver.find_element(*self.PRODUCTS_LINK)
        products_link.click()
        if "https://automationexercise.com/#google_vignette" in self.driver.current_url:
            self.driver.back()
            products_link.click()
