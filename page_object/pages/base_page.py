import allure
from selenium.common import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from page_object import locators


# 12

def check_for_url_is_changed(current_url, url_that_should_be):
    with allure.step(f"Check, that current url equal {url_that_should_be}"):
        assert current_url == url_that_should_be


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_main_page(self):
        with allure.step("Open main page"):
            self.driver.get('https://www.booking.com')

    def close_main_popup(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(locators.close_main_popup)
        ).click()

    def wait_main_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locators.logo)
        )

    def find_element(self, *args):
        by_name, by_val = args[0]
        return self.driver.find_element(by_name, by_val)

    def is_element_visible(self, *args):
        by_name, by_val = args[0]
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((by_name, by_val))
        )
        return self.driver.find_element(by_name, by_val)

    def is_not_element_present(self, *args):
        try:
            by_name, by_val = args[0]
            WebDriverWait(self.driver, 10).until_not(
                EC.presence_of_element_located((by_name, by_val)),
            )
        except TimeoutException:
            return False
        return True

    def is_element_present(self, *args):
        try:
            by_name, by_val = args[0]
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((by_name, by_val)),
            )
        except TimeoutException:
            return False
        return True

    def find_elements(self, *args):
        by_name, by_val = args[0]
        return self.driver.find_elements(by_name, by_val)

    def go_to_main_page(self):
        self.is_element_visible(locators.logo).click()

    def get_current_url(self):
        return self.driver.current_url

    def is_elements_text_equal_to(self, *args, element_text):
        try:
            by_name, by_val = args[0]
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element((by_name, by_val), element_text),
            )
        except TimeoutException:
            return False
        return True

    def drag_and_drop_from_right_to_left(self, source, x_offset=0, y_offset=0):
        source_web_element = self.find_element(source)
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(source_web_element, x_offset, y_offset).perform()

