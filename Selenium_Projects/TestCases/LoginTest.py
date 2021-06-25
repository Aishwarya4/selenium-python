from selenium import webdriver
import sys
sys.path.append("E:\Selenium_using_python\Selenium_Projects\PageObjects")
from Selenium_Projects.PageObjects.LoginPage import LoginPage
import unittest
import time
import HtmlTestRunner

class LoginTest(unittest.TestCase):
    baseURL = "https://alison.com/"
    username = "aishwaryaparab88@gmail.com"
    password = "aishusy09"
    driver = webdriver.Chrome(executable_path="E:\Selenium_using_python\chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_login(self):
        lp = LoginPage(self.driver)
        lp.click_loginpage()
        # self.driver.find_element_by_xpath("//span[@class='text']").click()
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(5)
        self.assertEqual("Alison | Free Online Courses & Online Learning",self.driver.title,"webpage title is not matching")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="E:\Selenium_using_python\Selenium_Projects\Reports2"))

