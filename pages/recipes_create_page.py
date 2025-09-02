from data import *
from locators.recipes_create_locators import RecipesCreateLocators
from locators.recipes_locators import RecipesLocators
from pages.base_page import BasePage
from service import foodgram


class RecipesCreatePage(BasePage):

    def __init__(self, *args):
        super().__init__(*args)
        self.open_url(foodgram.recipes_create)

    def fill_out_recipe_form(self):
        self.input(RecipesCreateLocators.RECIPE_NAME, RECIPE_NAME)
        self.input(RecipesCreateLocators.INGREDIENT_NAME, INGREDIENT_NAME_1)
        self.click(RecipesCreateLocators.INGREDIENT_SUGGEST_1)
        self.input(RecipesCreateLocators.INGREDIENT_AMOUNT, INGREDIENT_AMOUNT)
        self.click(RecipesCreateLocators.ADD_INGREDIENT)
        self.input(RecipesCreateLocators.INGREDIENT_NAME, INGREDIENT_NAME_2)
        self.click(RecipesCreateLocators.INGREDIENT_SUGGEST_2)
        self.input(RecipesCreateLocators.INGREDIENT_AMOUNT, INGREDIENT_AMOUNT)
        self.click(RecipesCreateLocators.ADD_INGREDIENT)
        self.input(RecipesCreateLocators.TIME_OF_COOKING, TIME_OF_COOKING)
        self.input(RecipesCreateLocators.RECIPE_DESCRIPTION, RECIPE_DESCRIPTION)
        # self.scroll_to(RecipesCreateLocators.CREATE_BUTTON) - ломает тест при запуске в контейнере
        self.upload_img(RecipesCreateLocators.SELECT_FILE, path_to_file('assets/pie.jpg'))
        self.click(RecipesCreateLocators.CREATE_BUTTON)
        self.awaiting_redirect(foodgram.recipes_create, wait_until_equals=False)

    def check_recipe_is_created(self):
        return self.find(RecipesLocators.created_recipe).text == RECIPE_NAME
