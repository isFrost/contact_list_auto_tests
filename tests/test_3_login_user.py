import pytest
import requests
from utils.data_helper import DataHelper as DH


class TestLoginUser:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.gen_variables = DH.get_data('variables.json')
        self.url = self.gen_variables.get('login_url')
        self.user_data = DH.get_data('stored_user.json')

    def test_login_user(self):
        user = self.user_data['user']
        r = requests.post(self.url, json={'email': user['email'], 'password': user['password']})
        assert r.status_code == 200
        data = r.json()
        assert data['user']['firstName'] == user['firstName']
        assert data['user']['lastName'] == user['lastName']
        assert data['user']['email'] == user['email']
        assert data['user']['_id'] == user['_id']

    def test_login_non_existing_user(self):
        r = requests.post(self.url, json={'email': 'non.existing.user@test.com', 'password': 'Welcome@123'})
        assert r.status_code == 401
