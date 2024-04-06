import math

from selenium.webdriver.common.by import By

from utils.helper import Browser

URL = 'http://suninjuly.github.io/alert_accept.html'


def confirm_alert():
    Browser()
    browser = Browser(url=URL).get_browser()
    browser.find_element(By.TAG_NAME, 'button').click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = int(browser.find_element(By.ID, 'input_value').text)
    browser.find_element(By.ID, 'answer').send_keys(str(math.log(abs(12 * math.sin(x)))))
    browser.find_element(By.TAG_NAME, 'button').click()
    print(browser.switch_to.alert.text.split()[-1])


confirm_alert()
