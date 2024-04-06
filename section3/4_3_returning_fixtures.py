import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    # before testcase
    br = Chrome(service=Service(ChromeDriverManager().install()))
    yield br
    # after testcase
    br.quit()


URL = "http://selenium1py.pythonanywhere.com/"


class TestSuite:
    def test_existence_login_link(self, browser):
        browser.get(URL)
        assert browser.find_element(By.ID, 'login_link')

    def test_existence_basket_link_main_page(self, browser):
        browser.get(URL)
        assert browser.find_element(By.XPATH, '//a[text()="Посмотреть корзину"]')
