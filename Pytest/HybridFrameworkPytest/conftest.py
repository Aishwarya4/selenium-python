from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path="E:\Selenium_using_python\chromedriver.exe")
    return driver