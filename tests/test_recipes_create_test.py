import allure
from pages.recipes_create_page import RecipesCreatePage


class TestRecipesCreatePage:

    @allure.title('Проверка создания рецепта')
    def test_recipe_creation(self, recipes_page_with_authorization):
        with allure.step('Открываем страницу для создания рецепта'):
            page = RecipesCreatePage(recipes_page_with_authorization)
        with allure.step('Заполняем необходимые поля'):
            page.fill_out_recipe_form()
        with allure.step('Проверяем, что рецепт создан'):
            assert page.check_recipe_is_created()
