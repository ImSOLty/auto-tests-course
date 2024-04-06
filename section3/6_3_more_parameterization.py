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

    languages = [
        ("ru", "русский"),
        ("de", "немецкий"),
        pytest.param("ua", "украинский", marks=pytest.mark.xfail(reason="no ua language")),
        ("en-gb", "английский")
    ]

    @pytest.mark.parametrize("code, lang", languages)
    def test_that_login_link_exists_on_each_language(self, browser, code, lang):
        browser.get(f'{self.URL}/{code}')
        print("Проверяемый язык %s" % lang)
        assert browser.find_element(By.ID, 'login_link')
