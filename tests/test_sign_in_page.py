import allure
from pages.sing_in_page import SignInPage


class TestSignInPage:

    @allure.title('Проверка открытия страницы логина')
    def test_sing_in_page_opens(self, driver):
        with allure.step('Открываем страницу для входа пользователя'):
            page = SignInPage(driver)
        with allure.step('Проверяем, что страница открыта'):
            assert page.check_page_is_open()

    @allure.title('Проверка успешного входа пользователя с корректными данными')
    def test_sing_in(self, driver):
        with allure.step('Открываем страницу для входа пользователя'):
            page = SignInPage(driver)
        with allure.step('Заполняем необходимые для выхода поля'):
            page.fill_out_sing_in_form()
        with allure.step('Проверяем, что вход произошел успешно'):
            assert page.check_recipes_page_is_open()
