from selenium import webdriver

driver = webdriver.Edge(executable_path="E:\Selenium_using_python\chromedriver.exe")
driver.get("https://alison.com/login")
#print(driver.title)

driver.implicitly_wait(10)      #wait for sometime # it is applicable to all the elements in the script and need to declare only once
assert "Login | Alison" in driver.title

driver.find_element_by_name("email").send_keys("aishwaryaparab88@gmail.com")
driver.find_element_by_name("password").send_keys("aishusy09")

driver.find_element_by_class_name("submit-login").click()
#driver.close()