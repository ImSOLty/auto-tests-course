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
            cls.browser = Chrome(service=Service(ChromeDriverManager().install()))
        if 'url' in kwargs and cls.browser.current_url != kwargs['url']:
            cls.browser.get(kwargs['url'])
        return cls.browser


URL = 'http://suninjuly.github.io/get_attribute.html'


def find_treasure():
    browser = Browser(url=URL)
    x = int(browser.find_element(By.XPATH, '//img').get_attribute('valuex'))
    browser.find_element(By.ID, 'answer').send_keys(str(math.log(abs(12 * math.sin(x)))))
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.TAG_NAME, 'button').click()
    time.sleep(5)
    browser.quit()


find_treasure()
