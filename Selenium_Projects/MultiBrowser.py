import current as current
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

#to remove deprecation warning import this
# from selenium.webdriver.chrome.service import Service

#to remove deprecation warning
# s = Service("E:\Selenium_using_python\chromedriver.exe")
# driver= webdriver.Chrome(service=s)

#driver= webdriver.Chrome(executable_path="E:\Selenium_using_python\chromedriver.exe")
# driver= webdriver.Firefox(executable_path="E:\Selenium_using_python\geckodriver.exe")
driver= webdriver.Edge(executable_path="E:\Selenium_using_python\msedgedriver.exe")
# driver.get("http://www.facebook.com")
driver.refresh()
# print(driver.title)   #Return title of the page
# print(driver.current_url)  #Return the URL of the page
# print(driver.page_source)   #Return HTML code for the page
# print(driver.get_window_size(current)) #get height and width
# print(driver.get_window_position(current)) #get x,y position
# print(driver.get_window_rect())   #get x,y cord and height and width
# print(driver.current_window_handle) #returns handle of current window
# print(driver.fullscreen_window())
# print(driver.get_log())

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")
# get element
element = driver.find_element_by_link_text("Courses")
# get id of element
id = element._id
# create another element
element_clone = driver.create_web_element(id)
driver.close()