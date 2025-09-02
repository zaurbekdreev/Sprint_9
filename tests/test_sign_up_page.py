import allure
from pages.sing_up_page import SignUpPage


class TestSignUp:

    @allure.title('Проверка открытия страницы регистрации')
    def test_sing_up_page_opens(self, driver):
        with allure.step('Открываем страницу регистрации'):
            page = SignUpPage(driver)
        with allure.step('Проверяем, что страница открыта'):
            assert page.check_page_is_open()

    @allure.title('Проверка успешной регистрации пользователя')
    def test_sing_up_flow(self, driver):
        with allure.step('Открываем страницу регистрации'):
            page = SignUpPage(driver)
        with allure.step('Заполняем необходимые поля для регистрации'):
            page.fill_out_sign_up_form()
        with allure.step('Проверяем, что пользователь успешно создан'):
            assert page.check_redirect_to_sing_in_page()
