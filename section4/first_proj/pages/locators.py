from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.ID, 'login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTRATION_FORM = (By.ID, 'register_form')
