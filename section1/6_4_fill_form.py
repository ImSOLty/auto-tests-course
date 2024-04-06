import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

try:
    browser = Chrome(service=Service(executable_path=ChromeDriverManager().install()))
    browser.get('http://suninjuly.github.io/simple_form_find_task.html')

    data = ['A', 'B', 'C', 'D']

    inputs = browser.find_elements(By.TAG_NAME, 'input')
    for dt, inp in zip(data, inputs):
        inp.send_keys(dt)
    browser.find_element(By.ID, 'submit_button').click()
finally:
    time.sleep(5)
    browser.quit()
