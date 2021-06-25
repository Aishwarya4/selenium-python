from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver=webdriver.Chrome(executable_path="E:\Selenium using python\chromedriver.exe")
driver=webdriver.Edge(executable_path="E:\Selenium_using_python\chromedriver.exe")
driver.get("https://inorbitcabs.com/")

#Radio Button Status

From_ele=driver.find_element_by_name("osfrom")
print(From_ele.is_displayed())            #returns true/false based on element status
print(From_ele.is_enabled())              #returns true/false

To_ele=driver.find_element_by_name("osto")
print(To_ele.is_displayed())          #returns true/false based on element status
print(To_ele.is_enabled())            #returns true/false


roundtrip_radio=driver.find_element_by_id("radio1")
print("Status of roundtrip radio button", roundtrip_radio.is_selected())

onetrip_radio=driver.find_element_by_id("radio2")
print("Status of onewaytrip radio button", onetrip_radio.is_selected())

driver.get("https://alison.com/login")
user_ele=driver.find_element_by_name("email")
pass_ele=driver.find_element_by_name("password")

user_ele.send_keys("aishwaryaparab88@gmail.com")
pass_ele.send_keys("aishusy09")
driver.find_element_by_class_name("submit-login").click()

driver.close()


