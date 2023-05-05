#utility file which reads common data from .ini file
import configparser#package
config = configparser.RawConfigParser()#RawConfigParser - class - has methods to read data from config file
#we created an object called config for configparser.RawConfigParser()
#loading file
config.read('./Configurations/config.ini')#use read method to read config.ini file, specify location of config.ini
#Get Values
class ReadConfig:#ReadConfig() - brackets are optional
    #create static methods
    #For every variable create 1 method in the class
    @staticmethod#I can directly access this method with class without creating an object
    def getApplicationURL():
        url = config.get('common info','baseURL')
        return url

    @staticmethod  # I can directly access this method with class without creating an object
    def getUserName():
        username = config.get('common info', 'useremail')
        return username

    @staticmethod  # I can directly access this method with class without creating an object
    def getPassWord():
        password = config.get('common info', 'password')
        return password

# In TC we should call these 3 methods

