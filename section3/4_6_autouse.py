import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='class')
def browser():
    br = Chrome(service=Service(ChromeDriverManager().install()))
    yield br
    br.quit()


@pytest.fixture(autouse=True)  # autouse means that it will be called before each case in any case
def autouse_example():
    print('one more test:')


URL = "http://selenium1py.pythonanywhere.com/"


class TestSuite:
    def test_existence_login_link(self, browser):
        browser.get(URL)
        assert browser.find_element(By.ID, 'login_link')

    def test_existence_basket_link_main_page(self, browser):
        browser.get(URL)
        assert browser.find_element(By.XPATH, '//a[text()="Посмотреть корзину"]')
