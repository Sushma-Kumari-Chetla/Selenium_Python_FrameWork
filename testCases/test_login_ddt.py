import time

import pytest
from selenium import webdriver
from utilities.readproperties import ReadConfig
from pageObjects.LoginPage import LoginPage #To Access action methods
from testCases import conftest
from utilities.customLogger import LogGen #To create logd we created customLogger file
from utilities import XLUtils

class Test_002_DDT_Login:

    #call methods from Readconfig class by importing readproperties.py
    baseURL=ReadConfig.getApplicationURL()
    path="./TestData/nopcommerce_Login_testdata.xlsx"

    #calling loggem method from LogGen class of customeLogger package
    logger=LogGen.loggen()

    def test_login_ddt(self,setup):
        self.logger.info("********* Verifying Test_002_DDT_Login *********")
        self.logger.info("********* Verifying test_login_ddt *********")
        # we've defined self.driver twice here in this method and above in the test_homePageTitle method
        # Hence take the duplication to conftest
        # self.driver = webdriver.Chrome()
        self.driver = setup
        self.driver.get(self.baseURL)
        #To access methods in LoginPage create object for LoginPage class "self.lp" below
        #LoginPage has a constructor which is expecting driver, so I pass self.driver
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path,'Sheet1')#no: of rows in xl file and store in self.rows
        print("Number of Rows in an Excel:",self.rows)

        lst_status=[]#Empty List Variable to see if all the exp results are as expected
        #Data Driven test is Pass only when lst_status has all "Pass"

        for r in range(2,self.rows):
            self.user = XLUtils.readData(self.path,'Sheet1',r,1)#1st record
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)  # 1st record
            self.exp = XLUtils.readData(self.path,'Sheet1',r,3)
            # UserName and Password from Xl
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            #login
            self.lp.clickLogin()
            time.sleep(5)

            #Actual and expected titles after login
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            # if actual_tile == "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                #Expectation in Excel
                if self.exp == "Pass":
                    self.logger.info("*** Passed ***")
                    self.lp.clickLogout()
                    #Create a list to see if all the Exp results in the excel are as expected, i.e. this particular list should have all "Pass"
                    lst_status.append("Pass")
                    #Title is matching, But as per my expectation, in Excel File it is not matching (i.e., it is successfully logged in), So it is "Fail" and gets appended to lst)statis
                elif self.exp == "Fail":
                    self.logger.info("*** Failed ***")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            #Title is not Matching means - It should not be logged in
            elif act_title != exp_title:
                #Comparing with the excel data - It is Fail because, User got logged in but Title is not matching
                if self.exp == "Pass":
                    self.logger.info("*** Failed ***")
                    self.lp.clickLogout()
                    #Create a list to see if all the Exp results in the excel are as expected, i.e. this particular list should have all "Pass"
                    lst_status.append("Fail")
                    #Title is matching, But as per my expectation, in Excel File it is not matching (i.e., it is successfully logged in), So it is "Fail" and gets appended to lst_status
                # Comparing with the excel data - It is Pass because, User didn't login and so Title is also not matching
                elif self.exp == "Fail":
                    self.logger.info("*** Passed ***")
                    lst_status.append("Pass")

            # Data Driven test is Pass only when lst_status has all "Pass"
        if "Fail" not in lst_status:
            self.logger.info("*** Login DDT Test is Passed ***")
            self.driver.close()
            assert True
        else:
            self.logger.info("*** Login DDT Test is Failed ***")
            self.driver.close()
            assert False

        #Last Lines in Logs
        self.logger.info("*** END OF LOGIN DDT Test ***")
        self.logger.info("*** Completed Test_002_DDT_Login ***")