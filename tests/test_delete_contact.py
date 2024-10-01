import pytest
import requests
import allure


class TestDeleteContact:
    @pytest.fixture(autouse=True)
    def setup(self, new_contact):
        if not new_contact:
            pytest.skip('Failed to create test contact')  # skip if failed to create test contact
        else:
            self.c_id = new_contact['_id']

    @allure.parent_suite('Contact List API')
    @allure.suite('TS02: Contact Management')
    @allure.sub_suite('TC77: Unauthorized deletion of existing contact')
    def test_unauthorized_contact_deletion(self, contacts_url, invalid_headers):
        r = requests.delete(f'{contacts_url}/{self.c_id}', headers=invalid_headers)    # send request
        assert r.status_code == 401    # validate statis code
        data = r.json()
        assert data['error'] == 'Please authenticate.'    # validate error message

    @allure.parent_suite('Contact List API')
    @allure.suite('TS02: Contact Management')
    @allure.sub_suite('TC78: Delete existing contact')
    def test_delete_existing_contact(self, contacts_url, default_headers):
        r = requests.delete(f'{contacts_url}/{self.c_id}', headers=default_headers)  # send request
        assert r.status_code == 200    # validate status code
        assert r.text == 'Contact deleted'    # validate confirmation message

    @allure.parent_suite('Contact List API')
    @allure.suite('TS02: Contact Management')
    @allure.sub_suite('TC79: Delete non-existing contact')
    def test_delete_non_existing_contact(self, contacts_url, default_headers):
        r = requests.delete(f'{contacts_url}/0', headers=default_headers)  # send request
        assert r.status_code == 400    # validate status code
        assert r.text == 'Invalid Contact ID'    # validate error message
