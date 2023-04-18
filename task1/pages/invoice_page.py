import os

from selenium.webdriver.common.by import By


class InvoicePage:
    #Finding the button to download the invoice
    INVOICE_BUTTON = (By.XPATH, "//a[@class='btn btn-default check_out']")
    #Including the logout button so I can run my second test case. Otherwise the program doesn't need to log in for the second test case.
    LOGOUT_BUTTON = (By.XPATH, './/a[@href="/logout"]')
    def __init__(self, driver):
        self.driver = driver
    #Clicking the button that downloads the invoice
    def download_invoice(self):
        invoice_button = self.driver.find_element(*self.INVOICE_BUTTON)
        invoice_button.click()
        #Logging out exclusively for the purpose of running the test case recommended by Tyler
        logout_button = self.driver.find_element(*self.LOGOUT_BUTTON)
        logout_button.click()
    
    def assert_invoice_downloaded(self):
        # Get the current working directory
        current_dir = os.getcwd()
        # Specify the filename to be checked
        filename = "invoice.txt"
        # Join the current directory and filename
        file_path = os.path.join(current_dir, filename)
        #Assert statements that check if the file exists in the path, and if the file is empty
        assert os.path.exists(file_path), f"File {file_path} not found"
        assert os.path.getsize(file_path) > 0, f"File {file_path} is empty"
