# import sys,os
# myPath = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0,myPath+'E:\Selenium_using_python\Pytest\HybridFrameworkPytest\PageObjects')
from LoginPage import LoginPage
from readProperties import ReadConfig
from customlogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()
    def test_homePageTitle(self,setup):
        self.logger.info("******** Test_001_Login ********")
        self.logger.info("******** Verifying Home Page Title ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("******** Home page title test is passed ********")
        else:
            self.driver.save_screenshot("E:\\Selenium_using_python\\Pytest\\HybridFrameworkPytest\\Screenshots\\test_homePageTitle.png")
            self.driver.close()
            self.logger.info("******** Home page title test passed ********")
            assert False

    def test_login(self,setup):
        self.logger.info("******** Verifying Login test ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("******** Login test passed ********")
        else:
            self.driver.save_screenshot("E:\\Selenium_using_python\\Pytest\\HybridFrameworkPytest\\Screenshots\\test_login.png")
            self.driver.close()
            self.logger.info("******** Login test failed ********")
            assert False


