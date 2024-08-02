import pytest
import requests
from utils.data_helper import DataHelper as DH


class TestAddUser:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.vars = DH.get_data('variables.json')
        self.headers = {'Authorization': self.vars.get('token')}
        self.url = self.vars.get('users_url')
        self.payload = DH.get_data('new_user.json')   # payload with new user information

    def test_add_new_user(self):
        payload = self.payload
        payload['email'] = DH.generate_email()  # set email with the current timestamp

        # send request
        r = requests.post(self.url, headers=self.headers, json=payload)
        assert r.status_code == 201    # validate status code

        # validate that response returns required user fields with relevant information
        data = r.json()
        assert data['user']['firstName'] == payload['firstName']
        assert data['user']['lastName'] == payload['lastName']
        assert data['user']['email'] == payload['email']
        assert data['user']['_id'] is not None
        assert data['user']['__v'] == 1
        assert data['token'] is not None

        # save created user information to json file
        data['user']['password'] = payload['password']
        DH.set_data('stored_user.json', data)

    def test_first_name_validation(self):
        payload = self.payload
        payload['email'] = f'tc2-{payload['email']}'    # set email in case payload is accepted
        payload['firstName'] = ''    # set first name in the payload to blank

        # send request
        r = requests.post(self.url, headers=self.headers, json=payload)
        assert r.status_code == 400   # validate status code

        # validate error message
        data = r.json()
        assert data['errors']['firstName']['message'] == 'Path `firstName` is required.'

    def test_last_name_validation(self):
        payload = self.payload
        payload['email'] = f'tc3-{payload['email']}'    # set email in case payload is accepted
        payload['lastName'] = ''    # set last name in the payload to blank

        # send request
        r = requests.post(self.url, headers=self.headers, json=payload)
        assert r.status_code == 400    # validate status code

        # validate error message
        data = r.json()
        assert data['errors']['lastName']['message'] == 'Path `lastName` is required.'

    def test_email_validation(self):
        payload = self.payload
        payload['email'] = 'INVALID EMAIL TC4'     # set email in the payload to invalid value

        # send request
        r = requests.post(self.url, headers=self.headers, json=payload)
        assert r.status_code == 400

        # validate error message
        data = r.json()
        assert data['errors']['email']['message'] == 'Email is invalid'

    def test_password_validation(self):
        payload = self.payload
        payload['email'] = f'tc5-{payload['email']}'  # set email in case payload is accepted
        payload['password'] = '123'    # set password wit less characters than should be accepted

        # send request
        r = requests.post(self.url, headers=self.headers, json=payload)
        assert r.status_code == 400    # validate status code

        # validate error message
        data = r.json()
        assert data['errors']['password']['message'] == ('Path `password` (`123`) is shorter than the minimum allowed '
                                                         'length (7).')
