from selenium.webdriver.common.by import By
class SearchCustomer:
    #Add Customer Page
    txtEmail_xpath = "//input[@id = 'SearchEmail']"
    txtFirstName_xpath = "//input[@name = 'SearchFirstName']"
    txtLastName_xpath = "//input[@id= 'SearchLastName']"
    slctMonth_xpath = "//select[@id = 'SearchMonthOfBirth']"
    slctspecMonth_xpath = "//select[@id = 'SearchMonthOfBirth']//option"
    # optMonth_xpath = "//select[@name = 'SearchMonthOfBirth']//option[@value='{}']".format(input("Enter Month Number: "))
    slctDay_xpath = "//select[@name = 'SearchDayOfBirth']"
    ipcomp_id = "SearchCompany"
    ipipad_name = "SearchIpAddress"
    slctCustomRole_xpath = "//div[@role = 'listbox']"
    slctCustomRole_Admin_xpath = "//select[@id = 'SelectedCustomerRoleIds']//option[@value = '1']"
    slctCustomRole_ForumMod_xpath = "//select[@id = 'SelectedCustomerRoleIds']//option[@value = '2']"
    slctCustomRole_Guests_xpath = "//select[@id = 'SelectedCustomerRoleIds']//option[text() = 'Guests']"
    slctCustomRole_Registered_xpath = "//select[@id = 'SelectedCustomerRoleIds']//option[contains(text(),'Registered')]"
    btnSearch_id = "search-customers"
    table_grid_xpath = "//div[@id='customers-grid_wrapper']//div[@class='row']"
    table_searchresults_xpath = "//table[@id = 'customers-grid']"
    table_rows_xpath = "//table[@id = 'customers-grid']//tbody//tr"
    table_columns_xpath = "//table[@id = 'customers-grid']//tbody//tr//td"

    def __init__(self,driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setFirstName(self,fn):
        self.driver.find_element(By.XPATH,self.txtFirstName_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fn)

    def setLastName(self,ln):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(ln)

    def setMonthOfDOB(self,mon):
        # self.driver.find_element(By.XPATH,self.slctMonth_xpath)
        # js_commands = "document.getElementByXPATH(self.slctMonth_xpath).value=mon"
        # self.driver.execute_script(js_commands)
        self.driver.find_element(By.XPATH, self.slctspecMonth_xpath).select(mon)

    def clickSearch(self):
        self.driver.find_element(By.ID,self.btnSearch_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH,self.table_rows_xpath))
    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH,self.table_columns_xpath))

    def serchCustomerByEmail(self,email):
        flag = False
        for r in range(1,self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH,self.table_searchresults_xpath)
            emailid = table.find_element(By.XPATH,"//table[@id = 'customers-grid']//tbody//tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag


    def searchCustomerByName(self,Name):
        flag = False
        for r in range(1,self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH, self.table_searchresults_xpath)
            name = table.find_element(By.XPATH,"//table[@id = 'customers-grid']//tbody//tr[" + str(r) + "]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag





















