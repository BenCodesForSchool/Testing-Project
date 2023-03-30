import os

from selenium.webdriver.common.by import By


class InvoicePage:
    INVOICE_BUTTON = (By.XPATH, "//div[@class='row']//a[@class='btn btn-default check_out']")

    def __init__(self, driver):
        self.driver = driver
    
    def download_invoice(self):
        invoice_button = self.driver.find_element(*self.INVOICE_BUTTON)
        invoice_button.click()
    
    def assert_invoice_downloaded(self):
        # replace 'invoice.txt' with the name of the downloaded file
        file_path = os.path.join("D:\\", "C DRIVE STUFF", "Downloads", "invoice.txt")
        
        assert os.path.exists(file_path), f"File {file_path} not found"
        assert os.path.getsize(file_path) > 0, f"File {file_path} is empty"
