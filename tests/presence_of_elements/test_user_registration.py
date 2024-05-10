from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_user_registration(browser, url):
    browser.get(url + "/index.php?route=account/register")
    wait = WebDriverWait(browser, 1)
    wait.until(EC.visibility_of_element_located((By.ID, "input-firstname")))
    wait.until(EC.visibility_of_element_located((By.ID, "input-lastname")))
    wait.until(EC.visibility_of_element_located((By.NAME, "email")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-password")))
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Continue']")))
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Privacy Policy")))
