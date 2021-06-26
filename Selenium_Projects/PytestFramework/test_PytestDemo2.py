import pytest

#fixtures is to provide a fixed baseline upon which tests can reliably and repeatedly execute
# @pytest.fixture()
# def setup():
#     print("Once before every method")
# def testmethod1(setup):
#     print("This is test method1")
# def testmethod2(setup):
#     print("This is test method2")

@pytest.yield_fixture()
def setup():
    print("Once before every method")
    yield
    print("Once After every method")

def testmethod1(setup):
    print("This is test method1")
def testmethod2(setup):
    print("This is test method2")