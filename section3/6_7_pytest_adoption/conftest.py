import pytest
from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.chrome.service import Service
from webdriver_manager import chrome, firefox


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        browser = Chrome(service=Service(executable_path=chrome.ChromeDriverManager().install()))
    elif browser_name == "firefox":
        browser = Firefox(service=Service(executable_path=firefox.GeckoDriverManager().install()))
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()
