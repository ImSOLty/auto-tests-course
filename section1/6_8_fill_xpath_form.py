import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

LINK = 'http://suninjuly.github.io/find_xpath_form'

try:
    browser = Chrome(service=Service(ChromeDriverManager().install()))
    browser.get(LINK)
    for inp in browser.find_elements(By.XPATH, '//input'):
        inp.send_keys('a')
    browser.find_element(By.XPATH, '//*[text()="Submit"]').click()
finally:
    time.sleep(5)
    browser.quit()
