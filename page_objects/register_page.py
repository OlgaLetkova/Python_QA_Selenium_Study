from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class RegisterPage(BasePage):
    FIRST_NAME = By.ID, "input-firstname"
    LAST_NAME = By.ID, "input-lastname"
    EMAIL = By.NAME, "email"
    PASSWORD = By.CSS_SELECTOR, "#input-password"
    CONTINUE_BUTTON = By.XPATH, "//*[text()='Continue']"
    PRIVACY_POLICE = By.LINK_TEXT, "Privacy Policy"

    def visibility_of_first_name_field(self):
        self.get_element(self.FIRST_NAME)

    def visibility_of_last_name_field(self):
        self.get_element(self.LAST_NAME)

    def visibility_of_email_field(self):
        self.get_element(self.EMAIL)

    def visibility_of_password_field(self):
        self.get_element(self.PASSWORD)

    def continue_button_is_clickable(self):
        self.get_clickable_element(self.CONTINUE_BUTTON)

    def privacy_police_is_clickable(self):
        self.get_clickable_element(self.PRIVACY_POLICE)

    def form_filling(self, field, value):
        self.input_value(locator=(By.CSS_SELECTOR, f"input[placeholder='{field}']"), text=value)

    def click_privacy_policy(self):
        self.click((By.NAME, "agree"))

    def click_continue_button(self):
        self.browser.find_element(*self.CONTINUE_BUTTON).click()

    def success_account_creation(self):
        success_text = self.browser.find_element(By.CSS_SELECTOR, "div[id='content'] h1").text
        return success_text
