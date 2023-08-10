import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#this decorator will make this as fixture

@pytest.fixture
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        print("Launching Chrome Browser.......")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path = GeckoDriverManager().install())
        print("Launching Firefox Browser.......")
    elif browser == "edge":
        driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
        print("Launching Edge Browser.......")
    elif browser == "safari":
        driver = webdriver.Safari()
        print("Launching Safari Browser.......")
    else:#Default driver
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        print("Launching Chrome Browser.......")
    return driver #returndriver

# @pytest.fixture
# def setup(browser):
#     path = "./chromedriver"
#     driver = webdriver.Chrome(path)#Only CHrome broswer
#     print("Launching Chrome Driver")
#
#     return driver #returndriver


#Run tests on desired browser/Cross Browser/Parallel
#Different browsers parallely
# Update conftest.py with required fixtures which will accept command line argument (browser name)
# pass browser name as argument in command line
def pytest_addoption(parser):
    parser.addoption("--browser") #will get browser name from command line (CLI)

#once we get browsername pass it to the setup() method, one more pytest fixture, because setup method will decide which browser to launch

@pytest.fixture()
def browser(request): #This will return/send the browser value to set up method
    return request.config.getoption("--browser")
#same value should be recieved in setup method, so, pass this browser into set up  method

###### pytest HTML Report #######

#It is hook for adding environment info to html report
#It is customizable we can add any details we dont want to display
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Sushma Kumari Chetla'

#It is hook for delete/Modify Environment info to HTML Report #It is customizable we can add any details we dont want to display
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins", None)



