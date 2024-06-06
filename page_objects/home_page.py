import random
import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from page_objects.base_page import BasePage


class HomePage(BasePage):
    ADD_TO_CART_BUTTONS = By.CSS_SELECTOR, "button[formaction$='cart.add']"

    @allure.step("Добавляю рандомный товар в корзину")
    def add_random_item_to_cart(self):
        self.logger.info("Adding random product to cart from home page")
        add_item_button_list = self.browser.find_elements(*self.ADD_TO_CART_BUTTONS)
        a = random.randint(0, len(add_item_button_list) - 1)
        self.browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.CONTROL + Keys.END)
        time.sleep(4)
        self.browser.find_elements(*self.ADD_TO_CART_BUTTONS)[a].click()
