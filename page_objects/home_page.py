import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


class HomePage:
    ADD_TO_CART_BUTTONS = By.CSS_SELECTOR, "button[formaction$='cart.add']"

    def __init__(self, browser):
        self.browser = browser

    def add_random_item_to_cart(self):
        add_item_button_list = self.browser.find_elements(*self.ADD_TO_CART_BUTTONS)
        a = random.randint(0, len(add_item_button_list) - 1)
        self.browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.CONTROL + Keys.END)
        time.sleep(4)
        self.browser.find_elements(*self.ADD_TO_CART_BUTTONS)[a].click()
