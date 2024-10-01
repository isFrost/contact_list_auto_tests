import pytest
import requests
import allure


class TestGetContactInfo:
    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC17: Get the list of the contacts')
    def test_get_list_of_contacts(self, new_contact, contacts_url, default_headers):
        contacts = [new_contact for i in range(4)]  # create several new contacts
        if len(contacts) == 0:
            pytest.skip('Failed to create contacts for the test')    # skip if failed to create any contacts
        r = requests.get(contacts_url, headers=default_headers)  # send request to get list of contacts
        assert r.status_code == 200  # validate that server returns code 200 OK
        data = {i['_id']: i for i in r.json()}  # convert response data to dictionary with contact id as a key
        # validate that each of created contacts is in the list of contacts returned in response
        for contact in contacts:
            assert data[contact['_id']]['firstName'] == contact['firstName']
            assert data[contact['_id']]['firstName'] == contact['firstName']
            assert data[contact['_id']]['lastName'] == contact['lastName']
            assert data[contact['_id']]['birthdate'] == contact['birthdate']
            assert data[contact['_id']]['email'] == contact['email']
            assert data[contact['_id']]['phone'] == contact['phone']
            assert data[contact['_id']]['street1'] == contact['street1']
            assert data[contact['_id']]['street2'] == contact['street2']
            assert data[contact['_id']]['city'] == contact['city']
            assert data[contact['_id']]['stateProvince'] == contact['stateProvince']
            assert data[contact['_id']]['postalCode'] == contact['postalCode']
            assert data[contact['_id']]['country'] == contact['country']

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC18: Restriction on contacts information for unauthorized users')
    def test_get_contacts_without_authorization(self, contacts_url, invalid_headers):
        r = requests.get(contacts_url, headers=invalid_headers)
        assert r.status_code == 401    # validate that server returns code 401 Unauthorized
        assert r.json()['error'] == 'Please authenticate.'     # validate error message

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC19: Get information of a particular contact')
    def test_get_contact(self, new_contact, contacts_url, default_headers):
        if not new_contact:
            pytest.skip('Failed to create test contact')  # skip if failed to create test contact
        else:
            contact = new_contact
        r = requests.get(f'{contacts_url}/{contact['_id']}', headers=default_headers)  # send request
        assert r.status_code == 200  # validate that response returns code 200 OK
        data = r.json()
        # validate that response contains relevant information on the given contact
        assert data['firstName'] == contact['firstName']
        assert data['lastName'] == contact['lastName']
        assert data['birthdate'] == contact['birthdate']
        assert data['email'] == contact['email']
        assert data['phone'] == contact['phone']
        assert data['street1'] == contact['street1']
        assert data['street2'] == contact['street2']
        assert data['city'] == contact['city']
        assert data['stateProvince'] == contact['stateProvince']
        assert data['postalCode'] == contact['postalCode']
        assert data['country'] == contact['country']

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC20: Validation of contact id in contact information request')
    def test_get_non_existing_contact(self, contacts_url, default_headers):
        r = requests.get(f'{contacts_url}/66d9a1a52b15240013700f2p', headers=default_headers)
        assert r.status_code == 400    # validate that server returns code 400 Bad Request
        assert r.text == 'Invalid Contact ID'    # validate error message
