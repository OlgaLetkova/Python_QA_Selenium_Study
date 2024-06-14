import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class MenuCatalogElement(BasePage):

    @allure.step("Нажимаю на раздел '{section}' в каталоге")
    def click_menu_section(self, section):
        self.logger.info("Click menu section %s in dashboard" % section)
        self.browser.find_element(By.XPATH, f"//*[text()='{section}']").click()

    @allure.step("Нажимаю на кнопку перехода ко всем товарам в разделе '{section}' каталога")
    def click_all_section_products(self, section):
        self.logger.info("Click all products in section %s" % section)
        self.click(locator=(By.LINK_TEXT, f"Show All {section}"))

    def visibility_of_product(self, product):
        self.get_element(locator=(By.LINK_TEXT, f"{product}"))
