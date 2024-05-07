from pages import HomePage


def test_home_page(browser, url):
    browser.get(url)
    browser.find_element(*HomePage.SHOPPING_CART)
    browser.find_element(*HomePage.MY_ACCOUNT)
    browser.find_element(*HomePage.LOGO)
    browser.find_element(*HomePage.SEARCH_LINE)
    browser.find_element(*HomePage.CONTACT)
    browser.find_element(*HomePage.CART_BUTTON)
