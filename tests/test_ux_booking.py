import time
import pytest
import allure
from src import locators
from src.pages.singin_page import SingIn
from src.pages.register_page import Register
from src.pages.stays_page import SearchStay
from src.pages.main_page import MainPage
from src.pages.car_rentals_page import CarRentalsPage
from src.pages.attractions_pages import AttractionsPage


@pytest.mark.presentation
@pytest.mark.non_multiple_CPUs_run
@allure.suite("Account check")
@allure.title("Account registration of new user")
def test_create_account_with_valid_data(driver):
    reg = Register(driver)
    reg.open_main_page()
    reg.close_main_popup()
    reg.start_register()
    reg.fill_email_input_valid_data_and_submit()
    reg.fill_password_input_and_confirm_valid_data_register()
    assert reg.is_element_present(locators.your_account), "You are not registered"


@pytest.mark.presentation
@allure.suite("Account check")
@allure.title("Account sing in of registered user")
def test_sing_in_valid_data(driver):
    sing_in = SingIn(driver)
    sing_in.open_main_page()
    sing_in.close_main_popup()
    sing_in.start_sing_in()
    sing_in.fill_email_input_valid_data_and_submit()
    sing_in.fill_password_input_valid_data_and_submit()
    assert sing_in.is_element_present(locators.your_account), "You are not singed in"


@pytest.mark.presentation
@allure.suite('Searching check')
@allure.title("Searching stay")
def test_search_res(driver):
    search = SearchStay(driver)
    search.open_main_page()
    search.close_main_popup()
    search.fill_city_input()
    search.choose_dates()
    search.choose_occupancy()
    search.stays_search_btn()
    assert search.positive_stays_search_res(), "Search of stays is not successful. Try again."


@pytest.mark.presentation
@allure.suite('Changes check')
@allure.title("Change currency")
def test_change_currency(driver):
    currency = MainPage(driver)
    currency.open_main_page()
    currency.close_main_popup()
    currency.change_currency()
    driver.execute_script("window.scrollBy(0, 1800);")
    assert currency.is_element_present(locators.eur_currency_sign), "Currency is not changed. Try again."


@pytest.mark.presentation
@allure.suite('Changes check')
@allure.title("Change language")
def test_change_language(driver):
    language = MainPage(driver)
    language.open_main_page()
    language.close_main_popup()
    language.change_language_pl()
    assert language.is_element_present(locators.pl_language_pres), "Language is not changed. Try again."


@pytest.mark.presentation
@allure.suite('Searching check')
@allure.title("Searching car rental")
def test_car_rent_res(driver):
    car = CarRentalsPage(driver)
    car.open_main_page()
    car.close_main_popup()
    car.open_car_rentals()
    car.fill_car_location_input()
    car.pick_up_dates()
    car.drop_off_date()
    car.car_search_btn()
    time.sleep(20)


@pytest.mark.presentation
@allure.suite('Searching check')
@allure.title("Searching Attractions")
def test_attr_search(driver):
    attr = AttractionsPage(driver)
    attr.open_main_page()
    attr.close_main_popup()
    attr.open_attractions()
    attr.fill_attr_location_input()
    attr.attr_dates()
    attr.attr_search_btn()
    assert attr.positive_attr_search_res(), "Search of attractions is not successful. Try again."
