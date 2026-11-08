import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from pages.main_page import MainPage


def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="Запускать Firefox без окна")


@pytest.fixture
def driver(request):
    options = Options()
    if request.config.getoption("--headless"):
        options.add_argument("-headless")
    browser = webdriver.Firefox(options=options)
    browser.set_window_size(1920, 1080)
    yield browser
    browser.quit()


@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.open_main_page()
    return page

