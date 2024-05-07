from pages import LoginAdminPage
from config import OPENCART_USERNAME, OPENCART_PASSWORD
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_page_admin(browser, url):
    browser.get(url + "/administration")
    browser.find_element(*LoginAdminPage.USERNAME_INPUT).send_keys(OPENCART_USERNAME)
    browser.find_element(*LoginAdminPage.PASSWORD_INPUT).send_keys(OPENCART_PASSWORD)
    browser.find_element(*LoginAdminPage.LOGIN_BUTTON).click()
    wait = WebDriverWait(browser, 1)
    user_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img[title='user']")))
    assert user_name.get_attribute("alt") == "John Doe", "Пользователь не авторизован админом"
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#vmap")))
    user_name.click()
    profile = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()=' Your Profile']")))
    profile.click()
    profile_user_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-username")))
    assert profile_user_name.get_attribute("value") == "user", "Некорректные учетные данные админа"
    profile_first_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-firstname")))
    assert profile_first_name.get_attribute("value") == "John", "Некорректное имя админа"
    profile_last_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-lastname")))
    assert profile_last_name.get_attribute("value") == "Doe", "Некорректная фамилия админа"
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Logout']"))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()=' Please enter your login details.']")))
    browser.find_element(*LoginAdminPage.LOGIN_BUTTON).is_enabled()
