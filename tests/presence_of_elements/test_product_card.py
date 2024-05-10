from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_mac_card(browser, url):
    browser.get(url + "en-gb/product/laptop-notebook/macbook")
    wait = WebDriverWait(browser, 1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"img[title='MacBook']")))
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Add to Cart']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[formaction$='wishlist.add']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[formaction$='compare.add']")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href$='#tab-specification']")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href$='#tab-review']")))
