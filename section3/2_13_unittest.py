import time
import unittest

from selenium.common import NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

LINK = 'https://suninjuly.github.io/registration2.html'


class SingletonBrowser:
    browser = None

    def __new__(cls, *args, **kwargs):
        if not cls.browser:
            cls.browser = Chrome(service=Service(ChromeDriverManager().install()))
        return cls.browser


class TestTask(unittest.TestCase):

    def test_fields_existence(self):
        self.browser = SingletonBrowser()
        self.browser.get(LINK)
        elements = [('first name', 1), ('last name', 1), ('email', 1), ('phone', 0), ('address', 0)]
        for elem, require in elements:
            try:
                required = '@required' if require else 'not(@required)'
                self.browser.find_element(By.XPATH, f'//input[contains(@placeholder, "{elem}") and {required}]')
            except NoSuchElementException:
                self.fail(f"expected {elem}, {require}")

    def test_required_fields(self):
        self.browser = SingletonBrowser()
        self.browser.get(LINK)
        button = self.browser.find_element(By.XPATH, '//*[text()="Submit"]')
        inputs = self.browser.find_elements(By.XPATH, '//input[@required]')
        for inp in inputs:
            inp.send_keys('a')
        button.click()
        time.sleep(1)
        self.assertTrue(
            self.browser.find_element(By.XPATH, '//*[text()="Congratulations! You have successfully registered!"]'))

    def test_not_required_fields(self):
        self.browser = SingletonBrowser()
        self.browser.get(LINK)
        button = self.browser.find_element(By.XPATH, '//*[text()="Submit"]')
        inputs = self.browser.find_elements(By.XPATH, '//input[not(@required)]')
        for inp in inputs:
            inp.send_keys('a')
        button.click()
        time.sleep(1)
        els = self.browser.find_elements(By.XPATH, '//*[text()="Congratulations! You have successfully registered!"]')
        self.assertFalse(els)

    def test_all_fields(self):
        self.browser = SingletonBrowser()
        self.browser.get(LINK)
        button = self.browser.find_element(By.XPATH, '//*[text()="Submit"]')
        inputs = self.browser.find_elements(By.XPATH, '//input')
        for inp in inputs:
            inp.send_keys('a')
        button.click()
        time.sleep(1)
        self.assertTrue(
            self.browser.find_element(By.XPATH, '//*[text()="Congratulations! You have successfully registered!"]'))


if __name__ == "__main__":
    unittest.main()
