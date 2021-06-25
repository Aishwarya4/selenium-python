from Selenium_Projects.Package1.TC_LoginTest import LoginTest
from Selenium_Projects.Package1.TC_SignupTest import SignupTest
from Selenium_Projects.Package2.TC_PaymentTest import PaymentTest
from Selenium_Projects.Package2.TC_PaymentReturnsTest import PaymentReturnsTest
import unittest

#Get all tests from LoginTest, SignUpTest, PaymentTest and paymentReturnsTest

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

#Creating Test Suites
# sanityTestSuite = unittest.TestSuite([tc1,tc2])
# unittest.TextTestRunner().run(sanityTestSuite)
# functionalTestSuite = unittest.TestSuite([tc3,tc4])
# unittest.TextTestRunner().run(functionalTestSuite)
masterTestSuite = unittest.TestSuite([tc1,tc2,tc3,tc4])
unittest.TextTestRunner().run(masterTestSuite)



