from pages.main_page import MainPage
from pages.catalog_page import CatalogPage
from pages.mobile_phone_page import MobilePhonePage
from pages.honor_10x_page import Honor10XPage


def test_onliner(browser):
    main_page = MainPage(browser)
    main_page.open_base_page()
    main_page.catalog_link()
    catalog_page = CatalogPage(browser)
    catalog_page.electronics_button()
    catalog_page.mobile_active_link()
    catalog_page.mobile_link()
    catalog_page.mobile_phone_link()
    mobile_phone_page = MobilePhonePage(browser)
    mobile_phone_page.choice_honor_10x()
    honor_10X_page = Honor10XPage(browser)
    price = honor_10X_page.choice_price()
    honor_10X_page.search_field()
    honor_10X_page.search_phone()
    comparison_price = honor_10X_page.check_price()
    assert price == comparison_price
