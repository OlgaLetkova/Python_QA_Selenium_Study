from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class UserProfileElement(BasePage):
    USER_NAME = By.CSS_SELECTOR, "img[title='user']"

    def get_full_user_name(self):
        full_user_name = self.get_element(self.USER_NAME)
        return full_user_name.get_attribute("alt")

    def click_user_name_element(self):
        self.click(self.USER_NAME)


class UserProfileDialog(BasePage):
    PROFILE_IN_DIALOG = By.XPATH, "//*[text()=' Your Profile']"

    def click_profile_in_dialog(self):
        self.click(self.PROFILE_IN_DIALOG)


class UserProfilePage(BasePage):
    PROFILE_USER_NAME = By.CSS_SELECTOR, "#input-username"
    FIRST_NAME = By.CSS_SELECTOR, "#input-firstname"
    LAST_NAME = By.CSS_SELECTOR, "#input-lastname"

    def get_profile_user_name(self):
        return self.get_profile_user_data(self.PROFILE_USER_NAME)

    def get_profile_first_name(self):
        return self.get_profile_user_data(self.FIRST_NAME)

    def get_profile_last_name(self):
        return self.get_profile_user_data(self.LAST_NAME)


class DashBoardPage(BasePage):
    MAP = By.CSS_SELECTOR, "#vmap"

    def check_map_visibility(self):
        self.get_element(self.MAP)

    def click_dashboard_menu(self, section):
        self.click((By.CSS_SELECTOR, f"#menu-{section}"))
        self.get_element((By.CSS_SELECTOR, "ul[class='collapse show']"))

    def click_dashboard_menu_item(self, item):
        self.click((By.LINK_TEXT, f"{item}"))
