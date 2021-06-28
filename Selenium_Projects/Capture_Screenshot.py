from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\Selenium_using_python\chromedriver.exe")
driver.get("https://alison.com/")

driver.save_screenshot("E:\\Software_Testing\\test_screenshot\\test4.png")
# driver.get_screenshot_as_file("E:\\Software_Testing\\test_screenshot\\test4.png")
driver.close()