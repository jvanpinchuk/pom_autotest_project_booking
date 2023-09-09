import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.base_page import BasePage
from src import locators


class AttractionsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_attractions(self):
        with allure.step("Click button 'Attractions' in the main page"):
            self.find_element(locators.attractions_btn).click()

    def fill_attr_location_input(self):
        # with allure.step("Click field 'Pick up location'"):
        #     self.find_element(locators.location_input).click()
        with allure.step("Fill field 'Where are you going?'"):
            self.find_element(locators.where_attr_input).send_keys("Warsaw")
        with allure.step("Click first relative result"):
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locators.attr_rel_res)
            ).click()

    def attr_dates(self):
        with allure.step("Click field 'Dates'"):
            self.find_element(locators.attr_dates_btn).click()
        with allure.step("Choose date 'From'"):
            self.find_element(locators.attr_date_from).click()
        with allure.step("Choose date 'To'"):
            self.find_element(locators.attr_date_to).click()

    def attr_search_btn(self):
        with allure.step("Click button 'Search'"):
            self.find_element(locators.attr_search_btn).click()

    def positive_attr_search_res(self):
        search_res = len(self.find_elements(locators.attr_search_result))
        if search_res >= 1:
            return True
