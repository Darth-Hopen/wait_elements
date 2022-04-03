import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL_REGISTER_PAGE = "http://demo-opencart.ru/index.php?route=account/register"


@pytest.mark.parametrize("url, title", [
    ("http://demo-opencart.ru/index.php?route=product/product&path=57&product_id=49", "Личный кабинет")
])
def test_title_product_page(browser, url, title):
    browser.get(url)
    current_title = browser.title
    assert current_title == title, "Неверный Title на странице карточки товара"
    

def test_product_page(browser):
    browser.get(URL_REGISTER_PAGE)
    wait = WebDriverWait(driver=browser, timeout=2)
    wait.until(EC.title_is("Register Account"))

    browser.find_element(By.CSS_SELECTOR, "aside > div.list-group")
    browser.find_element(By.CSS_SELECTOR, "fieldset#account")
    browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    browser.find_element(By.LINK_TEXT, "Privacy Policy")
    browser.find_element(By.CSS_SELECTOR, "[value='1'][name='newsletter']")
    browser.find_element(By.CSS_SELECTOR, "[value='Continue']")