import random
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_item_to_cart(browser, url):
    browser.get(url)
    add_item_button_list = browser.find_elements(By.CSS_SELECTOR, "button[formaction$='cart.add']")
    a = random.randint(0, len(add_item_button_list) - 1)
    wait = WebDriverWait(browser, 2)
    browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.CONTROL + Keys.END)
    time.sleep(2)
    browser.find_elements(By.CSS_SELECTOR, "button[formaction$='cart.add']")[a].click()
    browser.find_element(By.CSS_SELECTOR, 'html').send_keys(Keys.PAGE_UP)
    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']")))
    wait.until(EC.element_to_be_clickable((By.ID, "header-cart"))).click()
    item_quantity = browser.find_element(By.CSS_SELECTOR, "td[class='text-end']").text
    assert item_quantity == "x 1", "Количество товара не равно 1"
