import pytest
import requests
from utils.data_helper import DataHelper as DH


class TestGetUserInfo:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.vars = DH.get_data('variables.json')
        self.url = self.vars.get('current_user_url')
        self.user_data = DH.get_data('stored_user.json')    # get previously created user info
        self.headers = {'Authorization': self.user_data.get('token')}    # token of existing user
        self.invalid_headers = {'Authorization': self.vars.get('invalid_token')}    # token non-existing in the system

    def test_get_user_profile(self):
        user = self.user_data['user']   # get user info for validation

        # send request
        r = requests.get(self.url, headers=self.headers)
        assert r.status_code == 200    # validate status code

        # validate that response returned information of the required user
        data = r.json()
        assert data['_id'] == user['_id']
        assert data['firstName'] == user['firstName']
        assert data['lastName'] == user['lastName']
        assert data['email'] == user['email']
        assert data['__v'] == user['__v']

    def test_get_non_existing_user(self):

        # send request
        r = requests.get(self.url, headers=self.invalid_headers)
        assert r.status_code == 401    # validate status code

        # validate error message
        data = r.json()
        assert data['error'] == 'Please authenticate.'
