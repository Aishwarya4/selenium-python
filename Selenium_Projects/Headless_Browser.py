from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


import time

browser_name = "chrome"
if browser_name == "chrome":
    option = webdriver.ChromeOptions()
    # option.headless = True #or
    option.add_argument('--headless')
    # option.headless = False
    # option.add_argument('--incognito')
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=option)
    driver.get("https://www.amazon.in/")
    print(driver.title)

elif browser_name == "firefox":
    option = webdriver.FirefoxOptions()
    option.headless = True
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=option)
    driver.get("https://www.amazon.in/")
    print(driver.title)

# elif browser_name == "edge":
#     option = webdriver.Microsoft.Edge.SeleniumTools.EdgeOptions()
#     option.headless =True
#     driver = webdriver.Edge(EdgeChromiumDriverManager().install(),options= option)
#     driver.get("https://www.amazon.in/")
#     print(driver.title)