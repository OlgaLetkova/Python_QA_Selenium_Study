from pages import LoginAdminPage
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class LoginPage(BasePage):
    LOGOUT_BUTTON = By.XPATH, "//*[text()='Logout']"
    MESSAGE_FOR_LOGIN = By.XPATH, "//*[text()=' Please enter your login details.']"

    def login(self, username, password):
        self.browser.find_element(*LoginAdminPage.USERNAME_INPUT).send_keys(username)
        self.browser.find_element(*LoginAdminPage.PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*LoginAdminPage.LOGIN_BUTTON).click()

    def logout(self):
        self.click(self.LOGOUT_BUTTON)

    def check_logout(self):
        self.get_element(self.MESSAGE_FOR_LOGIN)
        self.browser.find_element(*LoginAdminPage.LOGIN_BUTTON).is_enabled()
