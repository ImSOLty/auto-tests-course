from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from utils.helper import Browser

URL = 'http://suninjuly.github.io/wait1.html'


def test_wait_and_click():
    browser = Browser(url=URL).get_browser()
    browser.implicitly_wait(5)  # Wait for 5 seconds before each element searching, if is found earlier - stop waiting
    browser.find_element(By.TAG_NAME, 'button').click()
    try:
        browser.find_element(By.ID, 'verify_message')
    except NoSuchElementException:
        assert False
    finally:
        assert True
