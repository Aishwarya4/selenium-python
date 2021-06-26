from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver= webdriver.Chrome(executable_path="E:\Selenium_using_python\chromedriver.exe")

driver.implicitly_wait(10)
driver.get("https://www.booking.com/")
driver.find_element_by_xpath("//*[@id='b2indexPage']/header/nav[2]/ul/li[2]/a").click()

#Explicit Wait

#wait = WebDriverWait(driver, 10)
#from_ele = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-select-2--value']/div[2]/input")))

#Fluent Wait
# Fluent_wait = WebDriverWait(driver, 10,2,ignored_exceptions=[ElementClickInterceptedException])
#from_ele = Fluent_wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-select-2--value']/div[2]/input")))

driver.find_element(By.XPATH, "//*[@id='react-select-2--value']/div[2]/input").click()
time.sleep(2)
driver.find_element(By.XPATH, "(//input[@role='combobox'])[1]").send_keys("Mumbai")
time.sleep(2)
driver.find_element(By.XPATH, "(//input[@role='combobox'])[1]").send_keys(Keys.ARROW_DOWN)
time.sleep(2)
driver.find_element(By.XPATH, "(//input[@role='combobox'])[1]").send_keys(Keys.ENTER)

#to_ele = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-select-3--value']/div[2]/input")))
driver.find_element(By.XPATH, "//*[@id='react-select-3--value']/div[2]/input")
time.sleep(2)
driver.find_element(By.XPATH, "(//input[@role='combobox'])[2]").send_keys("Pune")
time.sleep(2)
driver.find_element(By.XPATH, "(//input[@role='combobox'])[2]").send_keys(Keys.ARROW_DOWN)
time.sleep(2)
driver.find_element(By.XPATH, "(//input[@role='combobox'])[2]").send_keys(Keys.ENTER)

#driver.find_element_by_id("airSubmitButtonId").click()
time.sleep(5)
driver.close()