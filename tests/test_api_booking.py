import time, allure, pytest, requests, json
from page_object.api_data import Url, Headers


@allure.suite("Check API of booking.com")
@allure.title("Check of status code")
def test_check_status_code_get():
    response = requests.request("GET", Url.url, headers=Headers.headers)
    with allure.step('Check of status code'):
        assert response.status_code == 200



