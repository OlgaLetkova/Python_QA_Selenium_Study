from config import OPENCART_USERNAME, OPENCART_PASSWORD
from page_objects.login_page import LoginPage
from page_objects.admin_home_page import UserProfileElement, DashBoardPage, UserProfileDialog, UserProfilePage


def test_login_page_admin(browser, url):
    browser.get(url + "/administration")
    LoginPage(browser).login(OPENCART_USERNAME, OPENCART_PASSWORD)
    name_in_header = UserProfileElement(browser)
    full_user_name = name_in_header.get_full_user_name()
    assert full_user_name == "John Doe", "Пользователь не авторизован админом"
    DashBoardPage(browser).check_map_visibility()
    name_in_header.click_user_name_element()
    UserProfileDialog(browser).click_profile_in_dialog()
    profile_page = UserProfilePage(browser)
    assert profile_page.get_profile_user_name() == "user", "Некорректные учетные данные админа"
    assert profile_page.get_profile_first_name() == "John", "Некорректное имя админа"
    assert profile_page.get_profile_last_name() == "Doe", "Некорректная фамилия админа"
    LoginPage(browser).logout()
    LoginPage(browser).check_logout()
