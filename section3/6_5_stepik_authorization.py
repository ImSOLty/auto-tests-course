import math
import time

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(name='browser', scope='function')
def create_browser():
    browser = Chrome(service=Service(ChromeDriverManager().install()))
    yield browser
    browser.quit()


class TestSuite:
    authorized = False

    @pytest.mark.parametrize('num', [
        '236895', '236896', '236897', '236898',
        '236899', '236903', '236904', '236905',
    ])
    def test_get_data(self, browser, num):
        browser.implicitly_wait(10)
        browser.get(f'https://stepik.org/lesson/{num}/step/1')
        browser.find_element(By.XPATH, '//a[contains(@href, "?auth=login")]').click()
        browser.find_element(By.NAME, 'login').send_keys('<email>')
        browser.find_element(By.NAME, 'password').send_keys('<password>')
        browser.find_element(By.XPATH, '//button[@type="submit"]').click()

        time.sleep(2)  # Fuck this, maybe I'm just tired... I've somehow managed to get this phrase

        WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, '//textarea[@placeholder="Напишите ваш ответ здесь..."]'))
        ).send_keys(str(math.log(int(time.time()))))

        WebDriverWait(browser, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.CLASS_NAME, 'submit-submission'))
        ).click()

        result = WebDriverWait(browser, 5).until(
            expected_conditions.visibility_of_element_located(
                (By.CLASS_NAME, 'smart-hints__hint'))
        ).text
        assert result == 'Correct!', result
