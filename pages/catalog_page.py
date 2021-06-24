from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


from pages.main_page import MainPage


LOCATOR_ELECTRONICS_BUTTON = (By.XPATH, '//li[@data-id="1"]')

LOCATOR_MOBILE_ACTIVE_LINK = (By.XPATH, '//div[@class="catalog-navigation-list__wrapper"]')

LOCATOR_MOBILE_LINK = (By.XPATH, '//div[@data-id="1"]//'
                                   'div[@class="catalog-navigation-list__aside catalog-navigation-list__aside_active"]//'
                                   'div[contains( text(),"Мобильные")]')
LOCATOR_MOBILE_PHONE_LINK = (By.XPATH, '//a[@href="https://catalog.onliner.by/mobile"]//'
                                           'span[contains( text(),"Мобильные телефоны")][1]')


class CatalogPage(MainPage):

    def electronics_button(self):
        self.find_element(LOCATOR_ELECTRONICS_BUTTON).click()

    def mobile_active_link(self):
        hover = self.find_element(LOCATOR_MOBILE_ACTIVE_LINK)
        ActionChains(self.driver).move_to_element(hover).perform()

    def mobile_link(self):
        self.find_element(LOCATOR_MOBILE_LINK).click()

    def mobile_phone_link(self):
        self.find_element(LOCATOR_MOBILE_PHONE_LINK).click()
