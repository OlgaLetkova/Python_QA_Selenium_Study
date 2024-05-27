import pytest
from page_objects.top_element import TopElement
from page_objects.menu_catalog_element import MenuCatalogElement
from page_objects.product_page import ProductPage


@pytest.mark.parametrize(("currency", "section"), [("€ Euro", "Tablets"), ("£ Pound Sterling", "Cameras")])
def test_switch_currency(browser, url, currency, section):
    browser.get(url)
    currency_element = TopElement(browser)
    currency_element.open_currency_dialog()
    currency_element.click_currency(currency=currency)
    MenuCatalogElement(browser).click_menu_section(section=section)
    value = ProductPage(browser).get_product_price()
    assert currency.split(" ")[0] in value
