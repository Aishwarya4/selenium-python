from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="E:\Selenium_using_python\chromedriver.exe")
driver.get("http://testautomationpractice.blogspot.com/")

dclk = driver.find_element_by_xpath("//button[normalize-space()='Copy Text']")

actions = ActionChains(driver)

actions.double_click(dclk).perform()

# driver.get("https://www.tutorialspoint.com/about/about_careers.htm")
# actions.key_down(Keys.CONTROL).send_keys('C').key_up(Keys.CONTROL).perform()
time.sleep(10)
driver.close()