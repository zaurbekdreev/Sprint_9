from faker import Faker
from datetime import datetime
import os


def path_to_file(path):
    return os.path.abspath(path)


fake = Faker()

EMAIL = 'zdreev@yandex.ru'
PASSWORD = 'praktikum'
RECIPE_NAME = 'Пирог с яблоками'
INGREDIENT_NAME_1 = 'яблоки'
INGREDIENT_NAME_2 = 'тесто готовое'
INGREDIENT_AMOUNT = '100'
TIME_OF_COOKING = '60'
RECIPE_DESCRIPTION = 'тест описание'


def generate_name():
    return fake.first_name()


def generate_last_name():
    return fake.last_name()


def generate_email():
    number = int(datetime.now().timestamp() * 1000)
    return f'test_email_{number}@yandex.ru'


def generate_password():
    return fake.password()
