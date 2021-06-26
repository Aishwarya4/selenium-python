from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="E:\Selenium_using_python\chromedriver.exe")
driver.get("https://www.w3schools.com/html/html_tables.asp")

rows = len(driver.find_elements_by_xpath("/html[1]/body[1]/div[7]/div[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr"))
print("Number of rows present in table:",rows)
cols = len(driver.find_elements_by_xpath("/html[1]/body[1]/div[7]/div[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[1]/th"))
print("Number of column in table:",cols)

print("Company"+"                            "+"Contact"+"       "+"Country")

for r in range(2, rows+1):
    for c in range(1, cols+1):
        values = driver.find_element_by_xpath("/html[1]/body[1]/div[7]/div[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr["+str(r)+"]/td["+str(c)+"]").text
        print(values,end='                  ')
    print()
driver.close()