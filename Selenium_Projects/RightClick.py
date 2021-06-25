from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="E:\Selenium_using_python\chromedriver.exe")
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

RCLK = driver.find_element_by_xpath("//span[@class='context-menu-one btn btn-neutral']")

actions = ActionChains(driver)

actions.context_click(RCLK).perform()
time.sleep(5)
driver.close()
