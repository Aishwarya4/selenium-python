from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="E:\Selenium_using_python\chromedriver.exe")
driver.get("https://www.redbus.in/")

#Print how many links present in the webpage
links = driver.find_elements_by_tag_name("a")

print("Number of links present:",len(links))

#Capture the links and print
for link in links:
    print(link.text)


#Clicking on link
#driver.find_element_by_link_text("BUS HIRE").click()
#print("Bus Hire is clicked")
driver.find_element_by_partial_link_text("HIRE").click()
print("Bus Hire is clicked")
time.sleep(5)

driver.close()