import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions
from config import OPENCART_USERNAME, OPENCART_PASSWORD
from page_objects.login_page import LoginPage
from page_objects import AlertSuccessElement
from page_objects.alert_element import AlertConfirmElement
from page_objects.admin_elements_table_page import ElementsTablePage
from file_helpers.csv_helper import read_lines_from_csv
from files import DATA_CSV_FILE_PATH
from page_objects.admin_home_page import DashBoardPage
from page_objects.add_product_page import AddProductPage
from selenium.webdriver.common.by import By
from files import USER_DATA_FILE_PATH


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome"
    )
    parser.addoption(
        "--yadriver",
        action="store_true",
        default="C:/Users/allet/selenium_drivers/yandexdriver.exe"
    )
    parser.addoption(
        "--url",
        default="http://192.168.2.122:8081/"
    )


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    yadriver = request.config.getoption("--yadriver")
    if browser_name == "ya":
        options = Options()
        options.binary_location = "C:/Program Files (x86)/Yandex/YandexBrowser/Application/browser.exe"
        service = Service(executable_path=yadriver)
        browser = webdriver.Chrome(service=service, options=options)
    elif browser_name == "chrome":
        options = Options()
        browser = webdriver.Chrome(service=Service(), options=options)
    elif browser_name == "ff":
        options = FFOptions()
        browser = webdriver.Firefox(service=FFService(), options=options)
    else:
        raise ValueError(f"Browser {browser_name} not supported")

    browser.maximize_window()

    yield browser

    browser.close()


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture()
def login_as_admin(browser, url):
    browser.get(url + "/administration")
    LoginPage(browser).login(OPENCART_USERNAME, OPENCART_PASSWORD)


@pytest.fixture()
def delete_product(browser):
    yield
    products_page = ElementsTablePage(browser)
    products_page.click_element_in_table()
    products_page.click_delete_button()
    AlertConfirmElement(browser).confirm_action()
    AlertSuccessElement(browser).success_message()


@pytest.fixture()
@pytest.mark.parametrize(("section", "item"),
                         [("catalog", "Products")])
def create_product(browser, login_as_admin, section, item):
    general_data = read_lines_from_csv()
    second_tab_data = read_lines_from_csv(source_file=DATA_CSV_FILE_PATH)
    dash_board = DashBoardPage(browser)
    dash_board.click_dashboard_menu(section=section)
    dash_board.click_dashboard_menu_item(item=item)
    products_page = ElementsTablePage(browser)
    products_page.visibility_of_products_list()
    products_page.click_add_new()
    add_product_form = AddProductPage(browser)
    add_product_form.visibility_of_add_product()
    add_product_form.input_product_field(field=general_data[0]["field"], value=general_data[0]["value"])
    add_product_form.input_product_field(field=general_data[1]["field"], value=general_data[1]["value"])
    browser.find_element(By.CSS_SELECTOR, 'html').send_keys(Keys.PAGE_UP)
    add_product_form.switch_tab(tab="Data")
    add_product_form.input_product_field(field=second_tab_data[0]["field"],
                                         value=second_tab_data[0]["value"])
    browser.find_element(By.CSS_SELECTOR, 'html').send_keys(Keys.PAGE_UP)
    time.sleep(1)
    add_product_form.switch_tab(tab="SEO")
    add_product_form.input_product_field(field="Keyword", value="qwerty128")
    browser.find_element(By.CSS_SELECTOR, 'html').send_keys(Keys.PAGE_UP)
    time.sleep(1)
    add_product_form.save_product()
    AlertSuccessElement(browser).success_message()
    yield


@pytest.fixture()
def delete_user(browser, url):
    yield
    browser.get(url + "/administration")
    LoginPage(browser).login(OPENCART_USERNAME, OPENCART_PASSWORD)
    dash_board = DashBoardPage(browser)
    dash_board.click_dashboard_menu(section="customer")
    browser.find_elements(By.LINK_TEXT, "Customers")[1].click()
    elements_page = ElementsTablePage(browser)
    user_data = read_lines_from_csv(source_file=USER_DATA_FILE_PATH)
    elements_page.filter_table(filer_field=user_data[2]["field"], filter_value=user_data[2]["value"])
    elements_page.new_element_is_enabled_in_table(model=user_data[2]["value"])
    elements_page.click_element_in_table()
    elements_page.click_delete_button_in_short_float()
    AlertConfirmElement(browser).confirm_action()
    AlertSuccessElement(browser).success_message()
