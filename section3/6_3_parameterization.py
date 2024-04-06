import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='session', name='browser')
def create_browser():
    browser = Chrome(service=Service(ChromeDriverManager().install()))
    yield browser
    browser.quit()


class TestSuite:
    URL = "http://selenium1py.pythonanywhere.com/"

    @pytest.mark.parametrize('language', ['ru', 'en-gb'])
    def test_that_login_link_exists_on_each_language(self, browser, language):
        browser.get(f'{self.URL}/{language}')
        assert browser.find_element(By.ID, 'login_link')


@pytest.mark.parametrize('language', ['ru', 'en-gb'])
class TestSuite2:  # Just for the example
    URL = "http://selenium1py.pythonanywhere.com/"

    def test_that_login_link_exists_on_each_language(self, browser, language):  # Will be ran twice
        browser.get(f'{self.URL}/{language}')
        assert browser.find_element(By.ID, 'login_link')

    def test_that_login_link_exists_on_each_language2(self, browser, language):  # Will be ran twice as well
        browser.get(f'{self.URL}/{language}')
        assert browser.find_element(By.ID, 'login_link')
