import time

import allure
import selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class AlertSuccessElement:
    SUCCESS_ALERT = By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']"

    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger

    @allure.step("Проверяю, что появилось всплывающее сообщение об успешном действии на странице")
    def success_message(self):
        self.logger.info("Waiting for success message")
        try:
            wait = WebDriverWait(self.browser, 2)
            wait.until(
                EC.visibility_of_element_located(self.SUCCESS_ALERT))
        except selenium.common.exceptions.TimeoutException:
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name="screenshot_image",
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Не удалось выполнить действие на странице")


class AlertConfirmElement:
    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger

    @allure.step("Подтверждаю действие во всплывающем окне")
    def confirm_action(self):
        self.logger.info("Confirm action on page")
        self.browser.switch_to.alert.accept()
        time.sleep(2)
