import time

import pytest

from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.urls import Urls


@pytest.mark.parametrize('link', ["coders-at-work_207/?promo=offer0",
                                  "coders-at-work_207/?promo=offer1",
                                  "coders-at-work_207/?promo=offer2",
                                  "coders-at-work_207/?promo=offer3",
                                  "coders-at-work_207/?promo=offer4",
                                  "coders-at-work_207/?promo=offer5",
                                  "coders-at-work_207/?promo=offer6",
                                  "coders-at-work_207/?promo=offer7",
                                  "coders-at-work_207/?promo=offer8",
                                  "coders-at-work_207/?promo=offer9"])
def test_purchase_and_pass_quiz(browser, link):
    product_page = ProductPage(browser, f'{Urls.CATALOGUE_URL}/{link}')
    product_page.should_be_purchase_button()
    product_page.purchase_item()
    product_page.solve_quiz_and_get_code()
    product_page.go_to_basket()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    time.sleep(3)
    basket_page.should_be_products([('coders-at-work_207', 19.99)])
