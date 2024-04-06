from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.helper import Browser

URL = 'http://suninjuly.github.io/wait2.html'


def test_wait_and_click():
    browser = Browser(url=URL).get_browser()
    WebDriverWait(browser, 5).until(
        expected_conditions.element_to_be_clickable((By.ID, 'verify'))
    ).click()
    try:
        browser.find_element(By.ID, 'verify_message')
    except NoSuchElementException:
        assert False
    finally:
        assert True
