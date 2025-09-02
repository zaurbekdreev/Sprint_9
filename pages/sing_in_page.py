from data import PASSWORD, EMAIL
from locators.sing_in_locators import SingInLocators
from pages.base_page import BasePage
from service import foodgram


class SignInPage(BasePage):

    def __init__(self, *args):
        super().__init__(*args)
        self.open_url(foodgram.signin)

    def check_page_is_open(self):
        return self.current_url == foodgram.signin

    def fill_out_sing_in_form(self):
        self.input(SingInLocators.EMAIL, EMAIL)
        self.input(SingInLocators.PASSWORD, PASSWORD)
        self.click(SingInLocators.SUBMIT_BUTTON)

    def check_recipes_page_is_open(self):
        self.awaiting_redirect(foodgram.recipes)
        return self.current_url == foodgram.recipes
