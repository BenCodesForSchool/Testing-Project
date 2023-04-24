from behave import given, when, then
from datetime import datetime
from pages.homepage import HomePage
from pages.login_page import LoginPage
#This makes our test case fail. Tyler told me to do this to demonstrate that my program reports correctly. 
@when("the user attempts to log in with invalid credentials")
def step_impl(context):
    
    context.logger.info("Starting step: the user attempts to log in with invalid credentials")
    start_time = datetime.now()
    login_page = LoginPage(context.driver)
    login_page.login("invalid_email@example.com", "invalid_password")
    end_time = datetime.now()
    elapsed_time = end_time - start_time
    assert context.driver.current_url != login_page.LOGIN_PAGE_URL, "Expected to be redirected to the home page, but am stuck on the Login page"
    context.logger.info(f"Completed step: the user attempts to log in with invalid credentials in {elapsed_time.total_seconds()} seconds")
    
#Oops this isn't reached! But that's okay
@then("the login should fail")
def step_impl(context):
    login_page = LoginPage(context.driver)

    assert context.driver.current_url == login_page.LOGIN_PAGE_URL, "Expected to stay on the login page, but was redirected to another page"