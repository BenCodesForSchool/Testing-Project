from selenium.webdriver.common.by import By
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#I created this page in order to handle the fact that the page undergoes a significant change when a search is made. 
class ProductSelection:
    #Finding the buy button for all shirts (or any specified product, really) on the page
    SHIRTS = (By.XPATH, "//div[@class='productinfo text-center']//a[contains(text(), 'Add to cart')]")
    #Finding the button that allows a user to continue shopping after having added an item to the cart
    CONTINUE_SHOPPING_BUTTON = (By.XPATH, "//*[@class='btn btn-success close-modal btn-block']")
    #Finding the button that allows a user to view the cart after having added an item to the cart. Keeping a specific xpath for this because there is 
    #Another view cart button that can be selected with just //a[@href='/view_cart']
    VIEWCART = (By.XPATH, "//div[@class='shop-menu pull-right']//a[@href='/view_cart']")
    #This is an ad that I gave up on trying to get rid of. If you stop using the adblocker, this thing will make your program not work like 4/6 of the time.
    BOTTOM_AD = (By.XPATH, "//div[@class='grippy-host']/g[@class='down']")

    def __init__(self, driver):
        self.driver = driver

    def add_products_to_cart(self, num_products):
        """#clicking away the ad that appears at the bottom so that it doesn't interfere with clicking any of the selected shirts
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class='grippy-host']/g[@class='down']"))):
            bottom_ad = self.driver.find_element(*self.BOTTOM_AD)
            bottom_ad.click()"""
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
            #Clicking on the continue shopping button after each shirt is selected
            continue_shopping = self.driver.find_element(*self.CONTINUE_SHOPPING_BUTTON)
            continue_shopping.click()
    
    def view_cart(self):
        #Clicking the view cart button
        viewcart = self.driver.find_element(*self.VIEWCART)
        viewcart.click()