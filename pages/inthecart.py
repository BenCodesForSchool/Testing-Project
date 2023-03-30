from selenium.webdriver.common.by import By
import random

class InTheCart:
    DELETE_BUTTONS = (By.CLASS_NAME, "cart_quantity_delete")
    CHECKOUT_BUTTON = (By.XPATH, '//div[@class="col-sm-6"]/descendant::a')

    def __init__(self, driver):
        self.driver = driver
    
    def delete_items(self, num_of_items):
        deletes = self.driver.find_elements(*self.DELETE_BUTTONS)
        selected_deletes = random.sample(deletes, k=num_of_items)
        for delete in selected_deletes:
            delete.click()
    
    def proceed_to_checkout(self):
        checkout_butt = self.driver.find_element(*self.CHECKOUT_BUTTON)
        checkout_butt.click()
