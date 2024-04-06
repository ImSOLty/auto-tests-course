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


URL = "http://selenium1py.pythonanywhere.com/"


class TestSuite:

    @pytest.mark.skip  # Will be skipped
    def test_existence_login_link(self, browser):
        browser.get(URL)
        assert browser.find_element(By.ID, 'login_link')

    @pytest.mark.skipif(True, reason='because of your mom')  # Will be skipped if a condition is true
    def test_existence_basket_link_main_page(self, browser):
        browser.get(URL)
        assert browser.find_element(By.XPATH, '//a[text()="Посмотреть корзину"]')
