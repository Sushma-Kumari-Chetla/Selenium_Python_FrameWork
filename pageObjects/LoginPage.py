from selenium import webdriver
from selenium.webdriver.common.by import By
class LoginPage:
    text_box_username_id="Email"
    text_box_password_id = "Password"
    button_login_xpath = "//button[text()='Log in']"
    link_logout_linktext = "Logout"

    #Befor defining Actions we should initialize the drive
    # For that we should create one python construstor (Automatically invoked at the time of object creation)
    def __init__(self,driver):#driver will come from actual test case
        self.driver=driver
        #What this constructor does is it takes driver from TestCase which we'll do later and that driver it will be given to the class level variable - self.driver

    #Action Methods
    def setUserName(self,username):
        self.driver.find_element(By.ID,self.text_box_username_id).clear()
        self.driver.find_element(By.ID,self.text_box_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.text_box_password_id).clear()
        self.driver.find_element(By.ID,self.text_box_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()
