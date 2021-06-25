import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="E:\Selenium_using_python\chromedriver.exe")
driver.get("https://www.snapdeal.com/search?keyword=laptop%20battery&santizedKeyword=&catId=&categoryId=0&suggested=true&vertical=&noOfResults=20&searchState=&clickSrc=suggested&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy")
driver.maximize_window()

ele1 = driver.find_element_by_xpath("//a[contains(@class,'left-handle' ) ]")
ele2 = driver.find_element_by_xpath("//a[contains(@class,'right-handle' ) ]")

#Approach1
# ActionChains(driver).drag_and_drop_by_offset(ele1,60,0).perform()
# time.sleep(5)
# ActionChains(driver).drag_and_drop_by_offset(ele2,-50,0).perform()
# time.sleep(5)
#Approach2
# ActionChains(driver).click_and_hold(ele1).pause(1).move_by_offset(50,0).release().perform()
# time.sleep(5)
# ActionChains(driver).click_and_hold(ele2).pause(1).move_by_offset(-50,0).release().perform()
# time.sleep(5)
#Approach3
ActionChains(driver).move_to_element(ele1).pause(1).click_and_hold(ele1).move_by_offset(50,0).release().perform()
time.sleep(5)
ActionChains(driver).move_to_element(ele2).pause(1).click_and_hold(ele2).move_by_offset(-50,0).release().perform()
time.sleep(5)
driver.close()


