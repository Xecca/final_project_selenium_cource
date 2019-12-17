from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
from .locators import ProductPageLocators
from .locators import BasketPageLocators
from .locators import MainPageLocators
import time

class BasketPage(BasePage):
    def should_be_cant_see_product_in_basket_opened_from_product_page(self):
        open_basket = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        open_basket.click()
        time.sleep(1)
        assert self.is_element_present(*BasketPageLocators.ALLERT_INNER_BASKET), "Basket is not empty!"