from selenium.common import NoSuchElementException


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.browser.implicitly_wait(timeout)
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, element: tuple):
        try:
            self.browser.find_element(element[0], element[1])
        except NoSuchElementException:
            return False
        return True

