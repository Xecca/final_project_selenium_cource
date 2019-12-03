from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_check_avaliable_basket()
        self.should_be_add_product_in_basket()
        self.should_be_compare_name_product()
        self.should_be_compare_cost_product_in_basket()
        self.should_be_see_success_message_after_adding_product_to_basket()
    
    def should_be_check_avaliable_basket(self):
        # реализуем проверку на доступность кнопки "Добавить в корзину"
        assert self.is_element_present(*ProductPageLocators.BUTTON_BASKET), "Button 'Add to Basket' is not presented"
        print("\nBasket is avaliable!")
    
    def should_be_add_product_in_basket(self):
        add_product = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        add_product.click()
        time.sleep(1)
        self.solve_quiz_and_get_code()

    def should_be_compare_name_product(self):
        allert_inner = self.browser.find_element(*ProductPageLocators.ALLERT_INNER_PRODUCT)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert allert_inner.text == product_name.text, f"\nОР: Product 'The shellcoder's handbook' has beed added in basket.\n ФР: Product '{allert_inner.text}' has beed added in basket."
        print(allert_inner.text)

    def should_be_compare_cost_product_in_basket(self):
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST)
        product_cost_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_COST_IN_BASKET)
        assert product_cost.text == product_cost_in_basket.text, f"\nОР: Product cost: '{product_cost_in_basket.text} has been added in basket.\n ФР: Product cost in basket: {product_cost_in_basket}."
        print(f"Product cost in basket: {product_cost_in_basket.text}.")

    def should_be_see_success_message_after_adding_product_to_basket(self):
        add_product = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        add_product.click()
        assert self.is_not_element_present(*ProductPageLocators.ALLERT_INNER), "Succes message isn't dissapeared after adding product in basket!"

    def should_be_guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALLERT_INNER), "Succes message dissapeared before adding product in basket!"

    def should_be_message_disappeared_after_adding_product_to_basket(self):
        add_product = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        add_product.click()
        time.sleep(1)
        assert self.is_disappeared(*ProductPageLocators.ALLERT_INNER), "Succes message is not dissapeared after adding product in basket"
