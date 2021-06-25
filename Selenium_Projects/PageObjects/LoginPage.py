class LoginPage():
    #Locators of all the elements in pages
    textbox_username_xpath = "//form[@name='login-form']//input[@placeholder='Email address']"
    textbox_password_xpath = "//input[@name='password']"
    button_login_xpath = "//input[@value='Log In']"
    button_loginpage_xpath = "//span[@class='text']"
    button_logout_xpath = "//a[contains(text(),'Logout')]"

    def __init__(self,driver):
        self.driver = driver
    def click_loginpage(self):
        self.driver.find_element_by_xpath(self.button_loginpage_xpath).click()
    def setUsername(self,username):
        self.driver.find_element_by_xpath(self.textbox_username_xpath).send_keys(username)
    def setPassword(self,password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)
    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()
    # def clickLogout(self):
    #     self.driver.find_element_by_xpath(self.button_logout_xpath).click()

