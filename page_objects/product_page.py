import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class ProductPage(BasePage):
    PRODUCT_PRICE = By.CSS_SELECTOR, ".price-new"
    ADD_TO_CART_BUTTON = By.XPATH, "//*[text()='Add to Cart']"
    WISH_LIST_BUTTON = By.CSS_SELECTOR, "button[formaction$='wishlist.add']"
    COMPARE_BUTTON = By.CSS_SELECTOR, "button[formaction$='compare.add']"
    SPECIFICATION = By.CSS_SELECTOR, "a[href$='#tab-specification']"
    REVIEW = By.CSS_SELECTOR, "a[href$='#tab-review']"

    @allure.step("Получаю цену товара")
    def get_product_price(self):
        self.logger.info("Getting product price")
        value = self.browser.find_element(*self.PRODUCT_PRICE).text
        return value

    def visibility_of_product_image(self, product):
        self.get_element((By.CSS_SELECTOR, f"img[title='{product}']"))

    @allure.step("Проверяю, что кнопка добавления товара в корзину кликабельна")
    def add_to_cart_is_clickable(self):
        self.get_clickable_element(self.ADD_TO_CART_BUTTON)

    def visibility_of_wish_list_button(self):
        self.get_element(self.WISH_LIST_BUTTON)

    def visibility_of_compare_button(self):
        self.get_element(self.COMPARE_BUTTON)

    @allure.step("Проверяю, что в карточке товара вкладка 'Specification' кликабельна")
    def specification_is_clickable(self):
        self.get_clickable_element(self.SPECIFICATION)

    @allure.step("Проверяю, что в карточке товара вкладка 'Review' кликабельна")
    def review_is_clickable(self):
        self.get_clickable_element(self.REVIEW)
