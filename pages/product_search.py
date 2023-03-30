from selenium.webdriver.common.by import By

class ProductSearch:
    #Finding the search text input box and the search button
    PRODUCT_SEARCH_BOX = (By.XPATH, '//*[@id="search_product"]') 
    SEARCH_BUTTON = (By.XPATH, '//*[@id="submit_search"]')

    def __init__(self, driver):
        self.driver = driver
    #Filling the search box with the search specified in the steps file and clicking the search button
    def search(self, query):
        search_box = self.driver.find_element(*self.PRODUCT_SEARCH_BOX)
        search_butt = self.driver.find_element(*self.SEARCH_BUTTON)

        search_box.send_keys(query)
        search_butt.click()