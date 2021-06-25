from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="E:\Selenium_using_python\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

#How to count the number of input boxs
count_input = driver.find_elements_by_class_name('text_field')
print(len(count_input))

#How to get the status of the input box
status = driver.find_element_by_class_name("text_field").is_displayed()
print("Displayed or not:",status) #true/false

status = driver.find_element_by_class_name("text_field").is_enabled()
print("Enabled or not:",status)

status = driver.find_element_by_class_name("text_field").is_selected()
print("Selected or not:",status)

#How to enter the values in input box
driver.find_element_by_id("RESULT_TextField-1").send_keys("Aishwarya")
driver.find_element_by_id("RESULT_TextField-2").send_keys("Parab")

time.sleep(10)
driver.close()