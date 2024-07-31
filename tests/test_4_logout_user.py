import pytest
import requests
from utils.data_helper import DataHelper as DH


class TestLogoutUser:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.gen_variables = DH.get_data('variables.json')
        self.url = self.gen_variables.get('login_url')
        self.user = DH.get_data('stored_user.json')['user']
        r = requests.post(self.url, json={'email': self.user['email'], 'password': self.user['password']})
        self.headers = {'Authorization': r.json()['token']}
        self.invalid_headers = {'Authorization': self.gen_variables.get('invalid_token')}
        self.url = self.gen_variables.get('logout_url')

    def test_logout_user(self):
        r = requests.post(self.url, headers=self.headers)
        assert r.status_code == 200

    def test_logout_unauthorized_user(self):
        r = requests.post(self.url, headers=self.invalid_headers)
        assert r.status_code == 401
