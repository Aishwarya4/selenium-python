from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#driver= webdriver.Chrome(executable_path="E:\Selenium_using_python\chromedriver.exe")
#driver= webdriver.Firefox(executable_path="E:\Selenium_using_python\geckodriver.exe")
#driver= webdriver.Ie(executable_path="E:\Selenium_using_python\IEDriverServer.exe")
driver= webdriver.Edge(executable_path="E:\Selenium_using_python\chromedriver.exe")
driver.get("http://pavantestingtools.blogspot.in/")
print(driver.title)   #Return title of the page

driver.get("http://www.facebook.com")
time.sleep(5)
print(driver.title)
driver.back()

time.sleep(5)
print(driver.title)
driver.forward()

time.sleep(5)
print(driver.title)
driver.close()