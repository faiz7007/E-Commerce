from selenium import webdriver
import pytest

@pytest.fixture
def setup(browser):
    if browser == "chrome": 
        driver=webdriver.Chrome()
        print("launching chrome browser")
    elif browser == "firefox":
        driver=webdriver.Firefox() 
        print("launching firefox browser")  
    else:
        driver=webdriver.Ie()      # it becomes the default browser
    return driver



def pytest_addoption(parser):   # This will get the value from Commond line like name of browser
    parser.addoption("--browser")


@pytest.fixture()
def browser (request): # This will return the Browser value to setup method
    return request.config.getoption("--browser")


############### pytest HTML report ##################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Faiz'

# It is hook for delete Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop ("JAVA_HOME", None) 
    metadata.pop ("Plugins", None)   