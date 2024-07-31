import pytest
import requests
from utils.data_helper import DataHelper as DH


class TestGetUserInfo:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.gen_variables = DH.get_data('variables.json')
        self.url = self.gen_variables.get('current_user_url')
        self.user_data = DH.get_data('stored_user.json')
        self.headers = {'Authorization': self.user_data.get('token')}
        self.invalid_headers = {'Authorization': self.gen_variables.get('invalid_token')}

    def test_get_user_profile(self):
        user = self.user_data['user']
        r = requests.get(self.url, headers=self.headers)
        assert r.status_code == 200
        data = r.json()
        assert data['_id'] == user['_id']
        assert data['firstName'] == user['firstName']
        assert data['lastName'] == user['lastName']
        assert data['email'] == user['email']
        assert data['__v'] == user['__v']

    def test_get_non_existing_user(self):
        r = requests.get(self.url, headers=self.invalid_headers)
        assert r.status_code == 401
        data = r.json()
        assert data['error'] == 'Please authenticate.'
