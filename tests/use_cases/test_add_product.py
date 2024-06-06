import time

import allure
import pytest
from selenium.webdriver import Keys

from page_objects import AlertSuccessElement
from page_objects.admin_home_page import DashBoardPage
from page_objects.admin_elements_table_page import ElementsTablePage
from page_objects.add_product_page import AddProductPage
from file_helpers.csv_helper import read_lines_from_csv
from files import DATA_CSV_FILE_PATH
from files import TEXT_GENERAL_DATA_CSV_FILE_PATH
from selenium.webdriver.common.by import By
from files import TABS_LIST_FILE_PATH

product_test_general_data = read_lines_from_csv()
text_general_data = read_lines_from_csv(source_file=TEXT_GENERAL_DATA_CSV_FILE_PATH)
product_second_tab_data = read_lines_from_csv(source_file=DATA_CSV_FILE_PATH)
tabs = read_lines_from_csv(source_file=TABS_LIST_FILE_PATH)


@allure.title("Добавление нового товара в разделе администратора")
@pytest.mark.parametrize(("section", "item", "general_data", "text_data", "tabs_list", "second_tab_data"),
                         [("catalog", "Products", product_test_general_data, text_general_data,
                           tabs, product_second_tab_data)])
def test_add_new_product(browser, login_as_admin, section, item, general_data, text_data, tabs_list,
                         second_tab_data, delete_product):
    dash_board = DashBoardPage(browser)
    dash_board.click_dashboard_menu(section=section)
    dash_board.click_dashboard_menu_item(item=item)
    products_page = ElementsTablePage(browser)
    products_page.visibility_of_products_list()
    products_page.click_add_new()
    add_product_form = AddProductPage(browser)
    add_product_form.visibility_of_add_product()

    with allure.step("Заполняю форму добавления нового товара, вкладка General"):
        for element in general_data:
            add_product_form.input_product_field(field=element["field"], value=element["value"])
            browser.execute_script("window.scrollBy(0,200)")
            time.sleep(1)
        for row in text_data:
            add_product_form.input_product_field_text_area(text_field=row["text_field"],
                                                           text_value=row["text_value"])
            browser.execute_script("window.scrollBy(0,200)")
            time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, 'html').send_keys(Keys.PAGE_UP)

        with allure.step("Заполняю форму добавления нового товара, вкладка Data"):
            add_product_form.switch_tab(tab=tabs_list[0]["tab"])
            for data_row in second_tab_data:
                add_product_form.input_product_field(field=data_row["field"], value=data_row["value"])
                browser.execute_script("window.scrollBy(0,100)")
                time.sleep(1)
            browser.find_element(By.CSS_SELECTOR, 'html').send_keys(Keys.PAGE_UP)
            time.sleep(1)

            with allure.step("Заполняю форму добавления нового товара, вкладка SEO"):
                add_product_form.switch_tab(tab=tabs_list[1]["tab"])
                add_product_form.input_product_field(field="Keyword", value="qwerty128")
                browser.find_element(By.CSS_SELECTOR, 'html').send_keys(Keys.PAGE_UP)
                time.sleep(1)

                add_product_form.save_product()

                with allure.step("Проверяю, что карточка нового товара добавилась"):
                    AlertSuccessElement(browser).success_message()
                    dash_board.click_dashboard_menu_item(item=item)
                    products_page.filter_table(filer_field=product_test_general_data[0]["field"],
                                               filter_value=product_test_general_data[0]["value"])
                    products_page.new_element_is_enabled_in_table(model=second_tab_data[0]["value"])
                    new_product_name = products_page.get_name_of_new_product()
                    assert product_test_general_data[0]["value"] in new_product_name
