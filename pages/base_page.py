from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_page = 'https://www.onliner.by/'

    def open_base_page(self,):
        self.driver.get(self.base_page)

    def find_element(self, locator: tuple, time=20):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            f'Can not find element {locator}')

    def find_elements(self, locator: tuple, time=20):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            f'Can not find element {locator}')
