from selenium.webdriver.common.by import By

class LoginPage:
    EMAIL_INPUT = (By.XPATH, "//*[@data-qa='login-email']")
    PASSWORD_INPUT = (By.XPATH, '//*[@data-qa="login-password"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-qa="login-button"]')
    PRODUCTS_LINK =prod_link = (By.XPATH, "//div[@class='shop-menu pull-right']//a[@href='/products']")

    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        email_input = self.driver.find_element(*self.EMAIL_INPUT)
        password_input = self.driver.find_element(*self.PASSWORD_INPUT)
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)

        email_input.send_keys(email)
        password_input.send_keys(password)
        login_button.click()
    
    def go_to_products_page(self):
        products_link = self.driver.find_element(*self.PRODUCTS_LINK)
        products_link.click()