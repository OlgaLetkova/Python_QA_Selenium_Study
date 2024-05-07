
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_catalog_page(browser, url):
    browser.get(url)
    browser.find_element(By.XPATH, "//*[text()='Desktops']").click()
    wait = WebDriverWait(browser, 1)
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Mac (1)")))
    browser.find_element(By.XPATH, "//*[text()='Laptops & Notebooks']").click()
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Show All Laptops & Notebooks")))
    browser.find_element(By.LINK_TEXT, "Show All Laptops & Notebooks").click()
    wait.until(EC.visibility_of_element_located((By.ID, "display-control")))
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Product Compare (0)']")))
    wait.until(EC.visibility_of_element_located((By.ID, "product-list")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img[title='Laptops & Notebooks']")))
