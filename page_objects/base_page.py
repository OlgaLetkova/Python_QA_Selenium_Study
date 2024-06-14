import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import logging


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger
        self.class_name = type(self).__name__

    def get_element(self, locator: tuple, timeout=2):
        self.logger.debug("%s: Getting element by locator: %s" % (self.class_name, str(locator)))
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Выполняю клик по элементу {locator}")
    def click(self, locator: tuple):
        self.logger.debug("%s: Clicking element: %s" % (self.class_name, str(locator)))
        ActionChains(self.browser).move_to_element(self.get_element(locator)).pause(0.3).click().perform()

    @allure.step("Ввожу '{text}' в элемент {locator}")
    def input_value(self, locator: tuple, text: str):
        self.logger.debug("%s: Input %s in input %s" % (self.class_name, text, locator))
        self.get_element(locator).click()
        self.get_element(locator).clear()
        for l in text:
            self.get_element(locator).send_keys(l)

    @allure.step("Получаю данные профиля пользователя из поля {locator}")
    def get_profile_user_data(self, locator: tuple, timeout=2):
        self.logger.debug("%s: Getting user profile data from field %s" % (self.class_name, locator))
        return (WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
                .get_attribute("value"))

    def get_clickable_element(self, locator: tuple, timeout=2):
        self.logger.debug("%s: Getting clickable element by locator: %s" % (self.class_name, str(locator)))
        return WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator))
