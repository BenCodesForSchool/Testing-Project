from behave import given, when, then
from datetime import datetime
from pages.homepage import HomePage
from pages.login_page import LoginPage
#Oops I can't redefine @given in my steps folder
"""@given("the user navigates to the shopping website")
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
        raise"""
#This makes our test case fail. Tyler told me to do this to demonstrate that my program reports correctly. 
@when("the user attempts to log in with invalid credentials")
def step_impl(context):
    try:
        context.logger.info(f"Starting step: the user attempts to log in with invalid credentials")
        start_time = datetime.now()
        login_page = LoginPage(context.driver)
        login_page.login_with_invalid_creds("invalid_email@example.com", "invalid_password")
        end_time = datetime.now()
        elapsed_time = end_time - start_time
        context.logger.infor(f"Completed step: the user attempts to log in with invalid credentials")
    except Exception as e:
        context.logger.error(f"Error in step: the user attempts to log in with invalid credentials")
        raise e
#Oops this isn't reached! But that's okay
@then("the login should fail")
def step_impl(context):
    login_page = LoginPage(context.driver)

    assert login_page.get_current_url() == login_page.LOGIN_PAGE_URL, "Expected to stay on the login page, but was redirected to another page"