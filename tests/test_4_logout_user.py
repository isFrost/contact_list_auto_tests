import pytest
import requests
from utils.data_helper import DataHelper as DH


class TestLogoutUser:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.vars = DH.get_data('variables.json')
        self.url = self.vars.get('login_url')
        self.user = DH.get_data('stored_user.json')['user']    # get previously created user info

        # login the user
        r = requests.post(self.url, json={'email': self.user['email'], 'password': self.user['password']})
        self.headers = {'Authorization': r.json()['token']}    # token of existing user
        self.invalid_headers = {'Authorization': self.vars.get('invalid_token')}    # token non-existing in the system
        self.url = self.vars.get('logout_url')

    def test_logout_user(self):

        # send request
        r = requests.post(self.url, headers=self.headers)
        assert r.status_code == 200    # validate status code

    def test_logout_unauthorized_user(self):

        # send request
        r = requests.post(self.url, headers=self.invalid_headers)
        assert r.status_code == 401    # validate status code
