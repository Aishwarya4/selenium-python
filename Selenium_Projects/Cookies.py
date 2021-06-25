from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\Selenium_using_python\chromedriver.exe")
driver.get("https://www.amazon.in/")

#capture all the cookies created by browser
cookies = driver.get_cookies()
print("Number of cookies before adding the cookie:",len(cookies))   #print number of cookies have been created
print(cookies)        #print all the cookies pairs

#Adding new cookie to the browser
cookie = {'name': 'MyCookie','value':'1223456670'}
driver.add_cookie(cookie)
cookies = driver.get_cookies()
print("Number of cookies after adding the cookie:",len(cookies))     #print number of cookies after adding cookie
print(cookies)

#Deleting cookie
driver.delete_cookie('MyCookie')
cookies = driver.get_cookies()
print("Number of cookies after deletion:",len(cookies))
print(cookies)

#Deleting all cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print("After deleting all cookies:",len(cookies))