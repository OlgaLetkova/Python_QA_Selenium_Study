import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class UserProfileElement(BasePage):
    USER_NAME = By.CSS_SELECTOR, "img[title='user']"

    @allure.step("Получаю имя и фамилию администратора")
    def get_full_user_name(self):
        self.logger.info("Getting admin profile data")
        full_user_name = self.get_element(self.USER_NAME)
        return full_user_name.get_attribute("alt")

    @allure.step("Нажимаю на имя и фамилию администратора в шапке страницы")
    def click_user_name_element(self):
        self.click(self.USER_NAME)


class UserProfileDialog(BasePage):
    PROFILE_IN_DIALOG = By.XPATH, "//*[text()=' Your Profile']"

    @allure.step("Нажимаю на профиль пользователя в выпадающем меню")
    def click_profile_in_dialog(self):
        self.logger.info("Click user profile in dialog")
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

    @allure.step("Проверяю элемент интефейса 'map' на главной странице личного кабинета администратора")
    def check_map_visibility(self):
        self.get_element(self.MAP)

    @allure.step("Открываю раздел меню {section}")
    def click_dashboard_menu(self, section):
        self.logger.info("Open dashboard menu section %s" % section)
        self.click((By.CSS_SELECTOR, f"#menu-{section}"))
        self.get_element((By.CSS_SELECTOR, "ul[class='collapse show']"))

    @allure.step("Открываю каталог {item}")
    def click_dashboard_menu_item(self, item):
        self.logger.info("Click dashboard menu item %s" % item)
        self.click((By.LINK_TEXT, f"{item}"))
