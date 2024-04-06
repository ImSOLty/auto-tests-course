import math
import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

try:
    browser = Chrome(service=Service(ChromeDriverManager().install()))
    browser.get('http://suninjuly.github.io/find_link_text')
    link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e) * 10000)))
    link.click()
    for inp in browser.find_elements(By.TAG_NAME, 'input'):
        inp.send_keys('sheeeesh')
    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    time.sleep(10)
    browser.quit()
