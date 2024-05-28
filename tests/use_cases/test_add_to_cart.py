import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from page_objects.home_page import HomePage
from page_objects.cart_element import CartElement
from page_objects.alert_element import AlertSuccessElement


def test_add_item_to_cart(browser, url):
    browser.get(url)
    HomePage(browser).add_random_item_to_cart()
    browser.find_element(By.CSS_SELECTOR, 'html').send_keys(Keys.PAGE_UP)
    time.sleep(1)
    AlertSuccessElement(browser).success_message()
    cart = CartElement(browser)
    cart.click_cart_dialog()
    item_quantity = cart.get_item_quantity()
    assert item_quantity == "x 1", "Количество товара не равно 1"
