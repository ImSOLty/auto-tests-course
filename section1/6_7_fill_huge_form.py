import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

LINK = 'http://suninjuly.github.io/huge_form.html'

try:
    browser = Chrome(service=Service(ChromeDriverManager().install()))
    browser.get(LINK)
    for inp in browser.find_elements(By.TAG_NAME, 'input'):
        inp.send_keys('a')
    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    time.sleep(5)
    browser.quit()
