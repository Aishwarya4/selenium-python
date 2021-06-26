import time
import re
from selenium import webdriver
from selenium.webdriver.support.color import Color
driver = webdriver.Chrome(executable_path="E:\Selenium_using_python\chromedriver.exe")
driver.get("https://colorhunt.co/")

rgb = driver.find_element_by_xpath("//div[3]//div[1]//div[3]").value_of_css_property("background-color")
# r,g,b = map(int, re.search(r'rgb\((\d+),\s*(\d+),\s*(\d+)', rgb).groups())
# color = '#%02x%02x%02x' % (r, g, b)
# print("color",color)
hex = Color.from_string(rgb).hex
atrri = driver.find_element_by_xpath("//div[3]//div[1]//div[3]").get_attribute("style")
print(rgb)
print(atrri)
print(hex)

print(Color.from_string('#00ff33').rgba)
print(Color.from_string('rgb(1, 255, 3)').hex)
print(Color.from_string('blue').rgba)
time.sleep(5)
driver.close()