import pytest

@pytest.yield_fixture()
def setup():
    print("Opening URL to signup")
    yield
    print("Closing browser after signup")

def test_signupByEmail(setup):
    print("This is signup by email test")
def test_signupByFacebook(setup):
    print("This is signup by facebook")