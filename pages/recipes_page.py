from locators.header_locators import HeaderLocators
from pages.base_page import BasePage
from service import foodgram


class RecipesPage(BasePage):

    def __init__(self, *args):
        super().__init__(*args)
        self.open_url(foodgram.recipes)

    def click_on_create_recipe(self):
        self.click(HeaderLocators.recipes_create)
        self.awaiting_redirect(foodgram.recipes_create)

    def check_recipes_create_page_is_open(self):
        return self.current_url == foodgram.recipes_create
