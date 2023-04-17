import configparser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
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
    options = webdriver.ChromeOptions()
    for key, value in config['BrowserPreferences'].items():
        options.add_argument(f"--{key}={value}")
    options.add_argument("--no-sandbox")
    options.headless = True
    options.add_argument("--disable-dev-shm-usage")

    # Checking to make sure the chromedriver and chrome paths exist
    assert os.access(config['Chrome']['chrome_path'], os.X_OK), "Chrome binary is not executable"
    assert os.access(config['Chrome']['chromedriver_path'], os.X_OK), "Chromedriver binary is not executable"

    # Create the Chrome driver
    try:
        service = ChromeService(executable_path=config['Chrome']['chromedriver_path'], log_path='./chromedriver.log')
    except Exception as e:
        print(f"Error starting chromedriver service: {e}")
        raise

    options.binary_location = config['Chrome']['chrome_path']

    try:
        driver = webdriver.Chrome(options=options, service=service)
    except Exception as e:
        print(f"Error starting Chrome driver: {e}")
        raise

    # Set the driver to the context object
    context.driver = driver

    context.logger = logger
    context.logger.addHandler(file_handler)
    # Log service arguments
    logger.info(f"Service arguments: {service.service_args}")


def before_step(context, step):
    step.start_time = datetime.now()
    context.logger.info(f"Starting step: '{step.name}'")


def after_step(context, step):
    elapsed_time = datetime.now() - step.start_time
    context.logger.info(f"Step '{step.name}' took {elapsed_time.total_seconds()} seconds to execute")


def after_all(context):
    # Get the logger and remove the file handler
    logger = logging.getLogger()
    handlers = logger.handlers[:]
    for handler in handlers:
        handler.close()
        logger.removeHandler(handler)
    # Set up logging statements
    logger.info("Finished running test suite.")
