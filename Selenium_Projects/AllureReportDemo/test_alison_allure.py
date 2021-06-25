import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
@allure.severity(allure.severity_level.NORMAL)
class TestAlison:
    @allure.severity(allure.severity_level.MINOR)
    def test_logo(self):
        self.driver = webdriver.Chrome(executable_path="E:\Selenium_using_python\chromedriver.exe")
        self.driver.get("https://alison.com/")
        status = self.driver.find_element_by_xpath("//header[contains(@class,'not-loggedin')]//a[2]//img[1]").is_displayed()

        if status==True:
            assert True
        else:
            assert False
        self.driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    def test_list_course(self):
        pytest.skip("Skipping test...Later execute")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        self.driver = webdriver.Chrome(executable_path="E:\Selenium_using_python\chromedriver.exe")
        self.driver.get("https://alison.com/")
        self.driver.find_element_by_xpath("//span[@class='text']").click()
        self.driver.find_element_by_xpath("//form[@name='login-form']//input[@placeholder='Email address']").send_keys("aishwaryaparab88@gmail.com")
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys("aishusy09")
        self.driver.find_element_by_xpath("//input[@value='Log In']").click()
        acutal_title = self.driver.title

        if acutal_title == "Alison | Free Online Courses & Online Learning12":
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="testloginscreen",attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False
# to run = pytest -v -s --alluredir="E:\Selenium_using_python\Selenium_Projects\AllureReportDemo\reports" test_alison_allure.py
#to generate allure report =E:\Software Testing\allure-2.14.0\bin>allure serve E:\Selenium_using_python\Selenium_Projects\AllureReportDemo\reports