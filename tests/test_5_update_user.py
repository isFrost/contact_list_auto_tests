import pytest
import requests
from utils.data_helper import DataHelper as DH


class TestUpdateUser:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.vars = DH.get_data('variables.json')
        self.user_data = DH.get_data('stored_user.json')
        self.upd_data = {
            'firstName': f'upd-{self.user_data['user']['firstName']}',
            'lastName': f'upd-{self.user_data['user']['lastName']}',
            'email': f'upd-{self.user_data['user']['email']}',
            'password': f'upd-{self.user_data['user']['password']}'
        }
        self.headers = {'Authorization': self.user_data['token']}
        self.invalid_headers = {'Authorization': self.vars['invalid_token']}
        self.url = self.vars['current_user_url']

    def test_update_user(self):
        # send request
        r = requests.patch(self.url, headers=self.headers, json=self.upd_data)

        # validate that response returns code 200 OK
        assert r.status_code == 200
        data = r.json()
        assert data['firstName'] == self.upd_data['firstName']
        assert data['lastName'] == self.upd_data['lastName']
        assert data['email'] == self.upd_data['email']

        # update user info in the stored data file
        self.user_data['user']['firstName'] = self.upd_data['firstName']
        self.user_data['user']['lastName'] = self.upd_data['lastName']
        self.user_data['user']['email'] = self.upd_data['email']
        self.user_data['user']['password'] = self.upd_data['password']
        DH.set_data('stored_user.json', self.user_data)

    def test_update_non_existing_user(self):
        upd_data = self.upd_data
        upd_data['email'] = f'tc2-{upd_data['email']}'
        r = requests.patch(self.url, headers=self.invalid_headers, json=upd_data)
        assert r.status_code == 401
        data = r.json()
        assert data['error'] == 'Please authenticate.'

    def test_update_first_name_validation(self):
        upd_data = self.upd_data
        upd_data['email'] = f'tc3-{upd_data['email']}'
        upd_data['firstName'] = ''
        r = requests.patch(self.url, headers=self.headers, json=upd_data)
        assert r.status_code == 400
        data = r.json()
        assert data['errors']['firstName']['message'] == 'Path `firstName` is required.'

    def test_update_last_name_validation(self):
        upd_data = self.upd_data
        upd_data['email'] = f'tc4-{upd_data['email']}'
        upd_data['lastName'] = ''
        r = requests.patch(self.url, headers=self.headers, json=upd_data)
        assert r.status_code == 400
        data = r.json()
        assert data['errors']['lastName']['message'] == 'Path `lastName` is required.'

    def test_update_email_validation(self):
        upd_data = self.upd_data
        upd_data['email'] = 'INVALID EMAIL'
        r = requests.patch(self.url, headers=self.headers, json=upd_data)
        assert r.status_code == 400
        data = r.json()
        assert data['errors']['email']['message'] == 'Email is invalid'

    def test_update_password_validation(self):
        upd_data = self.upd_data
        upd_data['email'] = f'tc6-{upd_data['email']}'
        upd_data['password'] = '123'
        r = requests.patch(self.url, headers=self.headers, json=upd_data)
        assert r.status_code == 400
        data = r.json()
        assert data['errors']['password']['message'] == ('Path `password` (`123`) is shorter than the minimum allowed '
                                                         'length (7).')
