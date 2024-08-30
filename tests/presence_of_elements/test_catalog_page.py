import allure
import pytest
from page_objects.menu_catalog_element import MenuCatalogElement
from page_objects.catalog_page import CatalogPage

@allure.title("Присутствие элементов на странице каталога")
@pytest.mark.parametrize(("section", "product"), [("Desktops", "Mac (1)"), ("Laptops & Notebooks", "Macs (0)")])
def test_catalog_page(browser, url, section, product):
    browser.get(url)
    catalog = MenuCatalogElement(browser)
    catalog.click_menu_section(section=section)
    catalog.visibility_of_product(product=product)
    catalog.click_all_section_products(section=section)
    catalog_page = CatalogPage(browser)
    catalog_page.visibility_of_display_control()
    catalog_page.visibility_of_product_list()
    catalog_page.visibility_of_section_image(section=section)
