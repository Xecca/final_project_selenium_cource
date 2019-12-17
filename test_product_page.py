from .pages.product_page import ProductPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from selenium.common.exceptions import NoAlertPresentException
from selenium import webdriver as WebDriver
import pytest
import time

        
@pytest.mark.xfail(reason="Will need fix!")
@pytest.mark.login
class TestLoginFromProductPage():
    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        # 1. Гость открывает страницу товара
        page = BasketPage(browser, link)
        page.open()
        # 2. Переходит в корзину по кнопке в шапке сайта
        page.should_be_cant_see_product_in_basket_opened_from_product_page()

    @pytest.mark.need_review
    @pytest.mark.parametrize('promo_offer', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]) # , "2", "3", "4", "5", "6", "7", "8", "9"
    def test_guest_can_add_product_to_basket(browser, promo_offer):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
        print(f"opened link: {link}")
        page = ProductPage(browser, link)
        page.open()
        # page.should_be_product_page()
        page.should_be_check_avaliable_basket()
        page.should_be_add_product_in_basket()
        page.solve_quiz_and_get_code()
        page.should_be_compare_name_product()
        page.should_be_compare_cost_product_in_basket()
        page.should_be_see_success_message_after_adding_product_to_basket()

    def test_guest_should_see_login_link_on_product_page(browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

# @pytest.mark.xfail(reason="Will need fix!")
@pytest.mark.register
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = email
        page.register_new_user(str(password))

    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
        print(f"opened link: {link}")
        page = ProductPage(browser, link)
        page.open()
        # page.should_be_product_page()
        page.should_be_check_avaliable_basket()
        page.should_be_add_product_in_basket()
        page.solve_quiz_and_get_code()
        # time.sleep(1)
        page.should_be_compare_name_product()
        page.should_be_compare_cost_product_in_basket()
        page.should_be_see_success_message_after_adding_product_to_basket()

    def test_user_cant_see_success_message(browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
        # Открываем страницу товара 
        page = ProductPage(browser, link)
        page.open() 
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        page.should_be_guest_cant_see_success_message()
 
