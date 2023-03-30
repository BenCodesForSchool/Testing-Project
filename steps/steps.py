from behave import given, when, then
from behave.runner import Context
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
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
    try:
        context.logger.info(f"Starting step: the user navigates to the shopping website")
        start_time = datetime.now()
        context.driver.get("https://automationexercise.com")
        home_page = HomePage(context.driver)
        home_page.go_to_login_page()
        end_time = datetime.now()
        elapsed_time = end_time - start_time
        context.logger.info(f"Completed step: the user navigates to the shopping website in {elapsed_time.total_seconds()} seconds")
    except Exception as e:
        context.logger.error(f"Error occurred in step: the user navigates to the shopping website. Error message: {str(e)}")
        raise


@when("the user logs in with valid credentials")
def step_impl(context):
    try:
        context.logger.info(f"Starting step: the user logs in with valid credentials")
        start_time = datetime.now()
        login_page = LoginPage(context.driver)
        login_page.login("bweiler@qac.com", "password")
        login_page.go_to_products_page()
        end_time = datetime.now()
        elapsed_time = end_time - start_time
        context.logger.info(f"Completed step: the user logs in with valid credentials in {elapsed_time.total_seconds()} seconds")
    except Exception as e:
        context.logger.error(f"Error in step: the user logs in with valid credentials - {str(e)}")
        raise e

@when("searches for a product")
def step_impl(context):
    try:
        context.logger.info(f"Starting step: searches for a product")
        start_time = datetime.now()
        product_search = ProductSearch(context.driver)
        product_search.search("tshirts")
        end_time = datetime.now()
        elapsed_time = end_time - start_time
        context.logger.info(f"Completed step: searches for a product in {elapsed_time.total_seconds()} seconds")
    except Exception as e:
        context.logger.error(f"Error in step: searches for a product - {str(e)}")
        raise e

@when("selects some products to add to the cart")
def step_impl(context):
    try:
        context.logger.info(f"Starting step: selects some products to add to the cart")
        start_time = datetime.now()
        product_selection = ProductSelection(context.driver)
        product_selection.add_products_to_cart(2)
        product_selection.view_cart()
        end_time = datetime.now()
        elapsed_time = end_time - start_time
        context.logger.info(f"Completed step: selects some products to add to the cart in {elapsed_time.total_seconds()} seconds")
    except Exception as e:
        context.logger.error(f"Error in step: selects some products to add to the cart - {str(e)}")
        raise e

@when("deletes one product from the cart")
def step_impl(context):
    try:
        context.logger.info(f"Starting step: deletes one product from the cart")
        start_time = datetime.now()
        in_the_cart_page = InTheCart(context.driver)
        in_the_cart_page.delete_items(1)
        end_time = datetime.now()
        elapsed_time = end_time - start_time
        context.logger.info(f"Completed step: deletes one product from the cart in {elapsed_time.total_seconds()} seconds")
    except Exception as e:
        context.logger.error(f"Error in step: deletes one product from the cart - {str(e)}")
        raise e


@when("proceeds to checkout")
def step_impl(context):
    context.logger.info(f"Starting step: proceeds to checkout")
    start_time = datetime.now()
    in_the_cart_page = InTheCart(context.driver)
    in_the_cart_page.proceed_to_checkout()
    end_time = datetime.now()
    elapsed_time = end_time - start_time
    context.logger.info(f"Completed step: proceeds to checkout in {elapsed_time.total_seconds()} seconds")


@when("confirms address and reviews order")
def step_impl(context):
    context.logger.info(f"Starting step: confirms address and reviews order")
    start_time = datetime.now()
    checkoutpage = CheckoutPage(context.driver)
    checkoutpage.place_order()
    end_time = datetime.now()
    elapsed_time = end_time - start_time
    context.logger.info(f"Completed step: confirms address and reviews order in {elapsed_time.total_seconds()} seconds")

@when("enters payment information")
def step_impl(context):
    context.logger.info(f"Starting step: enters payment information")
    start_time = datetime.now()
    payment = Payment(context.driver)
    payment.input_payment_info("Joseph Mama", "1234567891011121", "123", "03", "2023")
    end_time = datetime.now()
    elapsed_time = end_time - start_time
    context.logger.info(f"Completed step: enters payment information in {elapsed_time.total_seconds()} seconds")
   

@when("confirms the payment")
def step_impl(context):
    context.logger.info(f"Starting step: confirms the payment")
    start_time = datetime.now()
    payment = Payment(context.driver)
    payment.confirm_payment()
    end_time = datetime.now()
    elapsed_time = end_time - start_time
    context.logger.info(f"Completed step: confirms the payment in {elapsed_time.total_seconds()} seconds")
   

@when("downloads the invoice")
def step_impl(context):
    context.logger.info(f"Starting step: downloading the invoice")
    start_time = datetime.now()
    invoicepage = InvoicePage(context.driver)
    invoicepage.download_invoice()
    end_time = datetime.now()
    elapsed_time = end_time - start_time
    context.logger.info(f"Completed step: downloading the invoice in {elapsed_time.total_seconds()} seconds")

@then("the invoice file should be downloaded")
def step_impl(context):
    context.logger.info(f"Starting step: invoice file should be downloaded")
    start_time = datetime.now()
    invoicepage = InvoicePage(context.driver)
    invoicepage.assert_invoice_downloaded()
    end_time = datetime.now()
    elapsed_time = end_time - start_time
    context.logger.info(f"Completed step: invoice file should be downloaded in {elapsed_time.total_seconds()} seconds")
    
