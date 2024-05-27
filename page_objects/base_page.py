from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def get_element(self, locator: tuple, timeout=2):
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def click(self, locator: tuple):
        ActionChains(self.browser).move_to_element(self.get_element(locator)).pause(0.3).click().perform()

    def input_value(self, locator: tuple, text: str):
        self.get_element(locator).click()
        self.get_element(locator).clear()
        for l in text:
            self.get_element(locator).send_keys(l)

    def get_profile_user_data(self, locator: tuple, timeout=2):
        return (WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
                .get_attribute("value"))

    def get_clickable_element(self, locator: tuple, timeout=2):
        return WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator))

