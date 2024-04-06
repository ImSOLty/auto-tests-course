import random
import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    browser = None

    def __new__(cls, *args, **kwargs):
        if not cls.browser:
            cls.browser = Chrome(service=Service(ChromeDriverManager().install()))
        if 'url' in kwargs and cls.browser.current_url != kwargs['url']:
            cls.browser.get(kwargs['url'])
        return cls.browser


URL1 = 'https://suninjuly.github.io/selects1.html'
URL2 = 'https://suninjuly.github.io/selects2.html'


def pick_sum():
    browser = Browser(url=random.choice([URL1, URL2]))
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    result = int(browser.find_element(By.ID, 'num1').text) + int(browser.find_element(By.ID, 'num2').text)
    select.select_by_visible_text(str(result))
    browser.find_element(By.TAG_NAME, 'button').click()
    time.sleep(5)
    browser.quit()


pick_sum()
