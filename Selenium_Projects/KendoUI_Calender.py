# Selenium testing tutorial to automate calendar using Selenium WebDriver
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

target_year = "2024"
target_month = "February"
target_date = "20"
space = " "

test_url = 'https://demos.telerik.com/kendo-ui/datetimepicker/index'

class CalendarControlTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="E:\Selenium_using_python\chromedriver.exe")
        self.driver.maximize_window()

    def test_calendar_control_range_(self):
        driver = self.driver
        driver.get(test_url)
        time.sleep(5)

        target_month_year_string = target_month + space + target_year

        elem_datepicker = driver.find_element_by_css_selector(".k-icon.k-i-calendar")
        elem_datepicker.click()

        time.sleep(5)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "k-content")))
        elem_table = driver.find_element_by_class_name("k-content")

        # Locators for the Previous and Next Buttons

        elem_previous_button_class_name = "k-nav-prev"
        elem_next_button_class_name = "k-nav-next"

        # Locator for Month and Year Selected label
        elem_month_year_class_name = "k-nav-fast"
        elem_selected_year = driver.find_element_by_class_name(elem_month_year_class_name)

        selected_month_year_string = elem_selected_year.get_attribute("innerHTML")

        while (selected_month_year_string != target_month_year_string):
            next_click = driver.find_element_by_class_name(elem_next_button_class_name)
            next_click.click()
            time.sleep(2)

            elem_selected_year = driver.find_element_by_class_name(elem_month_year_class_name)
            selected_month_year_string = elem_selected_year.get_attribute("innerHTML")
            # print(selected_month_year_string)

        # Added a sleep to check the output
        time.sleep(5)

        for row in elem_table.find_elements_by_xpath("//tr"):
            for cell in row.find_elements_by_xpath("td"):
                if (cell.text == target_date):
                    req_date = driver.find_element_by_link_text(cell.text)
                    req_date.click()
                    break

        time.sleep(5)

        # Since we are here and all the necessary fields are selected, the test has passed.
        print("Unit Test of jQuery Calendar passed")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()