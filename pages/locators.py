from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.ID, "registration_link")

class LoginPageLocators():
    LOGIN_URL = (By.ID, "registration_link")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    BUTTON_BASKET = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    ALLERT_INNER_PRODUCT = (By.XPATH, "//div[@class='alertinner '][strong]")
    PRODUCT_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    PRODUCT_COST = (By.XPATH, "//p[@class='price_color']")
    PRODUCT_COST_IN_BASKET = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-info  fade in']//strong")
    