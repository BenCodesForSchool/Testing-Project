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
        #Using code from the homepage page object model class
        home_page = HomePage(context.driver)
        #Navigating to the homepage
        home_page.navigate()
        # Clicking on the link to the login page
        home_page.go_to_login_page()
    except Exception as e:
        #Error log message
        context.logger.error(f"Error occurred in step: the user navigates to the shopping website. Error message: {str(e)}")
        raise


@when("the user logs in with valid credentials")
def step_impl(context):
    try:
        #An instance of the login_page POM class
        login_page = LoginPage(context.driver)
        #The specified credentials with which to log in; clicking the log in button
        login_page.login("bweiler@qac.com", "password")
        #Clicking the link to the products page
        login_page.go_to_products_page()
    except Exception as e:
        context.logger.error(f"Error in step: the user logs in with valid credentials - {str(e)}")
        raise e

@when("searches for a product")
def step_impl(context):
    try:
        #An instance of the product_search POM class
        product_search = ProductSearch(context.driver)
        #Putting "tshirts" into the search bar, and clicking on the search button
        product_search.search("tshirts")
    except Exception as e:
        context.logger.error(f"Error in step: searches for a product - {str(e)}")
        raise e

@when("selects some products to add to the cart")
def step_impl(context):
    try:
        #An instance of the product_selection POM class
        product_selection = ProductSelection(context.driver)
        #Using product_selection methods to randomly select 2 shirts to add to the cart
        product_selection.add_products_to_cart(2)
        #Clicking the view cart link when the specified amount of shirts have been added to the cart
        product_selection.view_cart()
    except Exception as e:
        context.logger.error(f"Error in step: selects some products to add to the cart - {str(e)}")
        raise e

@when("deletes one product from the cart")
def step_impl(context):
    try:
        #An instance of the in_the_cart_page POM class
        in_the_cart_page = InTheCart(context.driver)
        #Specifying that one item should be randomly deleted from the cart by the delete_items method
        in_the_cart_page.delete_items(1)
    except Exception as e:
        context.logger.error(f"Error in step: deletes one product from the cart - {str(e)}")
        raise e


@when("proceeds to checkout")
def step_impl(context):
    try:
        #On the same page file, proceeding to checkout
        in_the_cart_page = InTheCart(context.driver)
        in_the_cart_page.proceed_to_checkout()
    except Exception as e:
        context.logger.error(f"Error in step: 'proceeds to checkout' - {str(e)}")
        raise e


@when("confirms address and reviews order")
def step_impl(context):
    try:
        #This class simply finds the place order button and clicks it
        checkoutpage = CheckoutPage(context.driver)
        checkoutpage.place_order()
    except Exception as e:
        context.logger.error(f"Error in step: 'confirms address and reviews order' - {str(e)}")
        raise e

@when("enters payment information")
def step_impl(context):
    try:
        #The Payment POM class
        payment = Payment(context.driver)
        #Specifying valid credit card information (feel free to use this in real life)
        payment.input_payment_info("Joseph Mama", "1234567891011121", "123", "03", "2023")
    except Exception as e:
        context.logger.error(f"Error in step: 'enters payment information' - {str(e)}")
        raise e
   

@when("confirms the payment")
def step_impl(context):
    try:
        #Simply clicking the confirm payment button
        payment = Payment(context.driver)
        payment.confirm_payment()
    except Exception as e:
        context.logger.error(f"Error in step: 'confirms the payment' - {str(e)}")
        raise e
   

@when("downloads the invoice")
def step_impl(context):
    try:
        #The InvoicePage POM class
        invoicepage = InvoicePage(context.driver)
        #Finding and clicking the button that downloads the invoice
        invoicepage.download_invoice()
    except Exception as e:
        context.logger.error(f"Error in step: 'downloads the invoice' - {str(e)}")
        raise e 

@then("the invoice file should be downloaded")
def step_impl(context):

    try:
        invoicepage = InvoicePage(context.driver)
        #Asserting that the invoice has been downloaded using the corresponding method in the InvoicePage class
        invoicepage.assert_invoice_downloaded()
    except Exception as e:
        context.logger.error(f"Error in step: 'the invoice file should be downloaded' - {str(e)}")
        raise e
    
