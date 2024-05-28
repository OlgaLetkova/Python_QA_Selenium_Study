from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MenuCatalogElement:
    def __init__(self, browser):
        self.browser = browser

    def click_menu_section(self, section):
        self.browser.find_element(By.XPATH, f"//*[text()='{section}']").click()

    def click_all_section_products(self, section):
        wait = WebDriverWait(self.browser, 1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, f"Show All {section}"))).click()

    def visibility_of_product(self, product):
        wait = WebDriverWait(self.browser, 1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, f"{product}")))
