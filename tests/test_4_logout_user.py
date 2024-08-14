import pytest
import requests


class TestLogoutUser:
    def test_logout_user(self, new_user, logout_url):
        if not new_user:
            pytest.skip('Failed to create test user')    # skip test if user is not created
        r = requests.post(
            logout_url,
            headers={'Authorization': new_user['token']}
        )    # send request
        assert r.status_code == 200   # validate status code

    def test_logout_unauthorized_user(self, logout_url, invalid_headers):
        r = requests.post(logout_url, headers=invalid_headers)    # send request
        assert r.status_code == 401    # validate status code
