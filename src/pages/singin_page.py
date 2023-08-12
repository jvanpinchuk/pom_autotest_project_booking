import allure
from page_object.pages.base_page import BasePage
from page_object import locators


class SingIn(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def start_sing_in(self):
        with allure.step("Click button 'Sing in' in the main page"):
            self.find_element(locators.sing_in_btn).click()

    def fill_email_input_valid_data_and_submit(self):
        with allure.step("Fill field 'Email'"):
            self.find_element(locators.email_input).send_keys("j.v.a.n.pinchuk@gmail.com")
        with allure.step("Click button 'Continue'"):
            self.find_element(locators.continue_btn).click()

    def fill_password_input_valid_data_and_submit(self):
        with allure.step("Fill field 'Password' is present"):
            self.find_element(locators.pass_input).send_keys("N@hHh6,5Wep#CPp")
        with allure.step("Click button 'Sing in'"):
            self.find_element(locators.fin_sing_in_btn).click()




