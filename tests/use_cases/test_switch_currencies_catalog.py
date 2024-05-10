from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_switch_currencies_to_euro(browser, url):
    browser.get(url)
    browser.find_element(By.CLASS_NAME, "list-inline").click()
    wait = WebDriverWait(browser, 3)
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "€ Euro"))).click()
    browser.find_element(By.XPATH, "//*[text()='Tablets']").click()
    value = browser.find_element(By.CSS_SELECTOR, ".price-new").text
    assert "€" in value


def test_switch_currencies_to_pound(browser, url):
    browser.get(url)
    browser.find_element(By.CLASS_NAME, "list-inline").click()
    wait = WebDriverWait(browser, 3)
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "£ Pound Sterling"))).click()
    browser.find_element(By.XPATH, "//*[text()='Cameras']").click()
    value = browser.find_element(By.CSS_SELECTOR, ".price-new").text
    assert "£" in value
