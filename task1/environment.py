import configparser
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import logging
import os
from datetime import datetime
def before_all(context):


    file_handler = logging.FileHandler(filename='..\\task1\\test.log')
    file_handler.setLevel(logging.DEBUG)

    # Add the file handler to the logger
    logger = logging.getLogger()
    logger.addHandler(file_handler)

    # Create a FirefoxOptions object and set the browser preferences
    options = webdriver.FirefoxOptions()
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("browser.download.dir", "/path/to/download/folder")
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream,application/pdf")

    #Checking to make sure the geckodriver path exists
    assert os.path.exists('../drivers/geckodriver'), "Geckodriver path does not exist"
    service = Service(executable_path='/path/to/geckodriver')

    # Create the Firefox driver and install the addon
    driver = webdriver.Firefox(service=service, options=options)
    driver.install_addon('../uBlock0_1.47.4.firefox.signed.xpi', temporary=True)

    # Set the driver to the context object
    context.driver = driver

    context.logger = logging.getLogger()
    context.logger.addHandler(file_handler)



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