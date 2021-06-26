from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="E:\Selenium_using_python\chromedriver.exe")

driver.implicitly_wait(5)
driver.get("https://www.abhibus.com/")

driver.find_element(By.XPATH, "//*[@id='source']").send_keys("ben")
listElements = driver.find_elements(By.XPATH, "//ul[@id='ui-id-1']/li")

print("Total no of suggestions:", len(listElements))

for ele in listElements:
    print("Suggestion is:", ele.text)
    if ele.text == "Benipatti":
        print("Record Found", ele.text)
        ele.click()
        break

time.sleep(5)
driver.close()
