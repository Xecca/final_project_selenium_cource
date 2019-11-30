from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_check_avaliable_basket()
        self.should_be_add_product_in_basket()
        self.should_be_compare_name_product()
        self.should_be_compare_cost_product_in_basket()
    
    def should_be_check_avaliable_basket(self):
        # реализуем проверку на доступность кнопки "Добавить в корзину"
        assert self.is_element_present(*ProductPageLocators.BUTTON_BASKET), "Button 'Add to Basket' is not presented"
        print("\nBasket is avaliable!")
    
    def should_be_add_product_in_basket(self):
        add_product = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        add_product.click()
        self.solve_quiz_and_get_code()
        # time.sleep(100)

    def should_be_compare_name_product(self):
        allert_inner = self.browser.find_element(*ProductPageLocators.ALLERT_INNER_PRODUCT)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert allert_inner.text == f"{product_name.text} был добавлен в вашу корзину.", f"\nОР: Product 'The shellcoder's handbook' is added in basket.\n ФР: Product {allert_inner.text} is added in basket."
        print(allert_inner.text)

    def should_be_compare_cost_product_in_basket(self):
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST)
        product_cost_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_COST_IN_BASKET)
        assert product_cost.text == product_cost_in_basket.text, f"\nОР: Product cost: '{product_cost_in_basket.text} is added in basket.\n ФР: Product cost in basket: {product_cost_in_basket}."
        print(f"Product cost in basket: {product_cost_in_basket.text}.")
