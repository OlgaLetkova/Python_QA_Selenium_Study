import time

import pytest

from page_objects.top_element import TopElement
from file_helpers.csv_helper import read_lines_from_csv
from files import USER_DATA_FILE_PATH
from page_objects.register_page import RegisterPage

user_data = read_lines_from_csv(source_file=USER_DATA_FILE_PATH)


@pytest.mark.parametrize("user_field_data",
                         [user_data])
def test_new_user_registration(browser, url, user_field_data, delete_user):
    browser.get(url)
    account_list = TopElement(browser)
    account_list.open_account_list()
    account_list.click_registration()
    register_form = RegisterPage(browser)
    for element in user_field_data:
        register_form.form_filling(field=element["field"], value=element["value"])
    register_form.click_privacy_policy()
    register_form.click_continue_button()
    time.sleep(1)
    assert register_form.success_account_creation() == "Your Account Has Been Created!"
