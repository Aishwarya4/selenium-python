from selenium import webdriver
import pytest

class TestAlison():

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(executable_path="/chromedriver.exe")
        self.driver.maximize_window()
        yield
        self.driver.close()
    def test_homepagetitle(self,setup):
        self.driver.get("https://alison.com/")
        # assert self.driver.title == "Alison | Free Online Courses & Online Learning"
        assert self.driver.title == "Alison"

    def test_login(self,setup):
        self.driver.get("https://alison.com/")
        self.driver.find_element_by_xpath("//span[@class='text']").click()
        self.driver.find_element_by_xpath("//form[@name='login-form']//input[@placeholder='Email address']").send_keys("aishwaryaparab88@gmail.com")
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys("aishusy09")
        self.driver.find_element_by_xpath("//input[@value='Log In']").click()
        assert self.driver.title == "Alison | Free Online Courses & Online Learning"


