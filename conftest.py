import allure
import pytest
from pages.sing_in_page import SignInPage
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


@pytest.fixture
def driver_local():
    with allure.step('Открываем браузер'):
        width = 1920
        height = 1080
        driver = webdriver.Chrome()
        driver.set_window_size(width, height)
    yield driver
    with allure.step('Закрываем браузер'):
        driver.quit()


@pytest.fixture
def recipes_page_with_authorization(driver):
    with allure.step('Открываем страницу для входа пользователя'):
        page = SignInPage(driver)
    with allure.step('Заполняем необходимые данные для успешного входа'):
        page.fill_out_sing_in_form()
        page.check_recipes_page_is_open()
    return driver


@pytest.fixture(name='driver')
def driver_remote():
    options = Options()
    options.set_capability("selenoid:options", {"screenResolution": "1920x1080x24"})
    driver = webdriver.Remote(
        command_executor='http://selenoid:4444/wd/hub',
        options=options
    )
    yield driver
    driver.quit()
