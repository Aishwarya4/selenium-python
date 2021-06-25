from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="E:\Selenium_using_python\chromedriver.exe")
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

driver.switch_to.frame("packageListFrame")  #Using name
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(5)

driver.switch_to.default_content()
driver.switch_to.frame("packageFrame")
driver.find_element_by_xpath("//a[@href='Capabilities.html']").click()
time.sleep(5)

driver.switch_to.default_content()
driver.switch_to.frame("classFrame")
driver.find_element_by_xpath("//div[@class='topNav']//a[normalize-space()='Deprecated']").click()
# print(driver.switch_to.active_element())
time.sleep(5)
driver.close()
