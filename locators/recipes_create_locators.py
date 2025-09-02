from selenium.webdriver.common.by import By

from data import INGREDIENT_NAME_1, INGREDIENT_NAME_2


class RecipesCreateLocators:
    RECIPE_NAME = By.XPATH, '//div[contains(text(), "Название рецепта")]/parent::label/input'
    INGREDIENT_NAME = By.XPATH, '//div[contains(text(), "Ингредиенты")]/parent::label/input'
    INGREDIENT_AMOUNT = By.XPATH, '//div[contains(@class, "ingredientsAmount")]//input'
    ADD_INGREDIENT = By.XPATH, '//div[contains(text(), "Добавить")]'
    TIME_OF_COOKING = By.XPATH, '//div[contains(text(), "Время приготовления")]/parent::label//input'
    RECIPE_DESCRIPTION = By.XPATH, '//textarea'
    CREATE_BUTTON = By.XPATH, '//button[contains(text(), "Создать рецепт")]'
    INGREDIENT_SUGGEST_1 = By.XPATH, f'//div[contains(text(), "{INGREDIENT_NAME_1}")]'
    INGREDIENT_SUGGEST_2 = By.XPATH, f'//div[contains(text(), "{INGREDIENT_NAME_2}")]'
    SELECT_FILE = By.XPATH, '//input[@type="file"]'
