import json
import os
import time


class DataHelper:
    """ Decorator method that constructs path to data folder and adds filename to it. """
    @staticmethod
    def make_path(func):
        def wrapper(f_name, data=None):
            f_path = os.path.abspath(
                os.path.join(os.path.dirname(__file__), '..', 'data', f_name)
            )
            return func(f_path, data) if data else func(f_path)
        return wrapper

    """ Loads test data from JSON files. """
    @staticmethod
    @make_path
    def get_data(f_name):
        with open(f_name, 'r') as f:
            return json.load(f)

    """ Saves data as JSON file. """
    @staticmethod
    @make_path
    def set_data(f_name, data):
        with open(f_name, 'w') as f:
            json.dump(data, f, indent=4)

    """ Generates new user email based on the current timestamp. """
    @staticmethod
    def generate_email():
        return f'u-{str(time.time())}@test.com'
