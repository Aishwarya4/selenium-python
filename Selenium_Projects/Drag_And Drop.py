from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="E:\Selenium_using_python\chromedriver.exe")
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

drag_ele = driver.find_element_by_xpath("//div[@id='box6']")
drop_ele = driver.find_element_by_xpath("//div[@id='box106']")

actions = ActionChains(driver)

actions.drag_and_drop(drag_ele,drop_ele).perform()