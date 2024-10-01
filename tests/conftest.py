import pytest
import requests
from utils.data_helper import DataHelper as DH


@pytest.fixture()
def users_url():
    return DH.get_data('variables.json')['users_url']


@pytest.fixture()
def current_user_url():
    return DH.get_data('variables.json')['current_user_url']


@pytest.fixture()
def login_url():
    return DH.get_data('variables.json')['login_url']


@pytest.fixture()
def logout_url():
    return DH.get_data('variables.json')['logout_url']


@pytest.fixture()
def default_headers():
    return {'Authorization': DH.get_data('variables.json')['token']}


@pytest.fixture()
def invalid_headers():
    return {'Authorization': DH.get_data('variables.json')['invalid_token']}


@pytest.fixture()
def user_payload():
    return {**DH.get_data('new_user.json'), 'email': DH.generate_email()}    # creates new dictionary containing the
    # original user payload and updates it with unique email


@pytest.fixture()
def contact_payload_usa():
    return {**DH.get_data('new_contact_usa.json'), 'email': DH.generate_email()}    # create new dictionary containing
    # the original contact payload and update it with unique email


@pytest.fixture()
def contact_payload_amer():
    return {**DH.get_data('new_contact_canada.json'), 'email': DH.generate_email()}    # create new dictionary
    # containing the original contact payload and update it with unique email


@pytest.fixture()
def contact_payload_emea():
    return {**DH.get_data('new_contact_eu.json'), 'email': DH.generate_email()}    # create new dictionary containing
    # the original contact payload and update it with unique email


@pytest.fixture()
def contact_payload_asia():
    return {**DH.get_data('new_contact_asia.json'), 'email': DH.generate_email()}    # create new dictionary containing
    # the original contact payload and update it with unique email


@pytest.fixture()
def updated_payload(user_payload):
    return {key: f'upd-{value}' for key, value in user_payload.items()}    # update all values in the payload


@pytest.fixture()
def contacts_url():
    return DH.get_data('variables.json')['contacts_url']


@pytest.fixture()
def new_user(users_url, default_headers, user_payload):
    r = requests.post(users_url, headers=default_headers, json=user_payload)    # create new user
    return r.json() if r.status_code == 201 else None     # return user if created successfully


@pytest.fixture()
def new_contact(contacts_url, default_headers, contact_payload_usa):
    r = requests.post(contacts_url, headers=default_headers, json=contact_payload_usa)    # create new contact
    return r.json() if r.status_code == 201 else None    # return contact if created successfully
