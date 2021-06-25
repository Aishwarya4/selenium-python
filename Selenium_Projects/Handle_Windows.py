from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="E:\Selenium_using_python\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element_by_xpath("//a[@href='http://www.selenium.dev']//button[@class='btn btn-info'][normalize-space()='click']").click()

print("Current Handle of window:",driver.current_window_handle)

handles = driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    time.sleep(5)
    if driver.title == "Frames & windows":
        driver.close()       #close only parent window
driver.quit()