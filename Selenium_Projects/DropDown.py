from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path="E:\Selenium_using_python\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

drp = Select(driver.find_element_by_id("RESULT_RadioButton-9"))

#Select by option
#drp.select_by_visible_text("Morning")

#Select by index
#drp.select_by_index(2)

#Select by value
drp.select_by_value("Radio-2")

#Count the number of option in dropdown
print("Number of dropdown option:",len(drp.options))

#Capture options and print them
all_options =  drp.options
for option in all_options:
    print(option.text)

time.sleep(5)
driver.close()