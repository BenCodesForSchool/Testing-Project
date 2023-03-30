from behave import given, when, then
from behave.runner import Context
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import FirefoxProfile
import random
from pages.homepage import HomePage
from pages.login_page import LoginPage
from pages.product_search import ProductSearch
from pages.product_selection import ProductSelection
from pages.inthecart import InTheCart
from pages.checkout_page import CheckoutPage
from pages.payment import Payment
from pages.invoice_page import InvoicePage


@given("the user navigates to the shopping website")
def step_impl(context):
    context.driver.get("https://automationexercise.com")
    home_page = HomePage(context.driver)
    home_page.go_to_login_page()

@when("the user logs in with valid credentials")
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.login("bweiler@qac.com", "password")
    login_page.go_to_products_page()

@when("searches for a product")
def step_impl(context):
    product_search = ProductSearch(context.driver)
    product_search.search("tshirts")
    


@when("selects some products to add to the cart")
def step_impl(context):
    product_selection = ProductSelection(context.driver)
    product_selection.add_products_to_cart(2)
    product_selection.view_cart()


@when("deletes one product from the cart")
def step_impl(context):

    in_the_cart_page = InTheCart(context.driver)
    in_the_cart_page.delete_items(1)


@when("proceeds to checkout")
def step_impl(context):
    in_the_cart_page = InTheCart(context.driver)
    in_the_cart_page.proceed_to_checkout()


@when("confirms address and reviews order")
def step_impl(context):
    checkoutpage = CheckoutPage(context.driver)
    checkoutpage.place_order()

@when("enters payment information")
def step_impl(context):
    payment = Payment(context.driver)
    payment.input_payment_info("Joseph Mama", "1234567891011121", "123", "03", "2023")
   

@when("confirms the payment")
def step_impl(context):
    payment = Payment(context.driver)
    payment.confirm_payment()
    
   

@when("downloads the invoice")
def step_impl(context):
    invoicepage = InvoicePage(context.driver)
    invoicepage.download_invoice()

@then("the invoice file should be downloaded")
def step_impl(context):
    invoicepage = InvoicePage(context.driver)
    invoicepage.assert_invoice_downloaded()
    
