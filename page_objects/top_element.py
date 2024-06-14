import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class TopElement(BasePage):
    CURRENCY_LIST = By.CLASS_NAME, "list-inline"
    ACCOUNT_LIST = By.XPATH, "//span[contains(text(), 'My Account')]"

    @allure.step("Открываю диалоговое окно 'Currency'")
    def open_currency_dialog(self):
        self.logger.info("Opening currency dialog")
        self.browser.find_element(*self.CURRENCY_LIST).click()

    @allure.step("Выбираю нужную валюту")
    def click_currency(self, currency):
        self.logger.info("Click 'Currency'")
        self.click(locator=(By.LINK_TEXT, f"{currency}"))

    @allure.step("Открываю диалоговое окно авторизации")
    def open_account_list(self):
        self.browser.find_element(*self.ACCOUNT_LIST).click()

    @allure.step("Нажимаю кнопку регистрации")
    def click_registration(self):
        self.logger.info("Click 'Registration'")
        self.click(locator=(By.LINK_TEXT, "Register"))

    def get_currency_locator(self, currency):
        match currency:
            case "Euro":
                currency_locator = "€ Euro"
            case "Pound":
                currency_locator = "£ Pound Sterling"
            case _:
                raise ValueError(f"Unsupported currency: {currency}")
        return currency_locator
