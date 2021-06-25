from selenium import webdriver
import time
# open chrome browser
driver = webdriver.Chrome(executable_path=r'E:\Selenium_using_python\chromedriver.exe')
# set implicit time to 30 seconds
driver.implicitly_wait(30)
# navigate to the url
driver.get("https://chercher.tech/python/windows-selenium-python")
# get the Session id of the Parent
parentGUID = driver.current_window_handle
# click the button to open new window
driver.find_element_by_id("two-window").click()
time.sleep(5)
# get the All the session id of the browsers
allGUID = driver.window_handles
# print the title of the page
print("Page title before Switching : "+ driver.title)
print("Total Windows : ",len(allGUID))

# iterate the values in the set
for guid in allGUID:
    # one enter into if blobk if the GUID is not equal to parent window's GUID
    if(guid != parentGUID):
        # switch to the guid
        driver.switch_to.window(guid)
        # break the loop
        break

# search on the google page
driver.find_element_by_name("q").send_keys("success")
# print the title after switching
print("Page title after Switching to goolge : "+ driver.title)
time.sleep(5)
# close the browser
driver.close()
# switch back to the parent window
driver.switch_to.window(parentGUID)
# print the title
print("Page title after switching back to Parent: "+ driver.title)
driver.close()