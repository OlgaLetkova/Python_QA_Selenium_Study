import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CartElement:
    CART_DIALOG = By.ID, "header-cart"
    PRODUCT_QUANTITY = By.CSS_SELECTOR, "td[class='text-end']"

    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger

    @allure.step("Нажимаю на диалоговое окно корзины")
    def click_cart_dialog(self):
        self.logger.info("Click cart dialog")
        wait = WebDriverWait(self.browser, 2)
        wait.until(EC.element_to_be_clickable(self.CART_DIALOG)).click()

    @allure.step("Получаю количество товаров в корзине")
    def get_item_quantity(self):
        self.logger.info("Getting quantity of products in cart")
        item_quantity = self.browser.find_element(*self.PRODUCT_QUANTITY).text
        return item_quantity

    def cart_is_enabled(self, currency):
        wait = WebDriverWait(self.browser, 3)
        match currency:
            case "€":
                (wait.until(EC.visibility_of_element_located((By.XPATH, f"//*[text()=' 0 item(s) - 0.00{currency}']")))
                 .is_displayed())
            case "£":
                (wait.until(EC.visibility_of_element_located((By.XPATH, f"//*[text()=' 0 item(s) - {currency}0.00']")))
                 .is_displayed())
            case "$":
                (wait.until(EC.visibility_of_element_located((By.XPATH, f"//*[text()=' 0 item(s) - {currency}0.00']")))
                 .is_displayed())
