import unittest

def setUpModule(): #will execute before executing any class or any method present in test class
    print("setUpModule")
def tearDownModule(): #will be executed after completing everything present in the python module
    print("tearDownModule")

class WebTesting(unittest.TestCase):
    @classmethod
    def setUpClass(cls): #Execute once When class started
        print("Open Webapplication \n")
    @classmethod
    def tearDownClass(cls): #Execute once after class completed
        print("Close Webapplication")

    @classmethod
    def setUp(self): #This method will execute before every other method
        print("This is login test")
    @classmethod
    def tearDown(self): #This method will execute after every other method
        print("This is logout test")

    def test_search(self):
        print("This is search test")
    def test_advancedsearch(self):
        print("This is Advanced search test")
    def test_prepaidRecharge(self):
        print("This is prepaid recharge test")
    def test_postpaidRecharge(self):
        print("This is postpaid recharge test")
if __name__=="__main__":
    unittest.main()