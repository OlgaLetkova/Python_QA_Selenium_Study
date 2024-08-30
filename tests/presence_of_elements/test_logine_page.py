import allure

from pages import LoginAdminPage

@allure.title("Присутствие элементов на странице логина в админку")
def test_login_page_admin(browser, url):
    browser.get(url + "/administration")
    browser.find_element(*LoginAdminPage.USERNAME_INPUT)
    browser.find_element(*LoginAdminPage.PASSWORD_INPUT)
    browser.find_element(*LoginAdminPage.LOGO)
    browser.find_element(*LoginAdminPage.LOGIN_BUTTON)
    browser.find_element(*LoginAdminPage.OPENCART_LINK)
