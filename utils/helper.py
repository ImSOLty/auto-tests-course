from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Browser(object):
    _instance = None
    _browser: Chrome = None

    def __new__(cls, *args, **kwargs):
        url = kwargs.get('url')
        if not cls._instance:
            cls._instance = object.__new__(cls)
            cls._instance._browser = Chrome(service=Service(ChromeDriverManager().install()))
        cls._instance._set_url(url)
        return cls._instance

    def _set_url(self, new_url):
        if new_url and self._browser.current_url != new_url:
            self._browser.get(new_url)

    def get_browser(self):
        return self._browser

    def __del__(self):
        self._browser.quit()
