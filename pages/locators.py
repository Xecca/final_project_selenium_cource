from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.ID, "registration_link")
    BASKET_LINK = (By.XPATH, "//*[@id='default']/header/div[1]/div/div[2]/span/a")

class LoginPageLocators():
    LOGIN_URL = (By.ID, "registration_link")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    BUTTON_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    BASKET_LINK = (By.XPATH, "//*[@id='default']/header/div[1]/div/div[2]/span/a")
    ALLERT_INNER = (By.XPATH, "//*[@id='messages']/div[1]/div")
    ALLERT_INNER_PRODUCT = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    PRODUCT_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    PRODUCT_COST = (By.XPATH, "//p[@class='price_color']")
    PRODUCT_COST_IN_BASKET = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-info  fade in']//strong")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators():
    ALLERT_INNER_BASKET = (By.XPATH, "//*[@id='content_inner']/p")