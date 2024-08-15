import pytest
import requests
import allure


class TestAddUser:
    @allure.parent_suite('Contact List API')
    @allure.suite('TS01: User Management')
    @allure.sub_suite('TC01: Add user')
    def test_add_new_user(self, users_url, default_headers, user_payload):
        r = requests.post(users_url, headers=default_headers, json=user_payload)    # send request
        assert r.status_code == 201    # validate status code
        # validate that response returns required user fields with relevant information
        data = r.json()
        assert data['user']['firstName'] == user_payload['firstName']
        assert data['user']['lastName'] == user_payload['lastName']
        assert data['user']['email'] == user_payload['email']
        assert data['user']['_id'] is not None
        assert data['user']['__v'] == 1
        assert data['token'] is not None

    @allure.parent_suite('Contact List API')
    @allure.suite('TS01: User Management')
    @allure.sub_suite('TC02: Validation of First Name on adding new user')
    def test_first_name_validation(self, users_url, default_headers, user_payload):
        user_payload['firstName'] = ''    # set first name in the payload to blank
        r = requests.post(users_url, headers=default_headers, json=user_payload)    # send request
        assert r.status_code == 400   # validate status code
        data = r.json()
        assert data['errors']['firstName']['message'] == 'Path `firstName` is required.'    # validate error message

    @allure.parent_suite('Contact List API')
    @allure.suite('TS01: User Management')
    @allure.sub_suite('TC03: Validation of Last Name on adding new user')
    def test_last_name_validation(self, users_url, default_headers, user_payload):
        user_payload['lastName'] = ''    # set last name in the payload to blank
        r = requests.post(users_url, headers=default_headers, json=user_payload)   # send request
        assert r.status_code == 400    # validate status code
        data = r.json()
        assert data['errors']['lastName']['message'] == 'Path `lastName` is required.'   # validate error message

    @allure.parent_suite('Contact List API')
    @allure.suite('TS01: User Management')
    @allure.sub_suite('TC04: Validation of Email on adding new user')
    def test_email_validation(self, users_url, default_headers, user_payload):
        user_payload['email'] = 'INVALID EMAIL TC4'     # set email in the payload to invalid value
        r = requests.post(users_url, headers=default_headers, json=user_payload)    # send request
        assert r.status_code == 400
        data = r.json()
        assert data['errors']['email']['message'] == 'Email is invalid'    # validate error message

    @allure.parent_suite('Contact List API')
    @allure.suite('TS01: User Management')
    @allure.sub_suite('TC05: Validation of Password on adding new user')
    def test_password_validation(self, users_url, default_headers, user_payload):
        user_payload['password'] = '123'    # set password wit less characters than should be accepted
        r = requests.post(users_url, headers=default_headers, json=user_payload)    # send request
        assert r.status_code == 400    # validate status code
        data = r.json()
        assert data['errors']['password']['message'] == ('Path `password` (`123`) is shorter than the minimum allowed '
                                                         'length (7).')    # validate error message
