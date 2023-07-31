import allure
from selenium.common import NoSuchElementException
from page_object.pages.base_page import BasePage
from page_object import locators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def change_currency(self):
        with allure.step("Click button 'Currency'"):
            self.find_element(locators.currency_btn).click()
        with allure.step("Choose currency 'Euro'"):
            self.find_element(locators.eur_currency_btn).click()

    def change_language_pl(self):
        with allure.step("Click button 'Language'"):
            self.find_element(locators.language_btn).click()
        with allure.step("Choose language 'Polski'"):
            self.find_element(locators.pl_language_btn).click()
