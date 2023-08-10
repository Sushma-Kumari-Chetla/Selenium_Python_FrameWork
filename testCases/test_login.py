import pytest
from selenium import webdriver
from utilities.readproperties import ReadConfig
from pageObjects.LoginPage import LoginPage #To Access action methods
from testCases import conftest
from utilities.customLogger import LogGen #To create logd we created customLogger file
import time
class Test_001_Login:
    #Below are common values, we should write those common ones in config.ini file and to read config.ini file we'll create readproperties.py file
    # baseURL = "https://admin-demo.nopcommerce.com/"
    # username = "admin@yourstore.com"
    # password = "admin"
    #call methods from Readconfig class by importing readproperties.py
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUserName()
    password=ReadConfig.getPassWord()

    #calling loggem method from LogGen class of customeLogger package
    logger=LogGen.loggen()

#1st Tc1 - "test_homePageTitle"
    def test_homePageTitle(self,setup):
        self.logger.info("********* TC_001_Login *********")
        self.logger.info("********* Verifying test_homePageTitle *********")
        # we've defined self.driver twice here in this method and below in the test_Login method
        #Hence take the duplication to conftest
        #Create a fixture for this in conftest and assign it in method as "def text_homePageTitle(self,setup)"
        #fixture returns the driver
        #self.driver = webdriver.chrome()#Create Webdriver
        self.driver=setup #Driver is returned - setup in conftest.py to return driver
        self.driver.get(self.baseURL) #Launch Application

        actual_title=self.driver.title #Get Title
        # if actual_title == "Your store. Login1": #For negative scenario
        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("********* PASSED: test_homePageTitle *********")

        else:
            self.driver.save_screenshot("./Screenshots/test_homePageTitle.png")# ".save_screenshot" method to save screenshot; ./Screenshots - Path of screenshot,/test_homePageTitle.png - file name of the screenshot to be stored
            self.driver.close()
            self.logger.error("********* FAILED: test_homePageTitle *********")#I can give error() or info()
            assert False

#1st Tc2 - "test_homePageTitle"
    def test_login(self,setup):
        self.logger.info("********* Verifying test_login *********")
        # we've defined self.driver twice here in this method and above in the test_homePageTitle method
        # Hence take the duplication to conftest
        # self.driver = webdriver.Chrome() #Initiating driver - Cause - browser closed in last step
        self.driver = setup
        self.driver.get(self.baseURL) #Launch browser
        time.sleep(5)
        #To access methods in LoginPage create object for LoginPage class "self.lp" below
        #LoginPage has a constructor which is expecting driver, so I pass self.driver
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        #title of page after login
        actual_tile = self.driver.title
        time.sleep(5)

        # if actual_tile == "Dashboard / nopComerce administration": #For invalid scenario
        if actual_tile == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("********* PASSED: test_login *********")
            self.driver.close()
        else:
            self.driver.save_screenshot("./Screenshots/test_login.png")
            self.logger.error("********* FAILED: test_login *********")
            self.driver.close()
            assert False