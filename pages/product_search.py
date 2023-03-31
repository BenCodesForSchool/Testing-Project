from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductSearch:
    #Finding the search text input box and the search button
    PRODUCT_SEARCH_BOX = (By.XPATH, '//*[@id="search_product"]') 
    SEARCH_BUTTON = (By.XPATH, '//*[@id="submit_search"]')

    def __init__(self, driver):
        self.driver = driver
    #Filling the search box with the search specified in the steps file and clicking the search button
    def search(self, query):
        wait = WebDriverWait(self.driver, 10)
        search_box = wait.until(EC.visibility_of_element_located(self.PRODUCT_SEARCH_BOX))
        search_butt = self.driver.find_element(*self.SEARCH_BUTTON)

        search_box.send_keys(query)
        search_butt.click()
        if "https://automationexercise.com/#google_vignette" in self.driver.current_url:
            self.driver.back()
            search_butt.click()
        