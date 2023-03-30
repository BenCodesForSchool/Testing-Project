from selenium.webdriver.common.by import By
import random
#I created this page in order to handle the fact that the page undergoes a significant change when a search is made. 
class ProductSelection:
    #Finding the buy button for all shirts (or any specified product, really) on the page
    SHIRTS = (By.XPATH, "//div[@class='productinfo text-center']//a[contains(text(), 'Add to cart')]")
    #Finding the button that allows a user to continue shopping after having added an item to the cart
    CONTINUE_SHOPPING_BUTTON = (By.XPATH, "//div[@class='modal-footer']/descendant::button")
    #Finding the button that allows a user to view the cart after having added an item to the cart
    VIEWCART = (By.XPATH, "//div[@class='modal-body']/descendant::a")

    def __init__(self, driver):
        self.driver = driver

    def add_products_to_cart(self, num_products):
        #A variable that helps count how many items have been added to the cart
        num_shirts = 0
        #Collecting all buy buttons into a data structure
        shirts = self.driver.find_elements(*self.SHIRTS)
        #Randomly selecting the specified (2, in this case) number of buy buttons for shirts 
        selected_shirts = random.sample(shirts, k=num_products)
        for shirt in selected_shirts:
            #Clicking the buy buttons for all selected shirts
            shirt.click()
            #Counting how many buy buttons have been clicked
            num_shirts += 1
            if num_shirts < num_products:
                #Clicking on the continue shopping button if not all buy buttons that have been selected have been clicked
                continue_shopping = self.driver.find_element(*self.CONTINUE_SHOPPING_BUTTON)
                continue_shopping.click()
            else:
                #Leaving the loop when all selected buy buttons have been clicked
                break
    
    def view_cart(self):
        #Clicking the view cart button
        viewcart = self.driver.find_element(*self.VIEWCART)
        viewcart.click()