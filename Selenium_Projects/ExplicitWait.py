from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import time
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support.wait import WebDriverWait

driver= webdriver.Chrome(executable_path="E:\Selenium_using_python\chromedriver.exe")
#driver = webdriver.Edge(executable_path="E:\Selenium_using_python\msedgedriver.exe")
driver.implicitly_wait(5)           #waits for 5 sec
#driver.maximize_window()           #maximize the window

#driver.get("https://www.booking.com/")
driver.get("https://www.expedia.co.in/")
driver.find_element_by_xpath("//*[@id='uitk-tabs-button-container']/li[2]/a").click()

#Explicit wait
wait = WebDriverWait(driver,20)
source = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='location-field-leg1-origin-menu']/div[1]/button")))
source.send_keys("Mumbai (BOM - Chhatrapati Shivaji Intl.)")
time.sleep(3)
destination = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='location-field-leg1-destination-menu']/div[1]/button")))
destination.send_keys("Pune (PNQ - Lohegaon)")

'''deparature_date = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='d1-btn']")))
deparature_date.send_keys("2021-05-10")

return_date = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='d2-btn']")))
return_date.send_keys("2021-05-11")'''

search_btn = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='wizard-flight-pwa-1']/div[3]/div[2]/button")))
#search_btn = driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='wizard-flight-pwa-1']/div[3]/div[2]/button"))))

search_btn.click()


'''try:
  # Tries to click an element
  driver.find_element_by_css_selector("button selector").click()
except ElementClickInterceptedException:
  # If pop-up overlay appears, click the X button to close
  time.sleep(2) # Sometimes the pop-up takes time to load
  driver.find_element_by_css_selector("close button selector").click()'''


time.sleep(10)
driver.close()