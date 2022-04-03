import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait

URL_CATALOG = "http://demo-opencart.ru/index.php?route=product/category&path=20"


@pytest.mark.parametrize("url, title", [
    ("http://demo-opencart.ru/index.php?route=product/category&path=20", "Desktops!")
])
def test_title_catalog_page(browser, url, title):
    browser.get(url)
    current_title = browser.title
    assert current_title == title, "Неверный Title на странице Каталога"


def test_check_product_items_in_catalog(browser):
    browser.get(URL_CATALOG)
    wait = WebDriverWait(browser, 3)
    fetured_items = browser.find_elements_by_class_name("product-thumb")
    assert len(fetured_items) == 12, "Неверное количество продуктов в блоке featured"


def test_catalog_page_menu(browser):
    browser.get(URL_CATALOG)
    wait = WebDriverWait(browser, 3)
    menu_items = browser.find_elements_by_css_selector("ul.navbar-nav > li")
    assert len(menu_items) == 6, "Неверное количество элементов меню"


def test_catalog_page_footer_blocks(browser):
    browser.get(URL_CATALOG)
    wait = WebDriverWait(browser, 3)
    footer_blocks = browser.find_elements_by_xpath("//footer//ul")
    assert len(footer_blocks) == 4, "Неверное количество списков ссылок в футере"


def test_catalog_page_open_product(browser):
    browser.get(URL_CATALOG)
    wait = WebDriverWait(browser, 3)
    fetured_items = browser.find_elements_by_class_name("product-thumb")
    fetured_items[2].location_once_scrolled_into_view
    fetured_items[2].click()
    browser.find_elements_by_link_text("Apple Cinema")