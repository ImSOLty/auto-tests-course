from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestSuite1:
    browser = None
    URL = "http://selenium1py.pythonanywhere.com/"

    @classmethod
    def setup_class(cls):
        cls.browser = Chrome(service=Service(ChromeDriverManager().install()))

    @classmethod
    def teardown_class(cls):
        cls.browser.quit()

    def test_existence_login_link(self):
        self.browser.get(self.URL)
        assert self.browser.find_element(By.ID, 'login_link')

    def test_existence_basket_link_main_page(self):
        self.browser.get(self.URL)
        assert self.browser.find_element(By.XPATH, '//a[text()="Посмотреть корзину"]')
