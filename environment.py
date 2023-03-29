import configparser
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
def before_all(context):
    # Create a Config object
    config = configparser.ConfigParser()
    
    # Read the configuration values from config.ini
    config.read('config.ini')

    # Create a FirefoxOptions object and set the browser preferences
    options = webdriver.FirefoxOptions()
    for key, value in config['BrowserPreferences'].items():
        options.set_preference(key, value)

    # Set the Firefox binary and geckodriver paths
    service = Service(executable_path=config['Firefox']['geckodriver_path'])
    options.binary_location = config['Firefox']['firefox_path']

    # Create the Firefox driver and install the addon
    driver = webdriver.Firefox(service=service, options=options)
    driver.install_addon(config['Firefox']['addons_path'], temporary=True)

    # Set the driver to the context object
    context.driver = driver