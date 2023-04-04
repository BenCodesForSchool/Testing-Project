from selenium.webdriver.common.by import By

class HomePage:
    #Finding the link to the login page
    LOGIN_LINK = (By.XPATH, './/a[@href="/login"]')
    HOMEPAGE_LINK = "https://automationexercise.com"

    def __init__(self, driver):
        self.driver = driver
    #Clicking the link to the login page
    def go_to_login_page(self):
        login_link = self.driver.find_element(*self.LOGIN_LINK)
        login_link.click()
    #Simply navigating to the homepage
    def navigate(self):
        self.driver.get(self.HOMEPAGE_LINK)