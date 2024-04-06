import os
import time

from selenium.webdriver.common.by import By
from faker import Faker

from utils.helper import Browser

fake = Faker('ru_RU')

URL = 'https://suninjuly.github.io/file_input.html'


def upload_file(path):
    browser = Browser(url=URL).get_browser()
    for inp in browser.find_elements(By.XPATH, '//input[not(@type="file")]'):
        inp.send_keys(fake.name())
    browser.find_element(By.XPATH, '//input[@type="file"]').send_keys(path)
    browser.find_element(By.TAG_NAME, 'button').click()
    time.sleep(5)


filename = os.path.join(os.path.dirname(__file__), fake.user_name() + '.txt')
with open(filename, 'w') as f:
    f.write(fake.uuid4())
    upload_file(filename)
os.remove(filename)
