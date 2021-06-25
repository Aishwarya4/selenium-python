from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="E:\Selenium_using_python\chromedriver.exe")
driver.get("http://testautomationpractice.blogspot.com/")

driver.find_element_by_xpath("//button[normalize-space()='Click Me']").click()
time.sleep(5)
popup = driver.switch_to.alert
msg = popup.text
print("Alert message is:",msg)
# driver.switch_to.alert.accept()
driver.switch_to.alert.dismiss()

time.sleep(5)
driver.close()
