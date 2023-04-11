import configparser
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import logging
import os
from datetime import datetime
def before_all(context):


    # Create a Config object
    config = configparser.ConfigParser()
    
    # Read the configuration values from config.ini
    config.read('config.ini')


    file_handler = logging.FileHandler(filename='D:\\Testing-Project\\task1\\test.log')
    file_handler.setLevel(logging.DEBUG)
    
    # Add the file handler to the logger
    logger = logging.getLogger()
    logger.addHandler(file_handler)

    # Create a FirefoxOptions object and set the browser preferences
    options = webdriver.FirefoxOptions()
    for key, value in config['BrowserPreferences'].items():
        options.set_preference(key, value)

    #Checking to make sure the geckodriver and firefox paths exist
    assert os.path.exists(config['Firefox']['geckodriver_path']), "Geckodriver path does not exist"
    service = Service(executable_path=config['Firefox']['geckodriver_path'])

    assert os.path.exists(config['Firefox']['firefox_path']), "Firefox path does not exist"
    options.binary_location = config['Firefox']['firefox_path']
    


    # Create the Firefox driver and install the addon
    print("Got here")
    driver = webdriver.Firefox(service=service, options=options)
    print("abd ghere")
    driver.install_addon(config['Firefox']['addons_path'], temporary=True)

    # Set the driver to the context object
    context.driver = driver
    
    context.logger = logging.getLogger()
    context.logger.addHandler(file_handler)

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
