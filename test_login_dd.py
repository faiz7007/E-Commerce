import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import xlutils
from time import sleep

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path=".//TestData/LoginData.xlsx"
    
    logger=LogGen.loggen()

    def test_login_ddt(self,setup):
        self.logger.info("*********** Test_002_DDT_Login *************")
        self.logger.info("*********** Verifying Login Test *********** ")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)

        self.rows=xlutils.getRowCount(self.path,"Sheet1")
        print("No of rows in excel:",self.rows)

        lst_status=[]
        for r in range(2,self.rows+1):
            self.user=xlutils.readData(self.path,"Sheet1",r,1)
            self.password=xlutils.readData(self.path,"Sheet1",r,2)
            self.expected=xlutils.readData(self.path,"Sheet1",r,3)

            self.lp.SetUserName(self.user)
            self.lp.SetPassword(self.password)
            self.lp.ClickLogin()
            sleep(5)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.expected == "Pass":
                    self.logger.info("*******Passed")
                    self.lp.ClickLogout()
                    lst_status.append("Pass")

                elif self.expected == "Fail":
                    self.logger.info("*****Fail")
                    self.lp.ClickLogout()
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.expected == "Pass":
                    self.logger.info("*******Fail")
                    self.lp.ClickLogout()
                    lst_status.append("Fail")

                elif self.expected == "Fail":
                    self.logger.info("*****Pass")
                    self.lp.ClickLogout()
                    lst_status.append("Pass")

            if "Fail" not in lst_status:
                self.logger.info("Login ddt test is pass")
                self.driver.close()
                assert True
            else:
                self.logger.info("Login ddt test is fail")
                self.driver.close()
                assert False    

        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed TC_LoginDDT_02 ************* ")   

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