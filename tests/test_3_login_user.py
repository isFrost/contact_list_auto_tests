import allure
import pytest
import requests


class TestLoginUser:

    @allure.parent_suite('Contact List API')
    @allure.suite('TS01: User Management')
    @allure.sub_suite('TC14: Login existing user')
    def test_login_user(self, new_user, login_url, user_payload):
        if not new_user:
            pytest.skip('Failed to create test user')    # skip test if user is not created
        user = new_user['user']    # get user info for validation
        r = requests.post(
            login_url,
            json={'email': user['email'], 'password': user_payload['password']}
        )    # send request
        assert r.status_code == 200    # validate status code
        # validate that response returned correct user information
        data = r.json()
        assert data['user']['firstName'] == user['firstName']
        assert data['user']['lastName'] == user['lastName']
        assert data['user']['email'] == user['email']
        assert data['user']['_id'] == user['_id']

    @allure.parent_suite('Contact List API')
    @allure.suite('TS01: User Management')
    @allure.sub_suite('TC15: Login non-existing user')
    def test_login_non_existing_user(self, login_url):
        # send response with invalid user credentials
        r = requests.post(login_url, json={'email': 'non.existing.user@test.com', 'password': 'Welcome@123'})
        assert r.status_code == 401    # validate status code
