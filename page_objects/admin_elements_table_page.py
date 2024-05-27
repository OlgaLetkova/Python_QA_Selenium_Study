from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from page_objects.add_product_page import AddProductPage
from page_objects.base_page import BasePage


class ElementsTablePage(BasePage):
    PRODUCT_LIST = By.XPATH, "//*[text()=' Product List']"
    FORM_PRODUCTS = By.ID, "form-product"
    ADD_NEW_BUTTON = By.CSS_SELECTOR, "div[class='float-end'] a"
    NEW_PRODUCT_NAME = By.CSS_SELECTOR, "tbody tr td[class='text-start']"
    DELETE_BUTTON = By.CSS_SELECTOR, "div[class='float-end'] button[type='submit']"
    CHECKBOX = By.CSS_SELECTOR, "input[name='selected[]']"
    EMPTY_LIST_TEXT = By.CSS_SELECTOR, "tbody tr td[class='text-center']"

    def visibility_of_products_list(self):
        self.get_element(self.PRODUCT_LIST)
        self.get_element(self.FORM_PRODUCTS)

    def click_add_new(self):
        self.click(self.ADD_NEW_BUTTON)

    def filter_table(self, filer_field, filter_value):
        AddProductPage(self.browser).input_product_field(field=filer_field, value=filter_value)
        self.browser.find_element(By.ID, 'button-filter').click()

    def new_element_is_enabled_in_table(self, model):
        self.get_element((By.XPATH, f"//td[contains(., '{model}')]"))

    def get_name_of_new_product(self):
        wait = WebDriverWait(self.browser, 1)
        name = wait.until(EC.visibility_of_element_located(self.NEW_PRODUCT_NAME)).text
        return name

    def click_element_in_table(self):
        self.click(self.CHECKBOX)

    def click_delete_button(self):
        self.browser.find_elements(*self.DELETE_BUTTON)[1].click()

    def get_empty_list(self):
        wait = WebDriverWait(self.browser, 1)
        empty_list_text = wait.until(EC.visibility_of_element_located(self.EMPTY_LIST_TEXT)).text
        return empty_list_text

    def click_delete_button_in_short_float(self):
        self.browser.find_elements(*self.DELETE_BUTTON)[0].click()
