import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import FirefoxProfile
import requests
import csv

@given("the API endpoints for account creation, updating, verification, and deletion")
def step_impl(context):
    context.create_account_url = "https://automationexercise.com/api/createAccount"
    context.verify_account_url = "https://automationexercise.com/api/getUserDetailByEmail"
    context.update_account_url = "https://automationexercise.com/api/updateAccount"
    context.delete_account_url = "https://automationexercise.com/api/deleteAccount"
    context.params = {
        "name": "John Doe",
        "email": "JohnnyDiesel@example.com",
        "password": "password123",
        "title": "Mr",
        "birth_date": "01",
        "birth_month": "01",
        "birth_year": "2000",
        "firstname": "John",
        "lastname": "Doe",
        "company": "Example Company",
        "address1": "123 Main St.",
        "address2": "Apt. 456",
        "country": "USA",
        "zipcode": "12345",
        "state": "CA",
        "city": "Los Angeles",
        "mobile_number": "555-1234"
    }
    context.name = context.params["name"]
    context.email = context.params["email"]
    context.password = context.params["password"]
    context.title = context.params["title"]
    context.birth_date = context.params["birth_date"]
    context.birth_month = context.params["birth_month"]
    context.birth_year = context.params["birth_year"]
    context.firstname = context.params["firstname"]
    context.lastname = context.params["lastname"]
    context.company = context.params["company"]
    context.address1 = context.params["address1"]
    context.address2 = context.params["address2"]
    context.country = context.params["country"]
    context.zipcode = context.params["zipcode"]
    context.state = context.params["state"]
    context.city = context.params["city"]
    context.mobile_number = context.params["mobile_number"]


@when("the user uses the API to create an account")
def step_impl(context):
    
    context.response = requests.post(context.create_account_url, data=context.params)
    



@then("the user should be able to use the API to verify account details")
def step_impl(context):

    accountdetails = requests.get(context.verify_account_url, params=context.email)
    assert accountdetails.status_code == 200
    account_data = accountdetails.json()
    for key  in account_data:
        if hasattr(context, key):
            assert account_data[key] == getattr(context, key)

@when("the user attempts to change the address on the account")
def step_impl(context):
    context.new_address1 = "1 Sheppard Avenue West"
    context.new_address2 = "Unit 1000000000000000"
    updateparams = {
        "email": context.email,
        "password": context.password,
        "address1": context.new_address1,
        "address2": context.new_address2
    }
    context.response = requests.put(context.update_account_url, data=updateparams)


@then("the address should change on the account")
def step_impl(context):
    accountdetails = requests.get(context.verify_account_url, params=context.email)
    assert accountdetails.status_code == 200
    account_details = accountdetails.json()
    for key  in account_details:
        if hasattr(context, key):
            if key == "address1":
                assert account_details[key] == context.new_address1
            elif key == "address2":
                assert account_details[key] == context.new_address2
            else:
                assert account_details[key] == getattr(context, key)

@when("the user attempts to delete the account")
def step_impl(context):
    deletionparams = {
        "email": context.email,
        "password": context.password
    }
    deletesingle = requests.delete(context.delete_account_url, data=deletionparams)
    assert deletesingle.status_code == 200

@then("the account should be deleted")
def step_impl(context):
    findoutifdeleted = requests.get(context.verify_account_url, params={"email": context.email})
    print(findoutifdeleted.content)
    assert findoutifdeleted.content == b'{"responseCode": 404, "message": "Account not found with this email, try another email!"}'

