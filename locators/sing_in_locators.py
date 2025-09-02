from selenium.webdriver.common.by import By


class SingInLocators:
    SING_IN_TITLE = By.XPATH, '//h1[contains(text(), "Войти на сайт")]'
    EMAIL = By.XPATH, '//input[contains(@name, "email")]'
    PASSWORD = By.XPATH, '//input[contains(@name, "password")]'
    SUBMIT_BUTTON = By.XPATH, '//button[contains(text(), "Войти")]'
