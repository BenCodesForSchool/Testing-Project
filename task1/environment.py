import configparser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
import logging
import os
from datetime import datetime

def before_all(context):
    # Create a Config object
    config = configparser.ConfigParser()
    # Read the configuration values from config.ini
    config.read('config.ini')

    file_handler = logging.FileHandler(filename='test.log')
    file_handler.setLevel(logging.DEBUG)

    # Add the file handler to the logger
    logger = logging.getLogger()
    logger.addHandler(file_handler)

    # Create a ChromeOptions object and set the browser preferences
    options = ChromeOptions()
    for key, value in config['BrowserPreferences'].items():
        options.add_argument(f"--{key}={value}")
    options.add_argument("--no-sandbox")
    options.headless = True
    options.add_argument("--disable-dev-shm-usage")

    # Checking to make sure the chromedriver and chromium paths exist
    assert os.access(config['Chromium']['chromium_path'], os.X_OK), "Chromium binary is not executable"
    assert os.access(config['Chromium']['chromedriver_path'], os.X_OK), "Chromedriver binary is not executable"

    # Create the Chromedriver service
    try:
        service = ChromeService(executable_path=config['Chromium']['chromedriver_path'], log_path='./chromedriver.log')
    except Exception as e:
        print(f"Error starting chromedriver service: {e}")
        raise

    options.binary_location = config['Chromium']['chromium_path']

    try:
        driver = webdriver.Chrome(options=options, service=service)
    except Exception as e:
        print(f"Error starting Chromium driver: {e}")
        raise

    # Set the driver to the context object
    context.driver = driver

    context.logger = logger
    context.logger.addHandler(file_handler)
    # Log service arguments
    logger.info(f"Service arguments: {service.service_args}")

