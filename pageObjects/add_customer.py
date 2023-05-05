import time

from selenium.webdriver.common.by import By

class AddCustomer:
    lnkCustomers_menu_xpath = "//nav[@class='mt-2']//ul[@role='menu']//li[@class='nav-item has-treeview'][3]//a[@href='#']//i[@class='nav-icon far fa-user']"
    lnkCustomers_menuitem_xpath = "//li[@class='nav-item']//a[@href='/Admin/Customer/List']"
    btnAddnew_xpath = "//a[@href='/Admin/Customer/Create']"
    txtEmail_ID = "Email"
    txtPassword_ID = "Password"
    txtFirstName_ID = "FirstName"
    txtLastName_xpath = "//input[@id='LastName']"
    rdbtnGenderMale_ID = "Gender_Male"
    rdbtnGenderFemale_xpath = "//input[@value='F']"
    txtDOB_xpath = "//input[@id='DateOfBirth']"
    txtCompany_id = 'Company'
    chkbxtax_xpath = "//input[@id='IsTaxExempt']"
    selectNewsLetter_ID = "SelectedNewsletterSubscriptionStoreIds_taglist"
    selecttxtNewLetterYourStore_xpath = "//li[text()='Your store name']"
    selecttxtTestStore_xpath = "// li[text() = 'Test store 2']"
    del_defaultCustomerRole_xpath = "//span[@aria-label='delete']"
    lstCustRoles_xpath="//div[@class='form-group row'][10]//div[@class='col-md-9']"
    lstCustRolesAdm_xpath = "//li[text()='Administrators']"
    lstCustRolesFrmMod_xpath = "//li[text()='Forum Moderators']"
    lstCustRolesGst_xpath = "//li[text()='Guests']"
    lstCustRolesRegistered_xpath = "//li[text()='Registered']"
    lstCustRolesRegistereddel_xpath = "//ul[@id='SelectedCustomerRoleIds_taglist']/li[1]/span[2]"
    lstCustRolesVendor_xpath = "//span[text()='Vendors']"
    chkbxActive_id = "Active"
    selectManagerOfVendor_name = "VendorId"
    selectManagerOfVendor_Vendor1_xpath = "//option[text()='Vendor 1']"
    selectManagerOfVendor_Vendor2_xpath = "//option[text()='Vendor 2']"
    selectManagerOfVendor_NotAVendor_xpath = "//option[text()='Not a vendor']"
    txtAdmComment_id = "AdminComment"
    btnSave_xpath = "//button[@name='save']"

    #initialize driver
    def __init__(self,driver):
        self.driver = driver

    #Define Actions
    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH,self.btnAddnew_xpath).click()

    def enterEmail(self,txtEmail_ID):
        self.driver.find_element(By.ID,self.txtEmail_ID).send_keys(txtEmail_ID)

    def enterPassword(self,password):
        self.driver.find_element(By.ID,self.txtPassword_ID).send_keys(password)

    def enterFirstName(self,fname):
        self.driver.find_element(By.ID, self.txtFirstName_ID ).send_keys(fname)

    def enterLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath ).send_keys(lname)

    def setGender(self,gender):
        if gender.upper()=='MALE':
            self.driver.find_element(By.ID,self.rdbtnGenderMale_ID ).click()

        elif gender.upper()=='FEMALE':
            self.driver.find_element(By.XPATH,self.rdbtnGenderFemale_xpath).click()
        else:
            self.driver.find_element(By.ID, self.rdbtnGenderMale_ID).click()

    def setDOB(self,dob):
        self.driver.find_element(By.XPATH,self.txtDOB_xpath).send_keys(dob)

    def enterCompanyname(self,company):
        self.driver.find_element(By.ID,self.txtCompany_id).send_keys(company)

    def checkTaxExempt(self,checkbox):
        if checkbox == 'Yes':
            self.driver.find_element(By.XPATH,self.chkbxtax_xpath).click()

    def selectNewsletter(self,Newsletteropt):
        self.driver.find_element(By.ID,self.selectNewsLetter_ID).click()
        if Newsletteropt == 'Your store name':
            self.driver.find_element(By.XPATH,self.selecttxtNewLetterYourStore_xpath).click()
        elif Newsletteropt == "Test store 2":
            self.driver.find_element(By.XPATH,self.selecttxtTestStore_xpath).click()

        # self.driver.execute_script("arguments[0].click();", self.letteritem)

    def setCustomerRoles(self,role):
        self.driver.find_element(By.XPATH,self.lstCustRoles_xpath).click()
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH,self.lstCustRolesRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstCustRolesAdm_xpath)
        elif role == 'Forum Moderators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstCustRolesFrmMod_xpath)
        elif role == 'Guests':
            time.sleep(3)
            self.driver.find_element(By.XPATH, self.lstCustRolesRegistereddel_xpath).click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstCustRolesGst_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.lstCustRolesVendor_xpath)
        time.sleep(3)
        # self.listitem.click()#If .click() doesnot work (not working for this), use below java script (Execute_script - Pass args and enter the xpath details)
        self.driver.execute_script("arguments[0].click();",self.listitem)

    def ManagerOfVendor(self,manager):
        self.driver.find_element(By.NAME,self.selectManagerOfVendor_name).click()
        if manager=='Vendor1':
            self.driver.find_element(By.XPATH,self.selectManagerOfVendor_Vendor1_xpath).click()
        elif manager == 'Vendor2':
            self.driver.find_element(By.XPATH, self.selectManagerOfVendor_Vendor1_xpath).click()
        elif manager == 'Not a vendor':
            self.driver.find_element(By.XPATH, self.selectManagerOfVendor_NotAVendor_xpath).click()

    def Active_chkbox(self,value):
        if value == 'Uncheck':
            self.driver.find_element(By.ID,self.chkbxActive_id).click()

    def setAdminComment(self,text):
        if len(text)>0:
            self.driver.find_element(By.ID,self.txtAdmComment_id).send_keys(text)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()









