import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.base_page import BasePage
from src import locators


class SearchStay(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def fill_city_input(self):
        with allure.step("Clear field 'Where are you going?'"):
            self.find_element(locators.where_input).clear()
        with allure.step("Fill field 'Where are you going?'"):
            self.find_element(locators.where_input).send_keys("Warsaw")
        with allure.step("Click first relative result"):
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locators.first_rel_res)
            ).click()

    def choose_dates(self):
        # with allure.step("Click field 'Calendar'"):
        #     self.find_element(locators.dates_search).click()
        with allure.step("Date 'From'"):
            self.find_element(locators.start_date_btn).click()
        with allure.step("Date 'To'"):
            self.find_element(locators.fin_date_btn).click()

    def choose_occupancy(self):
        with allure.step("Click field 'Occupancy'"):
            self.find_element(locators.occupancy_btn).click()
        with allure.step("Adult minus in occupancy"):
            self.find_element(locators.adult_minus_btn).click()
        # with allure.step("Adult plus in occupancy"):
        #     self.find_element(locators.adult_plus_btn).click()
        # with allure.step("Child minus in occupancy"):
        #     self.find_element(locators.child_minus_btn).click()
        # with allure.step("Child plus in occupancy"):
        #     self.find_element(locators.child_plus_btn).click()
        # with allure.step("Room minus in occupancy"):
        #     self.find_element(locators.room_minus_btn).click()
        # with allure.step("Room plus in occupancy"):
        #     self.find_element(locators.room_plus_btn).click()

    def stays_search_btn(self):
        with allure.step("Click button 'Search'"):
            self.find_element(locators.search_btn).click()

    def positive_stays_search_res(self):
        search_res = len(self.find_elements(locators.stays_search_result))
        if search_res >= 1:
            return True

