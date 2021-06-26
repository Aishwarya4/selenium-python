from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

browser_name = "edge"

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
#     option = webdriver.chromiumOptions()
#     option.use_chromium = True
#     option.add_argument("headless")
#     # option.add_argument("disable-gpu")
#     driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install(),options= option)
#     driver.get("https://www.amazon.in/")
#     print(driver.title)