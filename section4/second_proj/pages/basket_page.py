from .base_page import BasePage
from .locators import BasketPageLocators, ProductLocatorInside


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_totals()

    def should_be_basket_url(self):
        assert 'basket' in self.browser.current_url, 'Not the basket url'

    def get_products(self):
        products = []
        for row in self.get_multiple_by_locator(BasketPageLocators.PRODUCTS):
            name_link = row.find_element(*ProductLocatorInside.NAME_AND_LINK)
            link = name_link.get_attribute('href')
            input_count = int(row.find_element(*ProductLocatorInside.INPUT_COUNT).get_attribute('value'))
            price = float(row.find_element(*ProductLocatorInside.PRICE).text.replace(',', '.').split()[0])
            total_price = float(row.find_element(*ProductLocatorInside.TOTAL_PRICE).text.replace(',', '.').split()[0])
            assert abs(price * input_count - total_price) < 0.01
            products.append((link, price))
        return products

    def should_be_products(self, lst: list):
        actual_products = self.get_products()
        print(actual_products)
        print(lst)
        # Yeah, O(N^2), I don't want to implement anything here...
        for link, price in lst:
            found = False
            for product in actual_products:
                if link in product[0] and price == product[1]:
                    found = True
            assert found

    def should_be_basket_totals(self):
        assert self.element_present(BasketPageLocators.BASKET_TOTALS)
