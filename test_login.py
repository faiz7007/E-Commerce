
import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage  
from Utilities.readProperties import ReadConfig 
from Utilities.customLogger import LogGen 

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger=LogGen.loggen()

    def test_homepage_title(self,setup):
        self.logger.info("*********** Test_001_Login *********** ")
        self.logger.info("*********** Verifying Home Page Title ***********")
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*********** Home Page Title Test Case Is Passed ***********")
        else:
            self.driver.save_screenshot(".//Screenshots//"+"test_homepage_title.png") #.// represents current project directory
            self.driver.close()
            self.logger.error("*********** Home Page Title Test Case Is Failed ***********")
            assert False


    def test_login(self,setup):
        self.logger.info("*********** Verifying Login Test *********** ")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver) 
        self.lp.SetUserName(self.username)
        self.lp.SetPassword(self.password) 
        self.lp.ClickLogin()
        act_title=self.driver.title 
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*********** Login Test Case Is Passed ***********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".//Screenshots//"+"test_login.png")
            self.driver.close()
            self.logger.error("*********** Login Test Case Is Failed ***********")
            assert False                 