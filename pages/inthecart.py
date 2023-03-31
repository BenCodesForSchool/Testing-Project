from selenium.webdriver.common.by import By
import random

class InTheCart:
    #Getting the delete and checkout buttons
    DELETE_BUTTONS = (By.CLASS_NAME, "cart_quantity_delete")
    CHECKOUT_BUTTON = (By.XPATH, '//div[@class="col-sm-6"]/descendant::a')

    def __init__(self, driver):
        self.driver = driver
    
    def delete_items(self, num_of_items):
        #collecting all the delete buttons
        deletes = self.driver.find_elements(*self.DELETE_BUTTONS)
        #randomly selecting as many delete buttons as specified
        selected_deletes = random.sample(deletes, k=num_of_items)
        #clicking all of the randomly selected delete buttons
        for delete in selected_deletes:
            delete.click()
    
    def proceed_to_checkout(self):
        #clicking the button to proceed to checkout
        checkout_butt = self.driver.find_element(*self.CHECKOUT_BUTTON)
        checkout_butt.click()
        if "https://automationexercise.com/#google_vignette" in self.driver.current_url:
            self.driver.back()
            checkout_butt.click()
