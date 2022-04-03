import pytest
import os

from selenium import webdriver

DRIVERS = os.path.expanduser("~/Drivers")


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "opera"], default="chrome")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")

    driver = None

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.headless = headless

        driver = webdriver.Chrome(
            options=options,
            executable_path=f"{DRIVERS}/chromedriver"
        )
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.headless = headless

        driver = webdriver.Firefox(
            options=options,
            executable_path=f"{DRIVERS}/geckodriver"
        )
    elif browser == "opera":
        driver = webdriver.Opera(executable_path=f"{DRIVERS}/operadriver")
    else:
        raise ValueError("Driver not supported: {}".format(browser))

    request.addfinalizer(driver.quit)

    if maximized:
        driver.maximize_window()

    return driver
    