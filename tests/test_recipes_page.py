import allure
from pages.recipes_page import RecipesPage


class TestRecipesPage:

    @allure.title('Проверка открытия страницы создания рецептов')
    def test_redirect_to_recipes_create_page(self, recipes_page_with_authorization):
        with allure.step('Открываем главную страницу'):
            page = RecipesPage(recipes_page_with_authorization)
        with allure.step('Кликаем на раздел создание рецептов'):
            page.click_on_create_recipe()
        with allure.step('Проверяем, что страница открыта'):
            assert page.check_recipes_create_page_is_open()
