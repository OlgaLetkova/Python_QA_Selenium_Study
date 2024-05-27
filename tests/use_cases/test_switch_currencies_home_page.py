import pytest
from page_objects import ProductPage, TopElement


@pytest.mark.parametrize("currency", ["€ Euro", "£ Pound Sterling"])
def test_switch_currency(browser, url, currency):
    browser.get(url)
    currency_element = TopElement(browser)
    currency_element.open_currency_dialog()
    currency_element.click_currency(currency=currency)
    value = ProductPage(browser).get_product_price()
    assert currency.split(" ")[0] in value
