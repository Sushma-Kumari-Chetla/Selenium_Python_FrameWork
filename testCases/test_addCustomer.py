from pageObjects.LoginPage import LoginPage
from pageObjects.add_customer import AddCustomer
#We get common URLs from config file
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
import random
import string
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassWord()
    logger = LogGen.loggen()

    def test_addCustomer(self,setup):

        self.logger.info("**********Test 003 AddCustomers **********")
        self.driver = setup#conftest.py methods will start execution - browser
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        #login page class object - as to add customers we whould 1st login
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********** Login Successful **********")
        self.logger.info("********** Starting Add Customer Test **********")
        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomersMenuItem()
        self.addcust.clickOnAddNew()
        self.logger.info("********** Providing Customer Info **********")
        #user_defined random_generator function below:
        self.email = random_generator()+"@gmail.com"
        print(self.email)
        self.addcust.enterEmail(self.email)
        self.logger.info("********** Email entered **********")
        self.addcust.enterPassword('text123')
        self.logger.info("********** Password entered **********")
        self.addcust.enterFirstName('ShowOff')
        self.logger.info("********** FirstName entered **********")
        self.addcust.enterLastName('Automation')
        self.logger.info("********** Last Name entered **********")
        self.addcust.setGender('Female')
        self.logger.info("********** Gender Selected **********")
        self.addcust.setDOB('06/17/1994')
        self.logger.info("********** DOB entered **********")
        self.addcust.enterCompanyname('SomeCompany')
        self.logger.info("********** Company entered **********")
        self.addcust.checkTaxExempt('Yes')
        self.logger.info("********** Checked In Tax Exempt **********")
        # self.addcust.selectNewsletter('Test Store 2')
        # self.logger.info("********** Newsletter selected **********")
        self.addcust.setCustomerRoles('Guests')
        self.addcust.setCustomerRoles('Administrators')
        self.logger.info("********** Customer roles selected **********")
        self.addcust.ManagerOfVendor('Vendor 1')
        self.logger.info("********** Vendors selected **********")
        self.addcust.Active_chkbox('Uncheck')
        self.logger.info("********** Check/Uncheck Active **********")
        self.addcust.setAdminComment('Adding Comments')
        self.logger.info("********** Comments entered **********")
        self.addcust.clickOnSave()
        time.sleep(5)
        self.logger.info("********** Clicked on save **********")

        self.logger.info("********** Saving Customer Info **********")
        # self.msg = self.driver.find_element(By.CLASS_NAME,"alert alert-success alert-dismissable")
        self.msg = self.driver.find_element(By.TAG_NAME,"body").text
        print(self.msg)
        time.sleep(5)
        if "The new customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("********** Add Customer Test Passed **********")
        else:
            self.driver.save_screenshot("./Screenshots/add_Customer_Scr.png")
            self.logger.info("********** Add Customer Test Failed **********")
            assert True == False

        # self.driver.close()
        self.logger.info("********** Ending Add Customer Test **********")

def random_generator(size=8,chars=string.ascii_lowercase+string.digits):#generates 8 characters with letters and digits
    x = ''.join(random.choice(chars) for x in range(size))#everytiome new character string
    print(x)
    return x