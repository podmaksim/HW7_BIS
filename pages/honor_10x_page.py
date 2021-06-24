from selenium.webdriver.common.by import By


from pages.mobile_phone_page import MobilePhonePage

LINK = 'https://catalog.onliner.by/mobile/honor/10xlitednnlx9iz/prices'

LOCATOR_PRICE = (By.XPATH, f'//div[@class="offers-description__price offers-description__price_primary"]//a[@href="{LINK}"]')
LOCATOR_SEARCH_FIELD = (By.XPATH, '//input[@class="fast-search__input"]')

LOCATOR_SEARCH_PHONE = (By.XPATH, '//a[contains(text(),"изумрудно-зеленый")]')
LOCATOR_FRAME = (By.XPATH, '//iframe[@class="modal-iframe"]')


class Honor10XPage(MobilePhonePage):

    def choice_price(self):
        return self.find_element(LOCATOR_PRICE).text

    def search_field(self):
        self.find_element(LOCATOR_SEARCH_FIELD).send_keys('Смартфон HONOR 10X Lite DNN-LX9 4GB/128GB')

    def search_phone(self):
        self.driver.switch_to.frame(self.find_element(LOCATOR_FRAME))
        self.find_element(LOCATOR_SEARCH_PHONE).click()
        self.driver.switch_to.default_content()

    def check_price(self):
        return self.find_element(LOCATOR_PRICE).text


