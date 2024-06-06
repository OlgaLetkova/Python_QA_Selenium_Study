import allure
import pytest
from page_objects.top_element import TopElement
from page_objects.menu_catalog_element import MenuCatalogElement
from page_objects.product_page import ProductPage


@allure.title("При переключении валют цены на товары меняются в каталоге")
@pytest.mark.parametrize(("currency", "section"), [("€ Euro", "Tablets"), ("£ Pound Sterling", "Cameras")])
def test_switch_currency_catalog(browser, url, currency, section):
    browser.get(url)
    currency_element = TopElement(browser)
    currency_element.open_currency_dialog()
    currency_element.click_currency(currency=currency)
    MenuCatalogElement(browser).click_menu_section(section=section)
    value = ProductPage(browser).get_product_price()
    assert currency.split(" ")[0] in value, (
            "Цены на товары в каталоге не соответствуют валюте"
            and allure.attach(body=browser.get_screenshot_as_png(),
                              name="screenshot_image",
                              attachment_type=allure.attachment_type.PNG))
