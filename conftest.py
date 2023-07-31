import pytest, requests
import undetected_chromedriver as uc



@pytest.fixture(scope='function')
def driver():
    driver = uc.Chrome()
    driver.maximize_window()
    driver.accept_untrusted_certs = True
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


