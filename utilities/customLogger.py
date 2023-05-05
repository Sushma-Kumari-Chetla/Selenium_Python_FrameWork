#Utility file to create logs
#Create customLogger.py under utilities package
#Adding logs to TC
import logging#predefined package in python

class LogGen:
    @staticmethod
    def loggen():
        #logger configuration
        logging.basicConfig(filename="./Logs/automation.log",
                            format='%(asctime)s: %(levelname)s :%(message)s',datefmt='%m%d%Y %I:%M:%S %p',force=True)#Specify where exacly we need to generate the log files - file and and format
        logger=logging.getLogger()#object
        #set log level
        logger.setLevel(logging.INFO)
        return logger
