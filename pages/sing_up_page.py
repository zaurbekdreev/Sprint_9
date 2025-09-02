from data import *
from locators.sing_in_locators import SingInLocators
from locators.sing_up_locators import SignUpLocators
from pages.base_page import BasePage
from service import foodgram


class SignUpPage(BasePage):

    def __init__(self, *args):
        super().__init__(*args)
        self.open_url(foodgram.signup)

    def check_page_is_open(self):
        return self.current_url == foodgram.signup

    def fill_out_sign_up_form(self):
        first_name = generate_name()
        last_name = generate_last_name()
        user_name = f'{first_name}_{last_name}'
        email = generate_email()
        password = generate_password()
        self.input(SignUpLocators.FIRST_NAME, first_name)
        self.input(SignUpLocators.LAST_NAME, last_name)
        self.input(SignUpLocators.USER_NAME, user_name)
        self.input(SignUpLocators.EMAIL, email)
        self.input(SignUpLocators.PASSWORD, password)
        self.click(SignUpLocators.SUBMIT_BUTTON)

    def check_redirect_to_sing_in_page(self):
        self.awaiting_redirect(foodgram.signin)
        return self.current_url == foodgram.signin and self.find(SingInLocators.SING_IN_TITLE)
