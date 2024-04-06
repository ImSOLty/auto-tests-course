import time

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


def test_fields_existence():
    browser = SingletonBrowser()
    browser.get(LINK)
    elements = [('first name', 1), ('last name', 1), ('email', 1), ('phone', 0), ('address', 0)]
    try:
        for elem, require in elements:
            required = '@required' if require else 'not(@required)'
            browser.find_element(By.XPATH, f'//input[contains(@placeholder, "{elem}") and {required}]')
    except NoSuchElementException:
        assert False


def test_required_fields():
    browser = SingletonBrowser()
    browser.get(LINK)
    button = browser.find_element(By.XPATH, '//*[text()="Submit"]')
    inputs = browser.find_elements(By.XPATH, '//input[@required]')
    for inp in inputs:
        inp.send_keys('a')
    button.click()
    time.sleep(1)
    assert browser.find_element(By.XPATH, '//*[text()="Congratulations! You have successfully registered!"]')


def test_not_required_fields():
    browser = SingletonBrowser()
    browser.get(LINK)
    button = browser.find_element(By.XPATH, '//*[text()="Submit"]')
    inputs = browser.find_elements(By.XPATH, '//input[not(@required)]')
    for inp in inputs:
        inp.send_keys('a')
    button.click()
    time.sleep(1)
    els = browser.find_elements(By.XPATH, '//*[text()="Congratulations! You have successfully registered!"]')
    assert not els


def test_all_fields():
    browser = SingletonBrowser()
    browser.get(LINK)
    button = browser.find_element(By.XPATH, '//*[text()="Submit"]')
    inputs = browser.find_elements(By.XPATH, '//input')
    for inp in inputs:
        inp.send_keys('a')
    button.click()
    time.sleep(1)
    assert browser.find_element(By.XPATH, '//*[text()="Congratulations! You have successfully registered!"]')
