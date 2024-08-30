import allure

from page_objects.register_page import RegisterPage

@allure.title("Присутствие элементов на странице регистрации")
def test_user_registration(browser, url):
    browser.get(url + "/index.php?route=account/register")
    register_page = RegisterPage(browser)
    register_page.visibility_of_first_name_field()
    register_page.visibility_of_last_name_field()
    register_page.visibility_of_email_field()
    register_page.visibility_of_password_field()
    register_page.continue_button_is_clickable()
    register_page.privacy_police_is_clickable()
