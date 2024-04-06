from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.urls import Urls


def test_main_page(browser):
    main_page = MainPage(browser, Urls.get_base_url())
    main_page.open()
    main_page.should_be_login_link()
    main_page.go_login_link()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
