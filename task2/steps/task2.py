import time
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

firefox_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'
service = Service(executable_path="D:\C DRIVE STUFF\Downloads\geckodriver-v0.32.2-win32\geckodriver.exe")
options = Options()
#options.set_preference("browser.startup.homepage", "https://www.google.com/")
options.set_preference("browser.cache.disk.enable", False)
options.set_preference("browser.cache.memory.enable", False)
options.set_preference("browser.cache.offline.enable", False)
options.set_preference("network.http.use-cache", False)
options.add_argument("--user-data-dir=D:/Selenium Projects")
#options.add_argument('-headless')
options.binary_location = firefox_path
driver = webdriver.Firefox(service=service, options=options)
wait = WebDriverWait(driver, 10)
driver.install_addon(r"D:/C DRIVE STUFF/Downloads/uBlock0_1.47.4.firefox.signed.xpi", temporary=True)
#driver.get("https://automationexercise.com")

url = ('https://automationexercise.com/api/createAccount')

#CREATING, VERIFYING, UPDATING ADDRESS OF, VERIFYING ADDRESS CHANGE OF, DELETING ONE ACCOUNT

params = {
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


oneAccount = requests.post(url, data=params)

print(oneAccount.content)

email = {
    "email": "JohnnyDiesel@example.com"
}
accountDetails = requests.get("https://automationexercise.com/api/getUserDetailByEmail", params=email)

print("Account details = ")
print( accountDetails.content)

verificationParams = {
    "email": "JohnnyDiesel@example.com",
    "password": "password123"
}

singleVerification = requests.post("https://automationexercise.com/api/verifyLogin", data=verificationParams)

print(singleVerification.content)

updateParams = {
    "email": "JohnnyDiesel@example.com",
    "password": "password123",
    "address1": "1 Sheppard Avenue West",
    "address2": "Unit 1000000000000000"
}

singleAddressUpdate = requests.put("https://automationexercise.com/api/updateAccount", data=updateParams)

print(singleAddressUpdate.content)

accountDetails = requests.get("https://automationexercise.com/api/getUserDetailByEmail", params=email)

print("Account details after update = ")
print(accountDetails.content)

deleteSingle = requests.delete("https://automationexercise.com/api/deleteAccount", data=verificationParams)
print(deleteSingle.content)

#CREATING MULTIPLE ACCOUNTS

with open(r'D:/Testing-Project/steps/users.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    # Loop through each row
    for row in reader:
        # Send a POST request to create the user account
        response = requests.post("https://automationexercise.com/api/createAccount", data=row)

        print("Account creation")
        print(response.content)
        userEmail = {
            "email":email
        }
        accountDetails = requests.get("https://automationexercise.com/api/getUserDetailByEmail", params=userEmail)
        print(accountDetails.content)

with open(r'D:/Testing-Project/steps/users.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    # Loop through each row in the CSV file
    for row in reader:
        # Extract the email and password values
        email = row['email']
        password = row['password']

        # Create the request payload
        verificationParams = {
            "email": email,
            "password": password
        }

        # Send the delete request
        deleteSingle = requests.delete("https://automationexercise.com/api/deleteAccount", data=verificationParams)
        print("deleting")
        print(deleteSingle.content)
        

