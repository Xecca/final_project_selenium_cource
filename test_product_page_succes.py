import pytest
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

# @pytest.mark.xfail(reason = "Need to fix it!")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # Открываем страницу товара
    page = ProductPage(browser, link)
    page.open()
    # Добавляем товар в корзину 
    page.should_be_see_success_message_after_adding_product_to_basket()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    # page.is_not_element_present()
 

def test_guest_cant_see_success_message(browser):
    # Открываем страницу товара 
    page = ProductPage(browser, link)
    page.open() 
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_be_guest_cant_see_success_message()
 

def test_message_disappeared_after_adding_product_to_basket(browser):
    # Открываем страницу товара
    page = ProductPage(browser, link)
    page.open()
    # Добавляем товар в корзину
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    page.should_be_message_disappeared_after_adding_product_to_basket()