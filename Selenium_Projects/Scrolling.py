from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="E:\Selenium_using_python\chromedriver.exe")
driver.get("https://www.nationsonline.org/oneworld/countries_of_the_world.htm")

#Scroll by pixel value
# time.sleep(3)
# driver.execute_script("window.scrollBy(0,3000)","")
# time.sleep(5)

# Scroll down page until element found
# flag = driver.find_element_by_xpath("//a[normalize-space()='Colombia']")
# driver.execute_script("arguments[0].scrollIntoView();",flag)
# time.sleep(10)

#Scroll down till page end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(10)

driver.close()