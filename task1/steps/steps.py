from behave import given, when, then
from datetime import datetime
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
    #Using a try except block in order to catch any errors (this occurs at every step)
    try:
        #Logging the beginning of the step
        context.logger.info(f"Starting step: the user navigates to the shopping website")
        #Logging the time that the step begins
        start_time = datetime.now()
        #The link to the website home page
        context.driver.get("https://automationexercise.com")
        #Using code from the homepage page object model class
        home_page = HomePage(context.driver)
        # Clickong on the link to the login page
        home_page.go_to_login_page()
        #Logging the time that the step ends
        end_time = datetime.now()
        #Recording the elapsed time of the step
        elapsed_time = end_time - start_time
        #Log message that displays step completion and elapsed time
        context.logger.info(f"Completed step: the user navigates to the shopping website in {elapsed_time.total_seconds()} seconds")
    except Exception as e:
        #Error log message
        context.logger.error(f"Error occurred in step: the user navigates to the shopping website. Error message: {str(e)}")
        raise


@when("the user logs in with valid credentials")
def step_impl(context):
    try:
        context.logger.info(f"Starting step: the user logs in with valid credentials")
        start_time = datetime.now()
        #An instance of the login_page POM class
        login_page = LoginPage(context.driver)
        #The specified credentials with which to log in; clicking the log in button
        login_page.login("bweiler@qac.com", "password")
        #Clicking the link to the products page
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
        #An instance of the product_search POM class
        product_search = ProductSearch(context.driver)
        #Putting "tshirts" into the search bar, and clicking on the search button
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
        #An instance of the product_selection POM class
        product_selection = ProductSelection(context.driver)
        #Using product_selection methods to randomly select 2 shirts to add to the cart
        product_selection.add_products_to_cart(2)
        #Clicking the view cart link when the specified amount of shirts have been added to the cart
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
        #An instance of the in_the_cart_page POM class
        in_the_cart_page = InTheCart(context.driver)
        #Specifying that one item should be randomly deleted from the cart by the delete_items method
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
    #On the same page file, proceeding to checkout
    in_the_cart_page = InTheCart(context.driver)
    in_the_cart_page.proceed_to_checkout()
    end_time = datetime.now()
    elapsed_time = end_time - start_time
    context.logger.info(f"Completed step: proceeds to checkout in {elapsed_time.total_seconds()} seconds")


@when("confirms address and reviews order")
def step_impl(context):
    context.logger.info(f"Starting step: confirms address and reviews order")
    start_time = datetime.now()
    #This class simply finds the place order button and clicks it
    checkoutpage = CheckoutPage(context.driver)
    checkoutpage.place_order()
    end_time = datetime.now()
    elapsed_time = end_time - start_time
    context.logger.info(f"Completed step: confirms address and reviews order in {elapsed_time.total_seconds()} seconds")

@when("enters payment information")
def step_impl(context):
    context.logger.info(f"Starting step: enters payment information")
    start_time = datetime.now()
    #The Payment POM class
    payment = Payment(context.driver)
    #Specifying valid credit card information (feel free to use this in real life)
    payment.input_payment_info("Joseph Mama", "1234567891011121", "123", "03", "2023")
    end_time = datetime.now()
    elapsed_time = end_time - start_time
    context.logger.info(f"Completed step: enters payment information in {elapsed_time.total_seconds()} seconds")
   

@when("confirms the payment")
def step_impl(context):
    context.logger.info(f"Starting step: confirms the payment")
    start_time = datetime.now()
    #Simply clicking the confirm payment button
    payment = Payment(context.driver)
    payment.confirm_payment()
    end_time = datetime.now()
    elapsed_time = end_time - start_time
    context.logger.info(f"Completed step: confirms the payment in {elapsed_time.total_seconds()} seconds")
   

@when("downloads the invoice")
def step_impl(context):
    context.logger.info(f"Starting step: downloading the invoice")
    start_time = datetime.now()
    #The InvoicePage POM class
    invoicepage = InvoicePage(context.driver)
    #Finding and clicking the button that downloads the invoice
    invoicepage.download_invoice()
    end_time = datetime.now()
    elapsed_time = end_time - start_time
    context.logger.info(f"Completed step: downloading the invoice in {elapsed_time.total_seconds()} seconds")

@then("the invoice file should be downloaded")
def step_impl(context):
    context.logger.info(f"Starting step: invoice file should be downloaded")
    start_time = datetime.now()
    invoicepage = InvoicePage(context.driver)
    #Asserting that the invoice has been downloaded using the corresponding method in the InvoicePage class
    invoicepage.assert_invoice_downloaded()
    end_time = datetime.now()
    elapsed_time = end_time - start_time
    context.logger.info(f"Completed step: invoice file should be downloaded in {elapsed_time.total_seconds()} seconds")
    
