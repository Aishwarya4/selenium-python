from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\Selenium_using_python\chromedriver.exe")
driver.get("https://alison.com/")

#driver.save_screenshot("E:\\test_screenshot\\test.png")

driver.get_screenshot_as_file("E:\\test_screenshot\\test2.png")
