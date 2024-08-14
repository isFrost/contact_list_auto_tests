import pytest
import requests
from utils.data_helper import DataHelper as DH


class TestAddUser:
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

        # save created user information to json file
        data['user']['password'] = user_payload['password']    # TODO: remove once all the tests are independent
        DH.set_data('stored_user.json', data)    # TODO: remove once all the tests are independent

    def test_first_name_validation(self, users_url, default_headers, user_payload):
        user_payload['firstName'] = ''    # set first name in the payload to blank
        r = requests.post(users_url, headers=default_headers, json=user_payload)    # send request
        assert r.status_code == 400   # validate status code
        data = r.json()
        assert data['errors']['firstName']['message'] == 'Path `firstName` is required.'    # validate error message

    def test_last_name_validation(self, users_url, default_headers, user_payload):
        user_payload['lastName'] = ''    # set last name in the payload to blank
        r = requests.post(users_url, headers=default_headers, json=user_payload)   # send request
        assert r.status_code == 400    # validate status code
        data = r.json()
        assert data['errors']['lastName']['message'] == 'Path `lastName` is required.'   # validate error message

    def test_email_validation(self, users_url, default_headers, user_payload):
        user_payload['email'] = 'INVALID EMAIL TC4'     # set email in the payload to invalid value
        r = requests.post(users_url, headers=default_headers, json=user_payload)    # send request
        assert r.status_code == 400
        data = r.json()
        assert data['errors']['email']['message'] == 'Email is invalid'    # validate error message

    def test_password_validation(self, users_url, default_headers, user_payload):
        user_payload['password'] = '123'    # set password wit less characters than should be accepted
        r = requests.post(users_url, headers=default_headers, json=user_payload)    # send request
        assert r.status_code == 400    # validate status code
        data = r.json()
        assert data['errors']['password']['message'] == ('Path `password` (`123`) is shorter than the minimum allowed '
                                                         'length (7).')    # validate error message
