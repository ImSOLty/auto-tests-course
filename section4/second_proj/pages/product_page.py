from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_purchase_button(self):
        assert self.element_present(ProductPageLocators.PURCHASE_BUTTON)[0], 'Purchase button not found'

    def should_be_basket_button(self):
        assert self.element_present(ProductPageLocators.BASKET_BUTTON)[0], 'Basket button not found'

    def purchase_item(self):
        self.element_present(ProductPageLocators.PURCHASE_BUTTON)[1].click()

    def go_to_basket(self):
        self.element_present(ProductPageLocators.BASKET_BUTTON)[1].click()
