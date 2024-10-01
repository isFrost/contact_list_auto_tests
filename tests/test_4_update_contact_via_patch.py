import pytest
import requests
import allure


class TestUpdateContactViaPATCH:
    @pytest.fixture(autouse=True)
    def setup(self, new_contact):
        if not new_contact:
            pytest.skip('Failed to create test contact')  # skip if failed to create test contact
        else:
            self.c_id = new_contact['_id']
            self.payload = {key: value for key, value in new_contact.items() if key not in {'_id', 'owner', '__v'}}

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC49: Update contact\'s firstName via PATCH method')
    def test_update_first_name(self, contacts_url, default_headers):
        payload = {**self.payload, 'firstName': 'Updated'}    # update payload with new firstName
        r = requests.patch(f'{contacts_url}/{self.c_id}', headers=default_headers, json=payload)    # send request
        assert r.status_code == 200    # validate status code
        data = r.json()
        assert data['firstName'] == payload['firstName']    # validate that firstName is updates

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC50: Update contact\'s lastName via PATCH method')
    def test_update_last_name(self, contacts_url, default_headers):
        payload = {**self.payload, 'lastName': 'Updated'}    # update payload with new lastName
        r = requests.patch(f'{contacts_url}/{self.c_id}', headers=default_headers, json=payload)    # send request
        assert r.status_code == 200    # validate status code
        data = r.json()
        assert data['lastName'] == payload['lastName']    # validate that lastName is updates

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC51: Update contact\'s birthdate via PATCH method')
    def test_update_birthdate(self, contacts_url, default_headers):
        payload = {**self.payload, 'birthdate': '1999-12-12'}  # update payload with new birthdate
        r = requests.patch(f'{contacts_url}/{self.c_id}', headers=default_headers, json=payload)  # send request
        assert r.status_code == 200  # validate status code
        data = r.json()
        assert data['birthdate'] == payload['birthdate']  # validate that birthdate is updates

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC52: Update contact\'s email via PATCH method')
    def test_update_email(self, contacts_url, default_headers):
        payload = {**self.payload, 'email': 'updated@test.com'}  # update payload with new email
        r = requests.patch(f'{contacts_url}/{self.c_id}', headers=default_headers, json=payload)  # send request
        assert r.status_code == 200  # validate status code
        data = r.json()
        assert data['email'] == payload['email']  # validate that email is updates

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC53: Update contact\'s phone via PATCH method')
    def test_update_phone(self, contacts_url, default_headers):
        payload = {**self.payload, 'phone': '5555555555'}  # update payload with new phone number
        r = requests.patch(f'{contacts_url}/{self.c_id}', headers=default_headers, json=payload)  # send request
        assert r.status_code == 200  # validate status code
        data = r.json()
        assert data['phone'] == payload['phone']  # validate that phone is updates

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC54: Update contact\'s street1 via PATCH method')
    def test_update_street1(self, contacts_url, default_headers):
        payload = {**self.payload, 'street1': 'Updated'}  # update payload with new street1 value
        r = requests.patch(f'{contacts_url}/{self.c_id}', headers=default_headers, json=payload)  # send request
        assert r.status_code == 200  # validate status code
        data = r.json()
        assert data['street1'] == payload['street1']  # validate that street1 is updates

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC55: Update contact\'s street2 via PATCH method')
    def test_update_street2(self, contacts_url, default_headers):
        payload = {**self.payload, 'street2': 'Updated'}  # update payload with new street2 value
        r = requests.patch(f'{contacts_url}/{self.c_id}', headers=default_headers, json=payload)  # send request
        assert r.status_code == 200  # validate status code
        data = r.json()
        assert data['street2'] == payload['street2']  # validate that street2 is updates

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC56: Update contact\'s city via PATCH method')
    def test_update_city(self, contacts_url, default_headers):
        payload = {**self.payload, 'city': 'Updated'}  # update payload with new city value
        r = requests.patch(f'{contacts_url}/{self.c_id}', headers=default_headers, json=payload)  # send request
        assert r.status_code == 200  # validate status code
        data = r.json()
        assert data['city'] == payload['city']  # validate that city is updates

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC57: Update contact\'s stateProvince via PATCH method')
    def test_update_state(self, contacts_url, default_headers):
        payload = {**self.payload, 'stateProvince': 'UP'}  # update payload with new stateProvince value
        r = requests.patch(f'{contacts_url}/{self.c_id}', headers=default_headers, json=payload)  # send request
        assert r.status_code == 200  # validate status code
        data = r.json()
        assert data['stateProvince'] == payload['stateProvince']  # validate that stateProvince is updates

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC58: Update contact\'s postalCode via PATCH method')
    def test_update_postal_code(self, contacts_url, default_headers):
        payload = {**self.payload, 'postalCode': '22222'}  # update payload with new postalCode value
        r = requests.patch(f'{contacts_url}/{self.c_id}', headers=default_headers, json=payload)  # send request
        assert r.status_code == 200  # validate status code
        data = r.json()
        assert data['postalCode'] == payload['postalCode']  # validate that postalCode is updates

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC59: Update contact\'s country via PATCH method')
    def test_update_country(self, contacts_url, default_headers):
        payload = {**self.payload, 'country': 'UPD'}  # update payload with new country value
        r = requests.patch(f'{contacts_url}/{self.c_id}', headers=default_headers, json=payload)  # send request
        assert r.status_code == 200  # validate status code
        data = r.json()
        assert data['country'] == payload['country']  # validate that country is updates

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC60: Update contact\'s firstName w/ blank value via PATCH method')
    def test_update_blank_first_name(self, contacts_url, default_headers):
        payload = {**self.payload, 'firstName': ''}    # update payload with blank firstName
        r = requests.patch(f'{contacts_url}/{self.c_id}', headers=default_headers, json=payload)  # send request
        assert r.status_code == 400
        data = r.json()
        assert data['message'] == 'Contact validation failed: firstName: Path `firstName` is required.'    # validate error text

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC61: Update contact\'s firstName w/ value exceeding length limit via PATCH method')
    def test_update_first_name_exceeding_length(self, contacts_url, default_headers):
        payload = {**self.payload, 'firstName': 'test_test_test_test_1'}  # set payload with firstName above char limit
        r = requests.patch(f'{contacts_url}/{self.c_id}', headers=default_headers, json=payload)  # send request
        assert r.status_code == 400
        data = r.json()
        assert data['message'] == ('Contact validation failed: firstName: Path `firstName` (`test_test_test_test_1`) is longer '
                                   'than the maximum allowed length (20).')    # validate error text

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC62: Update contact\'s lastName w/ blank value via PATCH method')
    def test_update_blank_last_name(self, contacts_url, default_headers):
        payload = {**self.payload, 'lastName': ''}  # update payload with blank lastName
        r = requests.patch(f'{contacts_url}/{self.c_id}', headers=default_headers, json=payload)  # send request
        assert r.status_code == 400
        data = r.json()
        assert data['message'] == 'Contact validation failed: lastName: Path `lastName` is required.'  # validate error text

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC63: Update contact\'s lastName w/ value exceeding length limit via PATCH method')
    def test_update_first_name_exceeding_length(self, contacts_url, default_headers):
        payload = {**self.payload, 'lastName': 'test_test_test_test_1'}  # set payload with lastName above char limit
        r = requests.patch(f'{contacts_url}/{self.c_id}', headers=default_headers, json=payload)  # send request
        assert r.status_code == 400
        data = r.json()
        assert data['message'] == ('Contact validation failed: lastName: Path `lastName` (`test_test_test_test_1`) is longer '
                                   'than the maximum allowed length (20).')  # validate error text

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC64: Update contact\'s birthdate w/ blank value via PATCH method')
    def test_update_blank_birthdate(self, contacts_url, default_headers):
        payload = {**self.payload, 'birthdate': ''}  # update payload with blank birthdate
        r = requests.patch(f'{contacts_url}/{self.c_id}', headers=default_headers, json=payload)  # send request
        assert r.status_code == 400
        data = r.json()
        assert data['message'] == 'Contact validation failed: birthdate: Birthdate is invalid'  # validate error text

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC65: Update contact\'s birthdate w/ invalid value via PATCH method')
    def test_update_invalid_birthdate(self, contacts_url, default_headers):
        payload = {**self.payload, 'birthdate': '01-01-1970'}  # update payload with invalid birthdate
        r = requests.patch(f'{contacts_url}/{self.c_id}', headers=default_headers, json=payload)  # send request
        assert r.status_code == 400
        data = r.json()
        assert data['message'] == 'Contact validation failed: birthdate: Birthdate is invalid'  # validate error text

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC66: Update contact\'s email w/ blank value via PATCH method')
    def test_update_blank_email(self, contacts_url, default_headers):
        payload = {**self.payload, 'email': ''}  # update payload with blank email
        r = requests.patch(f'{contacts_url}/{self.c_id}', headers=default_headers, json=payload)  # send request
        assert r.status_code == 400
        data = r.json()
        assert data['message'] == 'Contact validation failed: email: Email is invalid'  # validate error text

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC67: Update contact\'s email w/ invalid value via PATCH method')
    def test_update_invalid_email(self, contacts_url, default_headers):
        payload = {**self.payload, 'email': 'jdoetest.com'}  # update payload with invalid email
        r = requests.patch(f'{contacts_url}/{self.c_id}', headers=default_headers, json=payload)  # send request
        assert r.status_code == 400
        data = r.json()
        assert data['message'] == 'Contact validation failed: email: Email is invalid'  # validate error text

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC68: Update contact\'s phone w/ blank value via PATCH method')
    def test_update_blank_phone(self, contacts_url, default_headers):
        payload = {**self.payload, 'phone': ''}  # update payload with blank phone number
        r = requests.patch(f'{contacts_url}/{self.c_id}', headers=default_headers, json=payload)  # send request
        assert r.status_code == 400
        data = r.json()
        assert data['message'] == 'Contact validation failed: phone: Phone number is invalid'  # validate error text

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC69: Update contact\'s phone w/ value exceeding length limit via PATCH method')
    def test_update_phone_exceeding_length(self, contacts_url, default_headers):
        payload = {**self.payload, 'phone': '11111111111013'}  # set payload with phone above char limit
        r = requests.patch(f'{contacts_url}/{self.c_id}', headers=default_headers, json=payload)  # send request
        assert r.status_code == 400
        data = r.json()
        assert data['message'] == 'Contact validation failed: phone: Phone number is invalid'  # validate error text

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC70: Update contact\'s street1 w/ value exceeding length limit via PATCH method')
    def test_update_street1_exceeding_length(self, contacts_url, default_headers):
        payload = {**self.payload, 'street1': 'test_test_test_test_test_test_test_test_test_1'}  # set payload with
        # street1 value above char limit
        r = requests.patch(f'{contacts_url}/{self.c_id}', headers=default_headers, json=payload)  # send request
        assert r.status_code == 400
        data = r.json()
        assert data['message'] == ('Contact validation failed: street1: Path `street1` ('
                                   '`test_test_test_test_test_test_test_test_test_1`) is longer than the maximum '
                                   'allowed length (40).')  # validate error text

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC71: Update contact\'s street2 w/ value exceeding length limit via PATCH method')
    def test_update_street2_exceeding_length(self, contacts_url, default_headers):
        payload = {**self.payload, 'street2': 'test_test_test_test_test_test_test_test_test_1'}  # set payload with
        # street2 value above char limit
        r = requests.patch(f'{contacts_url}/{self.c_id}', headers=default_headers, json=payload)  # send request
        assert r.status_code == 400
        data = r.json()
        assert data['message'] == ('Contact validation failed: street2: Path `street2` ('
                                   '`test_test_test_test_test_test_test_test_test_1`) is longer than the maximum '
                                   'allowed length (40).')  # validate error text

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC72: Update contact\'s city w/ value exceeding length limit via PATCH method')
    def test_update_city_exceeding_length(self, contacts_url, default_headers):
        payload = {**self.payload, 'city': 'test_test_test_test_test_test_test_test_test_1'}  # set payload with
        # city value above char limit
        r = requests.patch(f'{contacts_url}/{self.c_id}', headers=default_headers, json=payload)  # send request
        assert r.status_code == 400
        data = r.json()
        assert data['message'] == ('Contact validation failed: city: Path `city` ('
                                   '`test_test_test_test_test_test_test_test_test_1`) is longer than the '
                                   'maximum allowed length (40).')  # validate error text

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC73: Update contact\'s stateProvince w/ value exceeding length limit via PATCH method')
    def test_update_state_exceeding_length(self, contacts_url, default_headers):
        payload = {**self.payload, 'stateProvince': 'test_test_test_test_1'}  # set payload
        # with stateProvince value above char limit
        r = requests.patch(f'{contacts_url}/{self.c_id}', headers=default_headers, json=payload)  # send request
        assert r.status_code == 400
        data = r.json()
        assert data['message'] == ('Contact validation failed: stateProvince: Path `stateProvince` (`test_test_test_test_1`) '
                                   'is longer than the maximum allowed length (20).')  # validate error text

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC74: Update contact\'s postalCode w/ blank value via PATCH method')
    def test_update_blank_postal_code(self, contacts_url, default_headers):
        payload = {**self.payload, 'postalCode': ''}  # update payload with blank postalCode
        r = requests.patch(f'{contacts_url}/{self.c_id}', headers=default_headers, json=payload)  # send request
        assert r.status_code == 400
        data = r.json()
        assert data['message'] == 'Contact validation failed: postalCode: Postal code is invalid'  # validate error text

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC75: Update contact\'s postalCode w/ invalid value via PATCH method')
    def test_update_invalid_postal_code(self, contacts_url, default_headers):
        payload = {**self.payload, 'postalCode': '00000008'}  # update payload with invalid postalCode
        r = requests.patch(f'{contacts_url}/{self.c_id}', headers=default_headers, json=payload)  # send request
        assert r.status_code == 400
        data = r.json()
        assert data['message'] == 'Contact validation failed: postalCode: Postal code is invalid'  # validate error text

    @allure.parent_suite('Contact List API')
    @allure.suite('Contact Management')
    @allure.sub_suite('TC76: Update contact\'s country w/ value exceeding length limit via PATCH method')
    def test_update_country_exceeding_length(self, contacts_url, default_headers):
        payload = {**self.payload, 'country': 'test_test_test_test_test_test_test_test_1'}  # set payload
        # with country value above char limit
        r = requests.patch(f'{contacts_url}/{self.c_id}', headers=default_headers, json=payload)  # send request
        assert r.status_code == 400
        data = r.json()
        assert data['message'] == ('Contact validation failed: country: Path `country` ('
                                   '`test_test_test_test_test_test_test_test_1`) is longer than the maximum allowed '
                                   'length (40).')  # validate error text
