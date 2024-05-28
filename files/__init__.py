import os.path

FILES_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)


PRODUCT_TEST_DATA_CSV_FILE_PATH = get_path(filename="new_product_general_data.csv")
DATA_CSV_FILE_PATH = get_path(filename="new_product_other_data.csv")
TEXT_GENERAL_DATA_CSV_FILE_PATH = get_path(filename="text_general_data.csv")
TABS_LIST_FILE_PATH = get_path(filename="tabs_list.csv")
USER_DATA_FILE_PATH = get_path(filename="user_data.csv")
