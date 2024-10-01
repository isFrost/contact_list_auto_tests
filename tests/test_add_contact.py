import pytest
import requests
import allure


class TestAddContact:
    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC01: Add contact with US address (North America US)')
    def test_add_new_contact_usa(self, contacts_url, default_headers, contact_payload_usa):
        r = requests.post(contacts_url, headers=default_headers, json=contact_payload_usa)    # send request
        assert r.status_code == 201    # validate status code
        # validate that response contains relevant information on the created contact
        data = r.json()
        assert data['firstName'] == contact_payload_usa['firstName']
        assert data['lastName'] == contact_payload_usa['lastName']
        assert data['birthdate'] == contact_payload_usa['birthdate']
        assert data['email'] == contact_payload_usa['email']
        assert data['phone'] == contact_payload_usa['phone']
        assert data['street1'] == contact_payload_usa['street1']
        assert data['street2'] == contact_payload_usa['street2']
        assert data['city'] == contact_payload_usa['city']
        assert data['stateProvince'] == contact_payload_usa['stateProvince']
        assert data['postalCode'] == contact_payload_usa['postalCode']
        assert data['country'] == contact_payload_usa['country']

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC02: Add contact with Canada address (North America non-US)')
    def test_add_new_contact_canada(self, contacts_url, default_headers, contact_payload_amer):
        r = requests.post(contacts_url, headers=default_headers, json=contact_payload_amer)  # send request
        assert r.status_code == 201  # validate status code
        # validate that response contains relevant information on the created contact
        data = r.json()
        assert data['firstName'] == contact_payload_amer['firstName']
        assert data['lastName'] == contact_payload_amer['lastName']
        assert data['birthdate'] == contact_payload_amer['birthdate']
        assert data['email'] == contact_payload_amer['email']
        assert data['phone'] == contact_payload_amer['phone']
        assert data['street1'] == contact_payload_amer['street1']
        assert data['street2'] == contact_payload_amer['street2']
        assert data['city'] == contact_payload_amer['city']
        assert data['stateProvince'] == contact_payload_amer['stateProvince']
        assert data['postalCode'] == contact_payload_amer['postalCode']
        assert data['country'] == contact_payload_amer['country']

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC03: Add contact with EMEA address')
    def test_add_new_contact_emea(self, contacts_url, default_headers, contact_payload_emea):
        r = requests.post(contacts_url, headers=default_headers, json=contact_payload_emea)  # send request
        assert r.status_code == 201  # validate status code
        # validate that response contains relevant information on the created contact
        data = r.json()
        assert data['firstName'] == contact_payload_emea['firstName']
        assert data['lastName'] == contact_payload_emea['lastName']
        assert data['birthdate'] == contact_payload_emea['birthdate']
        assert data['email'] == contact_payload_emea['email']
        assert data['phone'] == contact_payload_emea['phone']
        assert data['street1'] == contact_payload_emea['street1']
        assert data['street2'] == contact_payload_emea['street2']
        assert data['city'] == contact_payload_emea['city']
        assert data['stateProvince'] == contact_payload_emea['stateProvince']
        assert data['postalCode'] == contact_payload_emea['postalCode']
        assert data['country'] == contact_payload_emea['country']

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC04: Add contact with APAC address')
    def test_add_new_contact_asia(self, contacts_url, default_headers, contact_payload_asia):
        r = requests.post(contacts_url, headers=default_headers, json=contact_payload_asia)  # send request
        assert r.status_code == 201  # validate status code
        # validate that response contains relevant information on the created contact
        data = r.json()
        assert data['firstName'] == contact_payload_asia['firstName']
        assert data['lastName'] == contact_payload_asia['lastName']
        assert data['birthdate'] == contact_payload_asia['birthdate']
        assert data['email'] == contact_payload_asia['email']
        assert data['phone'] == contact_payload_asia['phone']
        assert data['street1'] == contact_payload_asia['street1']
        assert data['street2'] == contact_payload_asia['street2']
        assert data['city'] == contact_payload_asia['city']
        assert data['stateProvince'] == contact_payload_asia['stateProvince']
        assert data['postalCode'] == contact_payload_asia['postalCode']
        assert data['country'] == contact_payload_asia['country']

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC05: Add contact with birthdate before 1970')
    def test_add_new_contact_birth_before_1970(self, contacts_url, default_headers, contact_payload_usa):
        contact_payload_usa['birthdate'] = '1964-03-01'    # set birthdate before 1970
        r = requests.post(contacts_url, headers=default_headers, json=contact_payload_usa)  # send request
        assert r.status_code == 201  # validate status code
        # validate that response contains relevant information on the created contact
        data = r.json()
        assert data['firstName'] == contact_payload_usa['firstName']
        assert data['lastName'] == contact_payload_usa['lastName']
        assert data['birthdate'] == contact_payload_usa['birthdate']
        assert data['email'] == contact_payload_usa['email']
        assert data['phone'] == contact_payload_usa['phone']
        assert data['street1'] == contact_payload_usa['street1']
        assert data['street2'] == contact_payload_usa['street2']
        assert data['city'] == contact_payload_usa['city']
        assert data['stateProvince'] == contact_payload_usa['stateProvince']
        assert data['postalCode'] == contact_payload_usa['postalCode']
        assert data['country'] == contact_payload_usa['country']

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC06: Validation of firstName on contact creation')
    def test_blank_first_name_validation(self, contacts_url, default_headers, contact_payload_usa):
        contact_payload_usa['firstName'] = ''
        r = requests.post(contacts_url, headers=default_headers, json=contact_payload_usa)  # send request
        assert r.status_code == 400    # validate status code
        data = r.json()
        assert data['message'] == 'Contact validation failed: firstName: Path `firstName` is required.'

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC07: Validation of lastName on contact creation')
    def test_blank_last_name_validation(self, contacts_url, default_headers, contact_payload_usa):
        contact_payload_usa['lastName'] = ''
        r = requests.post(contacts_url, headers=default_headers, json=contact_payload_usa)  # send request
        assert r.status_code == 400    # validate status code
        data = r.json()
        assert data['message'] == 'Contact validation failed: lastName: Path `lastName` is required.'

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC08: Validation of birthdate on contact creation')
    def test_blank_birthdate_validation(self, contacts_url, default_headers, contact_payload_usa):
        contact_payload_usa['birthdate'] = ''
        r = requests.post(contacts_url, headers=default_headers, json=contact_payload_usa)  # send request
        assert r.status_code == 400    # validate status code
        data = r.json()
        assert data['message'] == 'Contact validation failed: birthdate: Birthdate is invalid'

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC09: Validation of email on contact creation')
    def test_blank_email_validation(self, contacts_url, default_headers, contact_payload_usa):
        contact_payload_usa['email'] = ''
        r = requests.post(contacts_url, headers=default_headers, json=contact_payload_usa)  # send request
        assert r.status_code == 400    # validate status code
        data = r.json()
        assert data['message'] == 'Contact validation failed: email: Email is invalid'

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC10: Validation of phone number on contact creation')
    def test_blank_phone_validation(self, contacts_url, default_headers, contact_payload_usa):
        contact_payload_usa['phone'] = ''
        r = requests.post(contacts_url, headers=default_headers, json=contact_payload_usa)  # send request
        assert r.status_code == 400    # validate status code
        data = r.json()
        assert data['message'] == 'Contact validation failed: phone: Phone number is invalid'

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC11: Validation of street1 length on contact creation')
    def test_street1_exceeding_length_validation(self, contacts_url, default_headers, contact_payload_usa):
        contact_payload_usa['street1'] = 'test_test_test_test_test_test_test_test_1'
        r = requests.post(contacts_url, headers=default_headers, json=contact_payload_usa)  # send request
        assert r.status_code == 400    # validate status code
        data = r.json()
        assert data['message'] == ('Contact validation failed: street1: Path `street1` ('
                                   '`test_test_test_test_test_test_test_test_1`) is longer than the maximum allowed '
                                   'length (40).')

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC12: Validation of street2 length on contact creation')
    def test_street2_exceeding_length_validation(self, contacts_url, default_headers, contact_payload_usa):
        contact_payload_usa['street2'] = 'test_test_test_test_test_test_test_test_1'
        r = requests.post(contacts_url, headers=default_headers, json=contact_payload_usa)  # send request
        assert r.status_code == 400    # validate status code
        data = r.json()
        assert data['message'] == ('Contact validation failed: street2: Path `street2` ('
                                   '`test_test_test_test_test_test_test_test_1`) is longer than the maximum allowed '
                                   'length (40).')

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC13: Validation of city length on contact creation')
    def test_city_exceeding_length_validation(self, contacts_url, default_headers, contact_payload_usa):
        contact_payload_usa['city'] = 'test_test_test_test_test_test_test_test_1'
        r = requests.post(contacts_url, headers=default_headers, json=contact_payload_usa)  # send request
        assert r.status_code == 400    # validate status code
        data = r.json()
        assert data['message'] == ('Contact validation failed: city: Path `city` ('
                                   '`test_test_test_test_test_test_test_test_1`) is longer than the maximum allowed '
                                   'length (40).')

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC14: Validation of stateProvince length on contact creation')
    def test_state_exceeding_length_validation(self, contacts_url, default_headers, contact_payload_usa):
        contact_payload_usa['stateProvince'] = 'test_test_test_test_1'
        r = requests.post(contacts_url, headers=default_headers, json=contact_payload_usa)  # send request
        assert r.status_code == 400  # validate status code
        data = r.json()
        assert data['message'] == ('Contact validation failed: stateProvince: Path `stateProvince` ('
                                   '`test_test_test_test_1`) is longer than the maximum allowed '
                                   'length (20).')

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC15: Validation of postalCode on contact creation')
    def test_blank_postal_code_validation(self, contacts_url, default_headers, contact_payload_usa):
        contact_payload_usa['postalCode'] = ''
        r = requests.post(contacts_url, headers=default_headers, json=contact_payload_usa)  # send request
        assert r.status_code == 400    # validate status code
        data = r.json()
        assert data['message'] == 'Contact validation failed: postalCode: Postal code is invalid'

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC16: Validation of country length on contact creation')
    def test_country_exceeding_length_validation(self, contacts_url, default_headers, contact_payload_usa):
        contact_payload_usa['country'] = 'test_test_test_test_test_test_test_test_1'
        r = requests.post(contacts_url, headers=default_headers, json=contact_payload_usa)  # send request
        assert r.status_code == 400    # validate status code
        data = r.json()
        assert data['message'] == ('Contact validation failed: country: Path `country` ('
                                   '`test_test_test_test_test_test_test_test_1`) is longer than the maximum allowed '
                                   'length (40).')
