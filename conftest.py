import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions


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
