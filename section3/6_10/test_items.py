from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

URL = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_to_busket_button_existence(browser):
    browser.implicitly_wait(5)
    browser.get(URL)
    try:
        browser.find_element(By.CSS_SELECTOR, '#add_to_basket_form > button')
    except NoSuchElementException:
        assert False, "Add to basket button not found"
