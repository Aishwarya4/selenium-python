from Selenium_Projects import XLUtils
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="E:\Selenium_using_python\chromedriver.exe")
driver.get("https://alison.com/")
time.sleep(5)
driver.find_element_by_xpath("//a[@class='link login-button']").click()
time.sleep(5)
path = "E:\DataDrivenTest.xlsx"
rows = XLUtils.getRowCount(path,"Sheet1")

for r in range(2,rows+1):
    username = XLUtils.readData(path,"Sheet1",r,1)
    password = XLUtils.readData(path,"Sheet1",r,2)

    driver.find_element_by_xpath("//form[@name='login-form']//input[@placeholder='Email address']").send_keys(username)
    driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
    time.sleep(5)
    driver.find_element_by_xpath("//input[@value='Log In']").click()
    time.sleep(5)

    if driver.current_url =="https://alison.com/dashboard":
        print("Test Passed")
        XLUtils.writeData(path,"Sheet1",r,3,"Test Passed")

        driver.find_element_by_xpath("//a[@class='link sidebar-trigger']//img[@alt='Aishwarya Parab']").click()
        b = driver.find_element_by_xpath("//a[contains(text(),'Logout')]")
        actions = ActionChains(driver)
        time.sleep(5)
        actions.move_to_element(b).click().perform()
        time.sleep(5)
        driver.find_element_by_xpath("//a[@class='link login-button']").click()

    else:
        print("Test Failed")
        XLUtils.writeData(path,"Sheet1",r,3,"Test Failed")
        time.sleep(5)
        driver.find_element_by_xpath("//form[@name='login-form']//input[@placeholder='Email address']").clear()
        driver.find_element_by_xpath("//input[@name='password']").clear()

time.sleep(5)
driver.close()

