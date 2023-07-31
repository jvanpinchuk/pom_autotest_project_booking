import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_object.pages.base_page import BasePage
from page_object import locators


class CarRentalsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_car_rentals(self):
        with allure.step("Click button 'Car rentals' in the main page"):
            self.find_element(locators.car_rentals_btn).click()

    def fill_car_location_input(self):
        # with allure.step("Click field 'Pick up location'"):
        #     self.find_element(locators.location_input).click()
        with allure.step("Fill field 'Pick up location''"):
            self.find_element(locators.location_input).send_keys("Warsaw")
        with allure.step("Click first relative result"):
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locators.loc_rel_res)
            ).click()

    def pick_up_dates(self):
        with allure.step("Click field 'Pick up dates'"):
            self.find_element(locators.pick_up_dates_btn).click()
        with allure.step("Pick up date 'From'"):
            self.find_element(locators.pick_up_date_from).click()
        with allure.step("Pick up date 'To'"):
            self.find_element(locators.pick_up_date_to).click()

    def drop_off_date(self):
        with allure.step("Click field 'Drop off date'"):
            self.find_element(locators.drop_off_date_btn).click()
        with allure.step("Drop off date"):
            self.find_element(locators.drop_off_date).click()

    def car_search_btn(self):
        with allure.step("Click button 'Search'"):
            self.find_element(locators.car_search_btn).click()