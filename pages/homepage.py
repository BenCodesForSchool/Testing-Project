from selenium.webdriver.common.by import By

class HomePage:
    #Finding the link to the login page
    LOGIN_LINK = (By.XPATH, "//div[@class='shop-menu pull-right']//a[@href='/login']")

    def __init__(self, driver):
        self.driver = driver
    #Clicking the link to the login page
    def go_to_login_page(self):
        login_link = self.driver.find_element(*self.LOGIN_LINK)
        login_link.click()