from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from .locators import BasePageLocators
import math
import time

class BasePage():
    def __init__(self, browser, url, timeout = 10): # , timeout = 10
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):    # или любое другое исключение
            return False
        return True

    def solve_quiz_and_get_code(self):
        strat_time = time.time()
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        print(f"x = {x}")
        answer = math.log(abs((12 * math.sin(float(x)))))
        # print("Test run time: %f seconds.\n" % (time.time() - start_time))
        print(f"answer = '{answer}'")
        # self.browser.switch_to.alert
        # alert = self.browser.switch_to.alert
        alert.send_keys(str(answer))
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self, how, what, timeout = 4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            print("\nElement is NOT present!")
            return True
        print("\nElement is present!")
        return False

    def should_not_be_succes_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALLERT_INNER), "Success message is presented, but should not be"

    def is_disappeared(self, how, what, timeout = 4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            print("\nElement is present!")
            return False
        print("\nElement is NOT present!")
        return True

