from selenium.webdriver.common.by import By

class CheckoutPage:
    PLACE_ORDER_BUTTON = (By.XPATH, "//a[@class='btn btn-default check_out']")

    def __init__(self, driver):
        self.driver = driver
    
    def place_order(self):
        place_order = self.driver.find_element(*self.PLACE_ORDER_BUTTON)
        place_order.click()