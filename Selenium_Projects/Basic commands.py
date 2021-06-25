from selenium import webdriver
import time

#driver= webdriver.Chrome(executable_path="E:\Selenium using python\chromedriver.exe")
#driver= webdriver.Firefox(executable_path="E:\Selenium using python\geckodriver.exe")
driver= webdriver.Edge(executable_path="E:\Selenium_using_python\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")
driver.refresh()
print(driver.title)   #Return title of the page
print(driver.current_url)  #Return the URL of the page
print(driver.page_source)   #Return HTML code for the page

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
time.sleep(5)
driver.close()