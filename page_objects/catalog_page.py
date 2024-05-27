from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class CatalogPage(BasePage):
    DISPLAY_CONTROL = By.ID, "display-control"
    PRODUCT_COMPARE = By.XPATH, "//*[text()='Product Compare (0)']"
    PRODUCT_LIST = By.ID, "product-list"

    def visibility_of_display_control(self):
        self.get_element(self.DISPLAY_CONTROL)
        self.get_clickable_element(self.PRODUCT_COMPARE)

    def visibility_of_product_list(self):
        self.get_element(self.PRODUCT_LIST)

    def visibility_of_section_image(self, section):
        self.get_element((By.CSS_SELECTOR, f"img[title='{section}']"))
