from selenium.webdriver.common.by import By

class Payment:
    #Finding the text boxes for all relevant credit card information, as well as the button that submits credit card information and confirms the user's payent.
    NAME_ON_CARD = (By.XPATH, "//input[@name='name_on_card']")
    CARD_NUMBER = (By.XPATH, "//input[@name='card_number']")
    CVC = (By.XPATH, "//input[@name='cvc']")
    EXPIRATION_MONTH = (By.XPATH, "//input[@name='expiry_month']")
    EXPIRATION_YEAR = (By.XPATH, "//input[@name='expiry_year']")
    CONFIRM_PAYMENT_BUTTON = (By.XPATH, './/button[@id="submit"]')

    def __init__(self, driver):
        self.driver = driver
    #Sending specified credit card information to the corresponding text boxes
    def input_payment_info(self, nameOnCard, cardNumber, cVc, exMonth, exYear):
        name_on_card = self.driver.find_element(*self.NAME_ON_CARD)
        card_number = self.driver.find_element(*self.CARD_NUMBER)
        cvc = self.driver.find_element(*self.CVC)
        expiration_month = self.driver.find_element(*self.EXPIRATION_MONTH)
        expiration_year = self.driver.find_element(*self.EXPIRATION_YEAR)

        name_on_card.send_keys(nameOnCard)
        card_number.send_keys(cardNumber)
        cvc.send_keys(cVc)
        expiration_month.send_keys(exMonth)
        expiration_year.send_keys(exYear)
    #Clicking the confirm payment button
    def confirm_payment(self):
        confirm_payment = self.driver.find_element(*self.CONFIRM_PAYMENT_BUTTON)
        confirm_payment.click()
        if "https://automationexercise.com/#google_vignette" in self.driver.current_url:
            self.driver.back()
            confirm_payment.click()

    
