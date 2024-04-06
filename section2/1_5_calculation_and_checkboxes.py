import math
import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    browser = None

    def __new__(cls, *args, **kwargs):
        if not cls.browser:
            cls.browser = Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        return cls.browser


URL = 'https://suninjuly.github.io/math.html'


def calculate_and_submit():
    browser = Browser()
    browser.get(URL)
    inp_value = int(browser.find_element(By.ID, 'input_value').text)
    browser.find_element(By.ID, 'answer').send_keys(str(math.log(abs(12 * math.sin(inp_value)))))
    for path in ['//*[@for="robotCheckbox"]', '//*[@for="robotsRule"]', '//button[text()="Submit"]']:
        browser.find_element(By.XPATH, path).click()
    time.sleep(5)
    browser.quit()


calculate_and_submit()
