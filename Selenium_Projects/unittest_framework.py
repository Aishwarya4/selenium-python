import unittest
from selenium import webdriver
# class Test(unittest.TestCase):
#     def test_FirstTest(self):
#         print("This is my first unit test case")
# if __name__=="__main__":
#     unittest.main()

class SearchEnginesTest(unittest.TestCase):
    def test_Google(self):
        self.driver = webdriver.Chrome(executable_path="E:\Selenium_using_python\chromedriver.exe")
        self.driver.get("https://www.google.co.in/")
        print("Title of the page:" + self.driver.title)
        self.driver.close()
    def test_Bing(self):
        self.driver = webdriver.Chrome(executable_path="E:\Selenium_using_python\chromedriver.exe")
        self.driver.get("https://www.bing.com/")
        print("Title of the page:"+self.driver.title)
        self.driver.close()
    def test_DuckDuckGo(self):
        self.driver = webdriver.Chrome(executable_path="E:\Selenium_using_python\chromedriver.exe")
        self.driver.get("https://duckduckgo.com/")
        print("Title of the page:" + self.driver.title)
        self.driver.close()


if __name__=="__main__":
    unittest.main()



