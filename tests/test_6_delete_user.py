import pytest
import requests


class TestDeleteUser:
    def test_delete_user(self, new_user, current_user_url):
        if not new_user:
            pytest.skip('Failed to create test user')  # skip test if user is not created
        r = requests.delete(
            current_user_url,
            headers={'Authorization': new_user['token']}
        )    # send request
        assert r.status_code == 200    # validate status code

    def test_delete_non_existing_user(self, current_user_url, invalid_headers):
        r = requests.delete(current_user_url, headers=invalid_headers)    # send request
        assert r.status_code == 401    # validate status code
        # validate error message
        data = r.json()
        assert data['error'] == 'Please authenticate.'
