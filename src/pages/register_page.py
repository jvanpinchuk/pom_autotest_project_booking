import allure
from page_object.pages.base_page import BasePage
from page_object import locators, data


class Register(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_main_page(self):
        with allure.step("Go to main page"):
            self.driver.get('https://www.booking.com')

    def start_register(self):
        with allure.step("Click button 'Register' on the main page"):
            self.find_element(locators.register_btn).click()

    def fill_email_input_valid_data_and_submit(self):
        with allure.step("Fill field 'Email'"):
            email = data.generate_email()
            self.find_element(locators.email_input).send_keys(email)
        with allure.step("Click button 'Continue'"):
            self.find_element(locators.continue_btn).click()

    def fill_password_input_and_confirm_valid_data_register(self):
        with allure.step("Fill field 'New password'"):
            password = data.generate_password(12)
            self.find_element(locators.new_pass_input).send_keys(password)
        with allure.step("Fill field ' Confirm password'"):
            self.find_element(locators.confirm_pass_input).send_keys(password)
        with allure.step("Click button 'Create account'"):
            self.find_element(locators.create_account_btn).click()


