import math
import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    browser = None

    def __new__(cls, *args, **kwargs):
        url = kwargs.get('url')
        if not cls.browser:
            cls.browser = Chrome(service=Service(ChromeDriverManager().install()))
        if url and cls.browser.current_url != url:
            cls.browser.get(url)
        return cls.browser

    def __del__(self):
        if self.browser:
            self.browser.quit()


URL = 'https://suninjuly.github.io/execute_script.html'


def scroll_and_click():
    browser = Browser(url=URL)
    x = int(browser.find_element(By.ID, 'input_value').text)
    browser.find_element(By.ID, 'answer').send_keys(str(math.log(abs(12 * math.sin(x)))))
    for value in ['#robotCheckbox', '#robotsRule', 'button']:
        element = browser.find_element(By.CSS_SELECTOR, value)
        browser.execute_script('arguments[0].scrollIntoView(true)', element)
        element.click()
    time.sleep(5)


scroll_and_click()
