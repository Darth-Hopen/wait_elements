import pytest
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from LoginAdminPage import LoginAdminPage

URL_ADMIN_PAGE = "http://demo-opencart.ru/"


@pytest.mark.parametrize("url, title", [
    ("http://demo-opencart.ru/admin/", "Авторизация")
])
def test_title_login_page(browser, url, title):
    browser.get(url)
    current_title = browser.title
    assert current_title == title, "Неверный Title на странице Admin Page"


def test_login_page(browser):
    browser.get((URL_ADMIN_PAGE) + "/admin")
    browser.find_element_by_id("input-username")
    browser.find_element_by_name("password")
    browser.find_element_by_css_selector("button[type='submit']")
    browser.find_element_by_link_text("Забыли пароль?")
    browser.find_element_by_xpath("//*[text()='OpenCart']")


def test_login_page_external(browser):
    browser.get((URL_ADMIN_PAGE) + "/admin")
    browser.find_element(*LoginAdminPage.USERNAME_INPUT)
    browser.find_element(*LoginAdminPage.PASSWORD_INPUT)
    browser.find_element(*LoginAdminPage.SUBMIT_BUTTON)
    browser.find_element(*LoginAdminPage.FORGOTTEN_PASSWORD)
    browser.find_element(*LoginAdminPage.OPENCART_LINK)
