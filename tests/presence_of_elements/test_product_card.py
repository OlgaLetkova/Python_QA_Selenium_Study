import allure
import pytest
from page_objects.product_page import ProductPage

@allure.title("Присутствие элементов на странице карточки товара")
@pytest.mark.parametrize("product", ["macbook"])
def test_mac_card(browser, url, product):
    browser.get(url + f"en-gb/product/{product}")
    product_page = ProductPage(browser)
    product_page.visibility_of_product_image(product=product)
    product_page.add_to_cart_is_clickable()
    product_page.visibility_of_wish_list_button()
    product_page.visibility_of_compare_button()
    product_page.specification_is_clickable()
    product_page.review_is_clickable()
