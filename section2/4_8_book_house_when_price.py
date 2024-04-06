import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.helper import Browser

URL = 'http://suninjuly.github.io/explicit_wait2.html'


def book_house():
    browser = Browser(url=URL).get_browser()
    button = browser.find_element(By.ID, 'book')
    WebDriverWait(browser, 20).until(
        expected_conditions.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    button.click()
    x = int(browser.find_element(By.ID, 'input_value').text)
    browser.find_element(By.ID, 'answer').send_keys(str(math.log(abs(12 * math.sin(x)))))
    browser.find_element(By.ID, 'solve').click()
    print(browser.switch_to.alert.text.split()[-1])


book_house()
