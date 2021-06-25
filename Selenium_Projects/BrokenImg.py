import requests
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
driver=webdriver.Chrome(chrome_options=options, executable_path=r"E:\Selenium_using_python\chromedriver.exe")
driver.get('http://the-internet.herokuapp.com/broken_images')
links = driver.find_elements_by_css_selector("img")
# for link in links:
#     r = requests.head(link.get_attribute('href'))
#     print(link.get_attribute('href'), r.status_code)



for link in links:

  if (requests.head(link.get_attribute('src')).status_code == 200):
    print("Valid img")
  else:
    print(link.get_attribute('src'),"Broken img")