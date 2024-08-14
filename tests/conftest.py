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
    # original payload and updates its email


@pytest.fixture()
def updated_payload(user_payload):
    # for key in user_payload.keys():
    #     user_payload[key] = f'upd{user_payload[key]}'
    return {key: f'upd-{value}' for key, value in user_payload.items()}


@pytest.fixture()
def new_user(users_url, default_headers, user_payload):
    r = requests.post(users_url, headers=default_headers, json=user_payload)    # create new user
    return r.json() if r.status_code == 201 else None     # return user if created successfully
