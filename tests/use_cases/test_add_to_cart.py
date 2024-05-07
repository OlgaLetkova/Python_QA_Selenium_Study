import random

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_item_to_cart(browser, url):
    browser.get(url)
    add_item_button_list = browser.find_elements(By.CSS_SELECTOR, "button[formaction$='cart.add']")
    a = random.randint(0, len(add_item_button_list) - 1)
    wait = WebDriverWait(browser, 1)
    browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.CONTROL + Keys.END)
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//button[@title='Add to Cart'][{a}]"))).click()
