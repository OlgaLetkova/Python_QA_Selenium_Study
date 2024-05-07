from selenium.webdriver.common.by import By


class HomePage:
    SEARCH_LINE = (By.NAME, "search")
    CART_BUTTON = (By.CSS_SELECTOR, "div[id='header-cart']")
    LOGO = (By.CSS_SELECTOR, "div[id='logo']")
    MY_ACCOUNT = (By.XPATH, "//*[text()='My Account']")
    CONTACT = (By.XPATH, "//*[text()='123456789']")
    SHOPPING_CART = (By.CSS_SELECTOR, "[title='Shopping Cart']")
