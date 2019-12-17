from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)      # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                         # открываем страницу
        page.go_to_login_page()             # выполняем метод страницы - переходим на страницу логина
        # login_page = LoginPage(browser, browser.current_url)
        # login_page.should_be_login_page()

    def test_guest_should_see_login_link(browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
        link = "http://selenium1py.pythonanywhere.com"
        # 1. Гость открывает главную страницу
        page = ProductPage(browser, link)
        page.open()
        # 2. Переходит в корзину по кнопке в шапке сайта
        page.should_be_cant_see_product_in_basket_opened_from_main_page()
