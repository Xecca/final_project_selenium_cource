from .pages.product_page import ProductPage
import pytest

@pytest.mark.xfail(reason="Will need fix!")
@pytest.mark.parametrize('promo_offer', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]) # , "2", "3", "4", "5", "6", "7", "8", "9"
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    print(f"opened link: {link}")
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
