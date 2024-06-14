import allure
import selenium.common.exceptions
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

    @allure.step("Проверяю, что отображается список товаров")
    def visibility_of_products_list(self):
        self.logger.info("Checking visibility of products list")
        self.get_element(self.PRODUCT_LIST)
        self.get_element(self.FORM_PRODUCTS)

    @allure.step("Открываю форму добавления товара")
    def click_add_new(self):
        self.logger.info("Click 'ADD NEW' button")
        self.click(self.ADD_NEW_BUTTON)

    @allure.step("Фильтрую список по {filer_field}")
    def filter_table(self, filer_field, filter_value):
        self.logger.info("Filtering table by %s" % filer_field)
        AddProductPage(self.browser).input_product_field(field=filer_field, value=filter_value)
        self.browser.find_element(By.ID, 'button-filter').click()

    @allure.step("Проверяю, что элемент '{model}' находится в списке")
    def new_element_is_enabled_in_table(self, model):
        self.logger.info("Check if element %s is present in table" % model)
        try:
            self.get_element((By.XPATH, f"//td[contains(., '{model}')]"))
        except selenium.common.exceptions.TimeoutException:
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name="screenshot_image",
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Элемент '{model}' не найден в списке")

    @allure.step("Получаю имя нового продукта")
    def get_name_of_new_product(self):
        self.logger.info("Getting new product name")
        wait = WebDriverWait(self.browser, 1)
        name = wait.until(EC.visibility_of_element_located(self.NEW_PRODUCT_NAME)).text
        return name

    @allure.step("Выбираю элемент списка, кликая чекбокс рядом с ним")
    def click_element_in_table(self):
        self.click(self.CHECKBOX)

    @allure.step("Нажимаю кнопку удаления")
    def click_delete_button(self):
        self.logger.info("Click 'DELETE' element")
        self.browser.find_elements(*self.DELETE_BUTTON)[1].click()

    @allure.step("Получаю пустой список")
    def get_empty_list(self):
        self.logger.info("Getting empty table")
        wait = WebDriverWait(self.browser, 1)
        empty_list_text = wait.until(EC.visibility_of_element_located(self.EMPTY_LIST_TEXT)).text
        return empty_list_text

    @allure.step("Нажимаю кнопку удаления")
    def click_delete_button_in_short_float(self):
        self.logger.info("Click 'DELETE' in short float")
        self.browser.find_elements(*self.DELETE_BUTTON)[0].click()
