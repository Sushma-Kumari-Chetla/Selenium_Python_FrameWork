import time

from utilities.customLogger import LogGen
from utilities.readproperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from pageObjects.add_customer import AddCustomer
from pageObjects.search_customer_page import SearchCustomer


class Test_SearchCustomerByEmail_004:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassWord()
    logger = LogGen.loggen()#logger

    def test_searchCustomerByEmail(self,setup):
        self.logger.info("********** Search Customer By Email_004 **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        #Login to application
        # self.lp = LoginPage(self.driver)
        # self.lp.setUserName(self.username)
        # self.lp.setPassword(self.password)
        # self.lp.clickLogin()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("***** Login Successful *****")
        self.logger.info("***** Searching Customer with Email ID *****")

        #Navigate to Customers from menu
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomersMenuItem()

        #Search Customer using email
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.serchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info("***** Test_SearchCustomerByEmail_004 Finished *****")


