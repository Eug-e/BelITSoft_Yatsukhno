'''c)	For the third code task you should create UI tests for https://www.metric-conversions.org/ .
	You have to create the following tests:
- Test for converting Celsius to Fahrenheit temperature;
- Test for converting meters to feet;
- Test for converting ounces to grams;'''

from selenium import webdriver
import unittest


class Conversions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../BelITSoft/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_temperature(self):
        self.driver.get('https://www.metric-conversions.org/temperature/celsius-to-fahrenheit.html')
        self.driver.find_element_by_name("argumentConv").send_keys(10)

    def test_length(self):
        self.driver.get('https://www.metric-conversions.org/length/meters-to-feet.htm')
        self.driver.find_element_by_name("argumentConv").send_keys(20)

    def test_weight(self):
        self.driver.get('https://www.metric-conversions.org/weight/ounces-to-grams.htm')
        self.driver.find_element_by_name("argumentConv").send_keys(30)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Completed!')


if __name__ == '__main__':
    unittest.main()