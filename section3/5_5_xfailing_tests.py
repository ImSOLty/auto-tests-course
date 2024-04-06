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
    @pytest.mark.xfail(reason="fixing this bug right now")  # Will be marked as XFAIL not to fail the suite
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(URL)
        browser.find_element(By.CSS_SELECTOR, "input.btn.btn-default")

    @pytest.mark.xfail(run=False)  # Even not try to run this test
    def test_existence_login_link(self, browser):
        browser.get(URL)
        assert browser.find_element(By.ID, 'login_link')

    @pytest.mark.xfail(strict=True)  # If this test will pass, then mark the result as fail!
    def test_existence_basket_link_main_page(self, browser):
        browser.get(URL)
        assert browser.find_element(By.XPATH, '//a[text()="Посмотреть корзину"]')
