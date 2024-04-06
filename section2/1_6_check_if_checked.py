from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    browser = None

    def __new__(cls, *args, **kwargs):
        if not cls.browser:
            cls.browser = Chrome(service=Service(ChromeDriverManager().install()))
        return cls.browser


URL = 'https://suninjuly.github.io/math.html'


def test_if_checked():
    browser = Browser()
    browser.get(URL)
    assert any([bool(inp.get_attribute('checked')) for inp in browser.find_elements(By.NAME, 'ruler')])
