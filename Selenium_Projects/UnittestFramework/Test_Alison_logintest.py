import unittest
from selenium import webdriver
import HtmlTestRunner

class AlisonTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="E:\Selenium_using_python/chromedriver.exe")
        cls.driver.maximize_window()

    def test_homepageTitle(self):
        self.driver.get("https://alison.com/")
        # self.assertEqual("Alison | Free Online Courses & Online Learning",self.driver.title,"webpage title is not matching")
        self.assertEqual("Alison | Login",self.driver.title,"webpage title is not matching")
    def test_login(self):
        self.driver.get("https://alison.com/")
        self.driver.find_element_by_xpath("//span[@class='text']").click()
        self.driver.find_element_by_xpath("//form[@name='login-form']//input[@placeholder='Email address']").send_keys("aishwaryaparab88@gmail.com")
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys("aishusy09")
        self.driver.find_element_by_xpath("//input[@value='Log In']").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test completed....")
if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="E:\Selenium using python\Selenium Projects\Reports"))