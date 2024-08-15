import allure
import pytest
import requests


class TestGetUserInfo:
    @allure.parent_suite('Contact List API')
    @allure.suite('TS01: User Management')
    @allure.sub_suite('TC06: Get information of existing user')
    def test_get_user_profile(self, new_user, current_user_url):
        if not new_user:
            pytest.skip('Failed to create test user')    # skip test if user is not created
        user = new_user['user']  # get user info for validation
        r = requests.get(
            current_user_url,
            headers={'Authorization': new_user['token']}
        )  # send request
        assert r.status_code == 200  # validate status code
        # validate that response returned information of the required user
        data = r.json()
        assert data['_id'] == user['_id']
        assert data['firstName'] == user['firstName']
        assert data['lastName'] == user['lastName']
        assert data['email'] == user['email']
        assert data['__v'] == user['__v']

    @allure.parent_suite('Contact List API')
    @allure.suite('TS01: User Management')
    @allure.sub_suite('TC07: Getting info on non-existing user')
    def test_get_non_existing_user(self, current_user_url, invalid_headers):
        r = requests.get(current_user_url, headers=invalid_headers)  # send request
        assert r.status_code == 401  # validate status code
        data = r.json()
        assert data['error'] == 'Please authenticate.'  # validate error message
