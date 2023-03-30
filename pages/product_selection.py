from selenium.webdriver.common.by import By
import random

class ProductSelection:
    SHIRTS = (By.XPATH, "//div[@class='productinfo text-center']//a[contains(text(), 'Add to cart')]")
    CONTINUE_SHOPPING_BUTTON = (By.XPATH, "//div[@class='modal-footer']/descendant::button")
    VIEWCART = (By.XPATH, "//div[@class='modal-body']/descendant::a")

    def __init__(self, driver):
        self.driver = driver

    def add_products_to_cart(self, num_products):
        num_shirts = 0
        shirts = self.driver.find_elements(*self.SHIRTS)
        selected_shirts = random.sample(shirts, k=num_products)
        for shirt in selected_shirts:
            shirt.click()
            num_shirts += 1
            if num_shirts < num_products:
                continue_shopping = self.driver.find_element(*self.CONTINUE_SHOPPING_BUTTON)
                continue_shopping.click()
            else:
                break
    
    def view_cart(self):
        viewcart = self.driver.find_element(*self.VIEWCART)
        viewcart.click()