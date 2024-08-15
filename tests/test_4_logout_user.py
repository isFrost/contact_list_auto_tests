import allure
import pytest
import requests


class TestLogoutUser:
    @allure.parent_suite('Contact List API')
    @allure.suite('TS01: User Management')
    @allure.sub_suite('TC16: Logout user that is logged in')
    def test_logout_user(self, new_user, logout_url):
        if not new_user:
            pytest.skip('Failed to create test user')    # skip test if user is not created
        r = requests.post(
            logout_url,
            headers={'Authorization': new_user['token']}
        )    # send request
        assert r.status_code == 200   # validate status code

    @allure.parent_suite('Contact List API')
    @allure.suite('TS01: User Management')
    @allure.sub_suite('TC17: Logout user that is not logged in')
    def test_logout_unauthorized_user(self, logout_url, invalid_headers):
        r = requests.post(logout_url, headers=invalid_headers)    # send request
        assert r.status_code == 401    # validate status code
