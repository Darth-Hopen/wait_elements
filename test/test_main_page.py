import pytest
import time
from selenium.webdriver.support.wait import WebDriverWait

URL_MAIN = "http://demo-opencart.ru/index.php"


# Параметризация тестовой функции для проверки Title
@pytest.mark.parametrize("url, title", [
    ("http://demo-opencart.ru/index.php", "Store")
])
def test_title_main_page(browser, url, title):
    browser.get(url)
    current_title = browser.title
    assert current_title == title, "Неверный Title на Главной странице"


# Проверка количества элементов слайдера на Главной странице
def test_check_swiper_elements_main_page(browser):
    browser.get(URL_MAIN)
    wait = WebDriverWait(browser, 3)
    fetured_items = browser.find_elements_by_class_name("swiper-viewport")
    assert len(fetured_items) == 2, "Неверное количество элементов слайдера на Главной странице"


# Проверка количества продуктов на Главной странице
def test_check_product_items_main_page(browser):
    browser.get(URL_MAIN)
    wait = WebDriverWait(browser, 3)
    fetured_items = browser.find_elements_by_class_name("product-thumb")
    assert len(fetured_items) == 4, "Неверное количество продуктов на Главной странице"


# Проверка количества элементов меню на Главной странице
def test_main_page_menu(browser):
    browser.get(URL_MAIN)
    wait = WebDriverWait(browser, 3)
    menu_items = browser.find_elements_by_css_selector("ul.navbar-nav > li")
    assert len(menu_items) == 8, "Неверное количество элементов меню"


# Проверка клика кнопки корзины
def test_main_page_button_cart(browser):
    browser.get(URL_MAIN)
    wait = WebDriverWait(browser, 3)
    browser.find_element_by_id("cart").click()
