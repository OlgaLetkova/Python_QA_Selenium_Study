from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CartElement:
    CART_DIALOG = By.ID, "header-cart"
    PRODUCT_QUANTITY = By.CSS_SELECTOR, "td[class='text-end']"

    def __init__(self, browser):
        self.browser = browser

    def click_cart_dialog(self):
        wait = WebDriverWait(self.browser, 2)
        wait.until(EC.element_to_be_clickable(self.CART_DIALOG)).click()

    def get_item_quantity(self):
        item_quantity = self.browser.find_element(*self.PRODUCT_QUANTITY).text
        return item_quantity
