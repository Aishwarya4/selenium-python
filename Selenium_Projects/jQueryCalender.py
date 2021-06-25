import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

# jQuery to select multiple dates
target_year = "2021"
target_month = "May"
target_date = "1"
space = " "

expected_month_year_val = '05/01/2021'

test_url = 'http://jqueryui.com/resources/demos/datepicker/other-months.html'

class CalendarControlTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="E:\Selenium_using_python\chromedriver.exe")
        self.driver.maximize_window()

    def test_calendar_control_range_(self):
        driver = self.driver
        driver.get(test_url)
        time.sleep(5)

        datepicker_val = driver.find_element_by_id('datepicker')
        datepicker_val.click()

        target_month_year_string = target_month + space + target_year

        elem_selected_year = driver.find_element_by_class_name("ui-datepicker-year")
        selected_year_string = elem_selected_year.get_attribute("innerHTML")

        elem_selected_month = driver.find_element_by_class_name("ui-datepicker-month")
        selected_month_string = elem_selected_month.get_attribute("innerHTML")

        # Concatenate selected month and year strings
        selected_month_year_string = selected_month_string + selected_year_string

        previous_button_xpath = "//*[@id='ui-datepicker-div']/div/a[1]"
        next_button_xpath = "//*[@id='ui-datepicker-div']/div/a[2]"

        # Navigate through the calendar to go to the required year
        # and than the required month

        while (selected_month_year_string == target_month_year_string):
            if (((int(target_year)) < int(selected_year_string))):
                # Click the next button
                previous_click = driver.find_element_by_xpath(previous_button_xpath)
                previous_click.click()
            else:
                next_click = driver.find_element_by_xpath(next_button_xpath)
                next_click.click()

            # The datepicker-year and datepicker-month elements are located using class name locator.
            # As these are label controls, the text content of these elements are read using innerHTML property.

            elem_selected_year = driver.find_element_by_class_name("ui-datepicker-year")
            selected_year_string = elem_selected_year.get_attribute("innerHTML")

            elem_selected_month = driver.find_element_by_class_name("ui-datepicker-month")
            selected_month_string = elem_selected_month.get_attribute("innerHTML")

            # Compute the final day-month-year string
            selected_month_year_string = selected_month_string + space + selected_year_string

        elem_date = driver.find_element_by_xpath("//td[not(contains(@class,'ui-datepicker-other-month'))]/a[text()='" + target_date + "']")
        elem_date.click()

        time.sleep(10)

        # Check the selected month, date, and year from the Calendar
        selected_month_year_val = datepicker_val.get_attribute('value')
        print(selected_month_year_val)

        self.assertEqual(selected_month_year_val, expected_month_year_val)

        print("Unit Test of jQuery Calendar passed")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()