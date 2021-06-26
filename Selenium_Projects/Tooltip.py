import time

from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome(executable_path="E:\Selenium_using_python\chromedriver.exe")
driver.get("https://demoqa.com/tool-tips/")
action = ActionChains(driver)
tooltip = driver.find_element_by_xpath("//button[normalize-space()='Hover me to see']")
action.move_to_element(tooltip).perform()
time.sleep(5)
tooltiptext = driver.find_element_by_xpath("//div[text()='You hovered over the Button']").text
print(tooltiptext)
time.sleep(5)
driver.close()