import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class AlertSuccessElement:
    SUCCESS_ALERT = By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']"

    def __init__(self, browser):
        self.browser = browser

    def success_message(self):
        wait = WebDriverWait(self.browser, 2)
        wait.until(
            EC.visibility_of_element_located(self.SUCCESS_ALERT))


class AlertConfirmElement:
    def __init__(self, browser):
        self.browser = browser

    def confirm_action(self):
        self.browser.switch_to.alert.accept()
        time.sleep(2)
