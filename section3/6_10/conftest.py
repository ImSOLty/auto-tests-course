import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='es',
                     help="Choose language")


@pytest.fixture(scope='session')
def browser(request):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': request.config.getoption("language")})
    browser = Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield browser
    browser.quit()
