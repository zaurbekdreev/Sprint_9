from selenium.webdriver.common.by import By


class RecipesLocators:
    recipes_create = By.XPATH, '//a[contains(text(), "Создать")]'
    created_recipe = By.XPATH, '//h1'
