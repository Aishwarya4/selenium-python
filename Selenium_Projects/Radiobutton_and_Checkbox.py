from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="E:\Selenium_using_python\chromedriver.exe")
'''driver.get("https://www.keynotesupport.com/internet/web-contact-form-example-radio-buttons.shtml")
driver.implicitly_wait(10)

#Check whether the radio button is selected or not

radio_status = driver.find_element(By.XPATH, "//input[@value='Beginner']").is_selected()
print("Status before element is not clicked:",radio_status)
time.sleep(5)

driver.find_element(By.XPATH, "//input[@value='Beginner']").click()
print("Radio Button is clicked")
time.sleep(5)

radio_status = driver.find_element(By.XPATH,"//input[@value='Beginner']").is_selected()
print("Status after element is clicked:",radio_status)
time.sleep(5)
'''
#Working with checkboxs
driver.get("https://www.ironspider.ca/forms/checkradio.htm")
driver.find_element_by_xpath("//input[@value='red']").click()
print("Red Checkbox is clicked")

driver.find_element_by_xpath("//input[@value='yellow']").click()
status = driver.find_element_by_xpath("//input[@value='yellow']").is_selected()
print("yellow checkbox selected or not:",status)

status = driver.find_element_by_xpath("//input[@value='purple']").is_selected()
print("Purple checkbox selected or not:",status)

time.sleep(10)
driver.quit()