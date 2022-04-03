import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

URL_PRODUCT_PAGE = "http://demo-opencart.ru/index.php?route=product/product&path=57&product_id=49"


# Параметризация тестовой функции для проверки Title
@pytest.mark.parametrize("url, title", [
    ("http://demo-opencart.ru/index.php?route=product/product&path=57&product_id=49", "Samsung Galaxy Tab 10.1")
])
def test_title_product_page(browser, url, title):
    browser.get(url)
    current_title = browser.title
    assert current_title == title, "Неверный Title на странице карточки товара"


# Проверка количества элементов фотографий товара на странице
def test_check_product_photos(browser):
    browser.get(URL_PRODUCT_PAGE)
    wait = WebDriverWait(browser, 3)
    photo_product_items = browser.find_elements_by_class_name("thumbnail")
    assert len(photo_product_items) == 7, "Неверное количество элементов фотографий товара на странице"


# Проверка наличия вкладки Description на странице товара
def test_check_description_item(browser):
    browser.get(URL_PRODUCT_PAGE)
    WebDriverWait(browser, 4).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Description')))


# Проверка количества элементов меню на странице каталога
def test_catalog_page_menu(browser):
    browser.get(URL_PRODUCT_PAGE)
    wait = WebDriverWait(browser, 3)
    menu_items = browser.find_elements_by_css_selector("ul.navbar-nav > li")
    assert len(menu_items) == 6, "Неверное количество элементов меню"

# Проверка количества списков ссылок в футере на странице каталога
def test_catalog_page_footer_blocks(browser):
    browser.get(URL_PRODUCT_PAGE)
    wait = WebDriverWait(browser, 3)
    footer_blocks = browser.find_elements_by_xpath("//footer//ul")
    assert len(footer_blocks) == 4, "Неверное количество списков ссылок в футере"