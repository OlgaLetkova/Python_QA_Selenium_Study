from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class AddProductPage(BasePage):
    ADD_PRODUCT_HEADER = By.XPATH, "//*[text()=' Add Product']"
    SAVE_PRODUCT_BUTTON = By.CSS_SELECTOR, "div[class='float-end'] button"

    def visibility_of_add_product(self):
        self.get_element(self.ADD_PRODUCT_HEADER)

    def input_product_field(self, field, value):
        self.input_value(locator=(By.CSS_SELECTOR, f"input[type='text'][placeholder='{field}']"), text=value)

    def input_product_field_text_area(self, text_field, text_value):
        self.input_value(locator=(By.CSS_SELECTOR, f"textarea[placeholder='{text_field}']"), text=text_value)

    def switch_tab(self, tab):
        self.click(locator=(By.LINK_TEXT, f"{tab}"))

    def save_product(self):
        self.click(self.SAVE_PRODUCT_BUTTON)
