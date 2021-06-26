import unittest
from selenium import webdriver

class Assert_Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path="/chromedriver.exe")
        # driver.get("https://www.google.com/")
        # title = driver.title

        # self.assertEqual("Google12",title,"Webpage title is not equal")
        # self.assertNotEqual("Google",title,"Webpage title is equal")
        # self.assertTrue(title =="Google")
        # self.assertFalse(title == "Google")
        # driver = None
        # self.assertIsNone(driver)
        # self.assertIsNotNone(driver)

        list1 = ["Python","Ruby","Java","C#"]
        # self.assertIn("Python",list1)  #passed
        # self.assertIn("Javascript", list1)  # failed

        # self.assertNotIn("Python",list1) #failed
        # self.assertNotIn("Javascript",list1)  #passed

        # self.assertGreater(100,10) #pass
        # self.assertGreater(10,145) #fail
        # self.assertGreaterEqual(100,100) #pass
        # self.assertGreaterEqual(100,10) #pass
        # self.assertGreaterEqual(10,100) #fail
        # self.assertLess(10,19)#pass
        # self.assertLess(100,78)#fail
        # self.assertLessEqual(10,90)#pass
        # self.assertLessEqual(10,10)#pass
        
if __name__=="__main__":
    unittest.main()
