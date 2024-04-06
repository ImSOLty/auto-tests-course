import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    browser = None

    def __new__(cls, *args, **kwargs):
        url = kwargs.get('url')
        if not cls.browser:
            cls.browser = Chrome(service=Service(ChromeDriverManager().install()))
        if url and url != cls.browser.current_url:
            cls.browser.get(url)
        return cls.browser

    def __del__(self):
        if self.browser:
            self.browser.quit()


def run_js_code(code='alert()'):
    browser = Browser()
    browser.execute_script(code)
    time.sleep(2)


run_js_code('document.title="hehehehe"; alert("hehehehe");')
