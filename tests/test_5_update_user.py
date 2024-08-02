import pytest
import requests
from utils.data_helper import DataHelper as DH


class TestUpdateUser:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.vars = DH.get_data('variables.json')
        self.user_data = DH.get_data('stored_user.json')
        self.url = self.vars['current_user_url']

        # setup payload to update the required user
        self.payload = {
            'firstName': f'upd-{self.user_data['user']['firstName']}',
            'lastName': f'upd-{self.user_data['user']['lastName']}',
            'email': f'upd-{self.user_data['user']['email']}',
            'password': f'upd-{self.user_data['user']['password']}'
        }
        self.headers = {'Authorization': self.user_data['token']}   # token of existing user
        self.invalid_headers = {'Authorization': self.vars['invalid_token']}    # token non-existing in the system

    def test_update_user(self):
        # send request
        r = requests.patch(self.url, headers=self.headers, json=self.payload)

        # validate that response returns code 200 OK
        assert r.status_code == 200
        
        # validate that response returns updated user information
        data = r.json()
        assert data['firstName'] == self.payload['firstName']
        assert data['lastName'] == self.payload['lastName']
        assert data['email'] == self.payload['email']

        # update user info in the stored data file
        self.user_data['user']['firstName'] = self.payload['firstName']
        self.user_data['user']['lastName'] = self.payload['lastName']
        self.user_data['user']['email'] = self.payload['email']
        self.user_data['user']['password'] = self.payload['password']
        DH.set_data('stored_user.json', self.user_data)

    def test_update_non_existing_user(self):
        payload = self.payload
        payload['email'] = f'tc2-{payload['email']}'    # set email in case payload is accepted

        # send request
        r = requests.patch(self.url, headers=self.invalid_headers, json=payload)
        assert r.status_code == 401    # validate status code

        # validate error message
        data = r.json()
        assert data['error'] == 'Please authenticate.'

    def test_update_first_name_validation(self):
        payload = self.payload
        payload['email'] = f'tc3-{payload['email']}'    # set email in case payload is accepted
        payload['firstName'] = ''   # set first name in the payload to blank

        # send request
        r = requests.patch(self.url, headers=self.headers, json=payload)
        assert r.status_code == 400    # validate status code

        # validate error message
        data = r.json()
        assert data['errors']['firstName']['message'] == 'Path `firstName` is required.'

    def test_update_last_name_validation(self):
        payload = self.payload
        payload['email'] = f'tc4-{payload['email']}'    # set email in case payload is accepted
        payload['lastName'] = ''    # set last name in the payload to blank

        # send request
        r = requests.patch(self.url, headers=self.headers, json=payload)
        assert r.status_code == 400    # validate status code

        # validate error message
        data = r.json()
        assert data['errors']['lastName']['message'] == 'Path `lastName` is required.'

    def test_update_email_validation(self):
        payload = self.payload
        payload['email'] = 'INVALID EMAIL'  # set email in the payload to invalid value

        # send request
        r = requests.patch(self.url, headers=self.headers, json=payload)
        assert r.status_code == 400    # validate status code

        # validate error message
        data = r.json()
        assert data['errors']['email']['message'] == 'Email is invalid'

    def test_update_password_validation(self):
        payload = self.payload
        payload['email'] = f'tc6-{payload['email']}'    # set email in case payload is accepted
        payload['password'] = '123'    # set password wit less characters than should be accepted

        # send request
        r = requests.patch(self.url, headers=self.headers, json=payload)
        assert r.status_code == 400    # validate status code

        # validate error message
        data = r.json()
        assert data['errors']['password']['message'] == ('Path `password` (`123`) is shorter than the minimum allowed '
                                                         'length (7).')
