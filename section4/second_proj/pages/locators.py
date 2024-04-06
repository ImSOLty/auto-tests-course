from selenium.webdriver.common.by import By


class ProductPageLocators:
    PURCHASE_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    BASKET_BUTTON = (By.XPATH, '//header//a[contains(@href, "basket/")]')


class BasketPageLocators:
    BASKET_TOTALS = (By.ID, 'basket_totals')
    BASKET_FORMSET = (By.ID, 'basket_formset')
    PRODUCTS = (By.CSS_SELECTOR, '#basket_formset .row')


class ProductLocatorInside:
    NAME_AND_LINK = (By.CSS_SELECTOR, ':nth-of-type(2) a')
    INPUT_COUNT = (By.XPATH, '//input[contains(@id, "quantity")]')
    PRICE = (By.CSS_SELECTOR, ':nth-of-type(4) > p')
    TOTAL_PRICE = (By.CSS_SELECTOR, ':nth-of-type(5) > p')
