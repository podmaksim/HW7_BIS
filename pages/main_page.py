from pages.base_page import BasePage
from selenium.webdriver.common.by import By


LOCATOR_CATALOG_LINK = (By.CLASS_NAME, 'b-main-navigation__text')


class MainPage(BasePage):

    def catalog_link(self):
        self.find_element(LOCATOR_CATALOG_LINK).click()
