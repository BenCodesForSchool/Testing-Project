import configparser
from selenium import webdriver

from selenium.webdriver.firefox.service import Service as FirefoxService
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

    # Create a FirefoxOptions object and set the browser preferences
    options = webdriver.FirefoxOptions()
    for key, value in config['BrowserPreferences'].items():
        options.set_preference(key, value)
    options.add_argument("--headless")

    #Checking to make sure the geckodriver and firefox paths exist
    assert os.path.exists(config['Firefox']['geckodriver_path']), "Geckodriver path does not exist"
    assert os.path.exists(config['Firefox']['firefox_path']), "Firefox path does not exist"
    
        # Create the Firefox driver
    try:
        service = FirefoxService(executable_path=config['Firefox']['geckodriver_path'], log_path='./geckodriver.log')
    except Exception as e:
        print(f"Error starting geckodriver service: {e}")
        raise
    print("Got here")
    options.binary_location = config['Firefox']['firefox_path']
    print("And here")

    try:
        driver = webdriver.Firefox(options=options, service=service)
        driver.install_addon(config['Firefox']['addons_path'], temporary=True)
    except Exception as e:
        print(f"Error starting Firefox driver: {e}")
        raise
    print("1")

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