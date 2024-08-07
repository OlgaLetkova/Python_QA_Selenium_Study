import time

import allure
import pytest
from page_objects import ProductPage, TopElement, CartElement


@allure.title("При переключении валют цены на товары меняются на главной")
@pytest.mark.parametrize("currency", ["Euro", "Pound"])
def test_switch_currency_home_page(browser, url, currency):
    browser.get(url)
    currency_element = TopElement(browser)
    currency_element.open_currency_dialog()
    currency_locator = currency_element.get_currency_locator(currency)
    currency_element.click_currency(currency=currency_locator)
    CartElement(browser).cart_is_enabled(currency_locator.split(" ")[0])
    value = ProductPage(browser).get_product_price()
    assert currency_locator.split(" ")[0] in value, (
            "Цены на товары на главной странице не соответствуют валюте"
            and allure.attach(body=browser.get_screenshot_as_png(),
                              name="screenshot_image",
                              attachment_type=allure.attachment_type.PNG))
