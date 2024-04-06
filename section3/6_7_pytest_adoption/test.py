from selenium.webdriver.common.by import By

URL = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(URL)
    browser.find_element(By.ID, "login_link")
