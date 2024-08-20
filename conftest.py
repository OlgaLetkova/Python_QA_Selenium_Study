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
import logging
import datetime


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="http://192.168.1.50:8081/")
    parser.addoption("--log_level", action="store", default="INFO")
    parser.addoption("--executor", action="store", default="127.0.0.1")
    parser.addoption("--mobile", action="store_true")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--headless", default="True")
    parser.addoption("--run", default="local")
    parser.addoption("--bv", default="125.0")
    parser.addoption("--host", default="127.0.0.1")
    parser.addoption("--port", default="5000")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    log_level = request.config.getoption("--log_level")
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")
    headless = request.config.getoption("--headless")
    run = request.config.getoption("--run")
    version = request.config.getoption("--bv")

    executor_url = f"http://{executor}:4444/wd/hub"

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    match browser_name:
        case "yandex":
            options = Options()
            if headless == "True":
                options.add_argument("headless=new")
            options.binary_location = "/usr/bin/yandex-browser"
            service = Service(executable_path="/home/olelet/Загрузки/drivers/yandexdriver")
            browser = webdriver.Chrome(service=service, options=options)

        case "chrome":
            options = Options()
            if headless == "True":
                options.add_argument("headless=new")
            if run == "local":
                browser = webdriver.Chrome(service=Service(), options=options)
            elif run == "remote":
                caps = {
                    "browserName": browser_name,
                    "browserVersion": version,
                    "selenoid:options": {
                        "name": request.node.name,
                        "enableVNC": vnc
                    }
                }
                for k, v in caps.items():
                    options.set_capability(k, v)

                browser = webdriver.Remote(
                    command_executor=executor_url,
                    options=options
                )

        case "firefox":
            options = FFOptions()
            if headless == "True":
                options.add_argument("headless=new")
            if run == "local":
                browser = webdriver.Firefox(service=FFService(), options=options)
            elif run == "remote":
                caps = {
                    "browserName": "firefox",
                    "browserVersion": version,
                    "selenoid:options": {
                        "name": request.node.name,
                        "sessionTimeout": "1m",
                        "enableVNC": vnc
                    }
                }
                for k, v in caps.items():
                    options.set_capability(k, v)

                browser = webdriver.Remote(
                    command_executor=executor_url,
                    options=options
                )

        case _:
            raise ValueError(f"Browser {browser_name} not supported")

    browser.maximize_window()

    browser.logger = logger

    logger.info("Browser %s started" % browser)

    def fin():
        browser.quit()
        logger.info("===> Test %s finished at %s" % (request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)
    yield browser


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
    add_product_form.save_product()
    AlertSuccessElement(browser).success_message()


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


@pytest.fixture(scope="session")
def host(request):
    return request.config.getoption("--host")


@pytest.fixture(scope="session")
def port(request):
    return request.config.getoption("--port")
