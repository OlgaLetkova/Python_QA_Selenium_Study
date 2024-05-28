from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TopElement:
    CURRENCY_LIST = By.CLASS_NAME, "list-inline"
    ACCOUNT_LIST = By.XPATH, "//span[contains(text(), 'My Account')]"

    def __init__(self, browser):
        self.browser = browser

    def open_currency_dialog(self):
        self.browser.find_element(*self.CURRENCY_LIST).click()

    def click_currency(self, currency):
        wait = WebDriverWait(self.browser, 3)
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, f"{currency}"))).click()

    def open_account_list(self):
        self.browser.find_element(*self.ACCOUNT_LIST).click()

    def click_registration(self):
        wait = WebDriverWait(self.browser, 2)
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register"))).click()
