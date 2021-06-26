import unittest

class SkippingTests(unittest.TestCase):
    @unittest.SkipTest # SkipTest decorator will skip the test
    def test_search(self):
        print("This is search test")

    @unittest.skip("skipping this test method bcoz it is not yet ready") #will skip method and print reason
    def test_advancedsearch(self):
        print("This is Advanced search test")

    @unittest.skipIf(1==1,"Numbers are equals") #will skip method if condition get true
    def test_prepaidRecharge(self):
        print("This is prepaid recharge test")

    @unittest.skipUnless(1!=1,"Numbers are not equals") #will skip method condition get fail
    def test_postpaidRecharge(self):
        print("This is postpaid recharge test")

    def test_loginbygoogle(self):
        print("This login by google")
if __name__=="__main__":
    unittest.main()