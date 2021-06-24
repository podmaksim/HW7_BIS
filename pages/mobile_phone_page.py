from selenium.webdriver.common.by import By
from pages.catalog_page import CatalogPage


LOCATOR_HONOR_10X_LINK = (By.XPATH, '//div[@class="schema-product__part schema-product__part_1"]//'
                                 'a[@href="https://catalog.onliner.by/mobile/honor/10xlitednnlx9iz"]')


class MobilePhonePage(CatalogPage):

    def choice_honor_10x(self):
        self.find_element(LOCATOR_HONOR_10X_LINK).click()

