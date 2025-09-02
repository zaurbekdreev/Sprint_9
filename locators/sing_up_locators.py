from selenium.webdriver.common.by import By


class SignUpLocators:
    FIRST_NAME = By.XPATH, '//input[contains(@name, "first_name")]'
    LAST_NAME = By.XPATH, '//input[contains(@name, "last_name")]'
    USER_NAME = By.XPATH, '//input[contains(@name, "username")]'
    EMAIL = By.XPATH, '//input[contains(@name, "email")]'
    PASSWORD = By.XPATH, '//input[contains(@name, "password")]'
    SUBMIT_BUTTON = By.XPATH, '//button[contains(text(), "Создать")]'
