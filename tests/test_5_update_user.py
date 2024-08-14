import pytest
import requests


class TestUpdateUser:
    def test_update_user(self, new_user, current_user_url, updated_payload):
        if not new_user:
            pytest.skip('Failed to create test user')    # skip test if user is not created
        r = requests.patch(
            current_user_url,
            headers={'Authorization': new_user['token']},
            json=updated_payload
        )    # send request
        assert r.status_code == 200    # validate that response returns code 200 OK
        # validate that response returns updated user information
        data = r.json()
        assert data['firstName'] == updated_payload['firstName']
        assert data['lastName'] == updated_payload['lastName']
        assert data['email'] == updated_payload['email']

    def test_update_non_existing_user(self, current_user_url, updated_payload, invalid_headers):
        updated_payload['email'] = f'tc2-{updated_payload['email']}'    # set email in case payload is accepted
        r = requests.patch(current_user_url, headers=invalid_headers, json=updated_payload)    # send request
        assert r.status_code == 401    # validate status code
        # validate error message
        data = r.json()
        assert data['error'] == 'Please authenticate.'

    def test_update_first_name_validation(self, new_user, current_user_url, updated_payload):
        if not new_user:
            pytest.skip('Failed to create test user')  # skip test if user is not created
        updated_payload['email'] = f'tc3-{updated_payload['email']}'    # set email in case payload is accepted
        updated_payload['firstName'] = ''   # set first name in the payload to blank
        r = requests.patch(
            current_user_url,
            headers={'Authorization': new_user['token']},
            json=updated_payload
        )    # send request
        assert r.status_code == 400    # validate status code
        # validate error message
        data = r.json()
        assert data['errors']['firstName']['message'] == 'Path `firstName` is required.'

    def test_update_last_name_validation(self, new_user, current_user_url, updated_payload):
        if not new_user:
            pytest.skip('Failed to create test user')  # skip test if user is not created
        updated_payload['email'] = f'tc3-{updated_payload['email']}'  # set email in case payload is accepted
        updated_payload['lastName'] = ''  # set first name in the payload to blank
        r = requests.patch(
            current_user_url,
            headers={'Authorization': new_user['token']},
            json=updated_payload
        )  # send request
        assert r.status_code == 400    # validate status code
        # validate error message
        data = r.json()
        assert data['errors']['lastName']['message'] == 'Path `lastName` is required.'

    def test_update_email_validation(self, new_user, current_user_url, updated_payload):
        if not new_user:
            pytest.skip('Failed to create test user')  # skip test if user is not created
        updated_payload['email'] = 'INVALID EMAIL TC4'  # set email in the payload to invalid value
        r = requests.patch(
            current_user_url,
            headers={'Authorization': new_user['token']},
            json=updated_payload
        )  # send request
        assert r.status_code == 400    # validate status code
        # validate error message
        data = r.json()
        assert data['errors']['email']['message'] == 'Email is invalid'

    def test_update_password_validation(self, new_user, current_user_url, updated_payload):
        if not new_user:
            pytest.skip('Failed to create test user')  # skip test if user is not created
        updated_payload['email'] = f'tc6-{updated_payload['email']}'    # set email in case payload is accepted
        updated_payload['password'] = '123'    # set password wit less characters than should be accepted
        r = requests.patch(
            current_user_url,
            headers={'Authorization': new_user['token']},
            json=updated_payload
        )  # send request
        assert r.status_code == 400    # validate status code
        # validate error message
        data = r.json()
        assert data['errors']['password']['message'] == ('Path `password` (`123`) is shorter than the minimum allowed '
                                                         'length (7).')
