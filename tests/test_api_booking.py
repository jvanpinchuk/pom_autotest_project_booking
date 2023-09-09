import time, allure, pytest, requests, json, re
from src.api_data import Url, Headers


@pytest.mark.presentation
@allure.suite("Check API of booking.com")
@allure.title("Check of status code")
def test_check_status_code_get():
    response = requests.request("GET", Url.main_url, headers=Headers.headers)
    with allure.step('Check of status code'):
        assert response.status_code == 200


@pytest.mark.presentation
@allure.suite("Check API of booking.com")
@allure.title("Check of tracker type is Client")
def test_check_tracker_type():
    response = requests.request("GET", Url.main_url, headers=Headers.headers)
    with allure.step('Check of tracker type is Client'):
        assert bool(re.search("tracker_type: 'Client'", response.text)), ('The searched text was not '
                                                                          'found in the response.')




