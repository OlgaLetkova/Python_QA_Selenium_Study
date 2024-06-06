import time

import allure
import pytest
from page_objects import AlertSuccessElement
from page_objects.admin_home_page import DashBoardPage
from page_objects.admin_elements_table_page import ElementsTablePage
from file_helpers.csv_helper import read_lines_from_csv
from page_objects.alert_element import AlertConfirmElement

product_test_general_data = read_lines_from_csv()


@allure.title("Удаление товара из списка в разделе администратора")
@pytest.mark.parametrize(("section", "item", "general_data"),
                         [("catalog", "Products", product_test_general_data)])
def test_delete_product(browser, create_product, login_as_admin, section, item, general_data):
    dash_board = DashBoardPage(browser)
    dash_board.click_dashboard_menu(section=section)
    dash_board.click_dashboard_menu_item(item=item)
    products_page = ElementsTablePage(browser)
    products_page.visibility_of_products_list()
    products_page.filter_table(filer_field=product_test_general_data[0]["field"],
                               filter_value=product_test_general_data[0]["value"])
    time.sleep(1)
    products_page.click_element_in_table()
    products_page.click_delete_button()
    AlertConfirmElement(browser).confirm_action()
    AlertSuccessElement(browser).success_message()
    assert products_page.get_empty_list() == "No results!"
