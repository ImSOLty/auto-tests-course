import math

from selenium.webdriver.common.by import By

from utils.helper import Browser

URL = 'http://suninjuly.github.io/redirect_accept.html'


def tabs_solve():
    browser = Browser(url=URL).get_browser()
    browser.find_element(By.TAG_NAME, 'button').click()
    tabs = browser.window_handles
    # switch to the second tab
    browser.switch_to.window(tabs[1])
    x = int(browser.find_element(By.ID, 'input_value').text)
    browser.find_element(By.ID, 'answer').send_keys(str(math.log(abs(12 * math.sin(x)))))
    browser.find_element(By.TAG_NAME, 'button').click()
    print(browser.switch_to.alert.text.split()[-1])


tabs_solve()
