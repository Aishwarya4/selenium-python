from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

#To download files at specific folder in Chrome
# chromeOptions = webdriver.ChromeOptions()
# chromeOptions.add_experimental_option("prefs",{"download.default_directory" : "E:\Filedownload"})
# driver = webdriver.Chrome(executable_path="E:\Selenium_using_python\chromedriver.exe",options = chromeOptions)

#To download files at specific folder in FireFox
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", 'E:\Filedownload')
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain,application/pdf")#Mime type

driver = webdriver.Firefox(executable_path="E:\Selenium_using_python\chromedriver.exe",firefox_profile=fp)
driver.get("http://demo.automationtesting.in/FileDownload.html")

#Download text file
driver.find_element_by_id("textbox").send_keys("testing text file")
driver.find_element_by_id("createTxt").click()
driver.find_element_by_id("link-to-download").click()

#Download pdf file
driver.find_element_by_id("pdfbox").send_keys("tesing pdf file")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()

time.sleep(10)

driver.close()