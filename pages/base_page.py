import selenium
from functools import wraps
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, driver: selenium.webdriver.Chrome):
        self.driver = driver
        self.timeout = 15
        self.wait = WebDriverWait(self.driver, self.timeout)

    @staticmethod
    def wait_for_element_visibility(func):
        @wraps(func)
        def wrapper(self, locator):
            self.wait.until(expected_conditions.visibility_of_element_located(locator))
            return func(self, locator)

        return wrapper

    @staticmethod
    def wait_for_element_presence(func):
        @wraps(func)
        def wrapper(self, locator):
            self.wait.until(expected_conditions.presence_of_element_located(locator))
            return func(self, locator)

        return wrapper

    @staticmethod
    def wait_for_element_clickability(func):
        @wraps(func)
        def wrapper(self, locator):
            self.wait.until(expected_conditions.element_to_be_clickable(locator))
            return func(self, locator)

        return wrapper

    @staticmethod
    def wait_for_element_invisibility(func):
        @wraps(func)
        def wrapper(self, locator):
            self.wait.until(expected_conditions.invisibility_of_element_located(locator))
            return func(self, locator)

        return wrapper

    def open_url(self, url) -> bool:
        """
        :param url: ссылка на ресурс
        :return: статус полной загрузки страницы
        """
        self.driver.get(url)
        return self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    @property
    def current_url(self):
        return self.driver.current_url

    @wait_for_element_visibility
    def find(self, locator):
        return self.driver.find_element(*locator)

    def input(self, locator, text):
        self.find(locator).send_keys(text)

    @wait_for_element_presence
    def find_hidden(self, locator):
        return self.driver.find_element(*locator)

    @wait_for_element_invisibility
    def wait_to_disappear(self, locator):
        pass

    @wait_for_element_clickability
    def click(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @wait_for_element_clickability
    def alt_click(self, locator):
        self.find(locator).click()

    def is_element_present(self, locator):
        return len(self.driver.find_elements(*locator)) > 0

    def awaiting_redirect(self, url, wait_until_equals=True):
        self.wait.until(lambda d: d.current_url == url if wait_until_equals else d.current_url != url)

    def upload_img(self, locator, file_path):
        self.find_hidden(locator).send_keys(file_path)

    def scroll_to(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
