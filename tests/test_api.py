import os
import requests
import pytest
import logging

log_dir = 'logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file = os.path.join(log_dir, 'logs_api.log')

def configure_logger(name, log_file):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

base_logger = configure_logger('base_request_logger', log_file)


class BaseRequest:
    def __init__(self, base_url):
        self.base_url = base_url
        self.logger = base_logger

    def _request(self, url, request_type, data=None, expected_error=False):
        stop_flag = False
        while not stop_flag:
            if request_type == 'GET':
                self.logger.debug(f'Sending GET request to: {url}')
                response = requests.get(url)
                stop_flag = True
            elif request_type == 'POST':
                self.logger.debug(f'Sending POST request to: {url}')
                response = requests.post(url, data=data)
                stop_flag = True
            elif request_type == 'PUT':
                self.logger.debug(f'Sending PUT request to: {url}')
                response = requests.put(url, data=data)
            else:
                self.logger.debug(f'Sending DELETE request to: {url}')
                response = requests.delete(url)

            if not expected_error and response.status_code == 200:
                stop_flag = True
            elif expected_error:
                stop_flag = True

        # Log response details
        self.logger.debug(f'{request_type} example')
        self.logger.debug(response.url)
        self.logger.debug(f'Status Code: {response.status_code}')
        self.logger.debug(f'Reason: {response.reason}')
        self.logger.debug(f'Response Text: {response.text}')
        self.logger.debug(f'Response JSON: {response.json()}')
        self.logger.debug('**********')
        return response

    def get(self, endpoint, endpoint_id, expected_error=False):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'GET', expected_error=expected_error)
        return response.json()

    def post(self, endpoint, body):
        url = f'{self.base_url}/{endpoint}/'
        response = self._request(url, 'POST', data=body)
        return response.status_code

    def delete(self, endpoint, endpoint_id):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'DELETE')
        return response.status_code

    def put(self, endpoint, endpoint_id, body):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'PUT', data=body)
        return response.status_code

# Configure logging
logging.basicConfig(level=logging.DEBUG)

BASE_URL = 'https://jsonplaceholder.typicode.com'

base_request = BaseRequest(BASE_URL)

@pytest.mark.parametrize('name, username, email',
                         [
                             ('IvanIvanich', 'Ivanich', 'Ivanich@gmail.com'),
                             ('Fedya', 'Alekseivic', 'F.Aleks@ya.ru'),
                             ('Sasha', 'Horus', 'hrw@mail.ru'),

                         ])
def test_create_user(name, username, email):
    # Create new user
    data = {
        'name': name,
        'username': username,
        'email': email
    }
    test_new = base_request.post('users', data)
    assert test_new == 201
    base_request.logger.debug(f'Created user with name: {name}, username: {username}, email: {email}')

@pytest.mark.parametrize('name, username, email, id',
                         [
                             ('Sergey', 'test_user', 'ssh@gmail.com', 1),
                             ('Vasiliy', 'breewer', 'bearrr@ya.ru', 2),
                             ('Vova', 'neo1234', 'neo_matrix@mail.ru', 3),

                         ])
def test_update_user(name, username, email, id):
    # Update user
    data = {
        'name': name,
        'username': username,
        'email': email
    }
    test_update = base_request.put('users', id, data)
    assert test_update == 200
    base_request.logger.debug(f'Updated user with ID {id} to have name: {name}, username: {username}, email: {email}')

@pytest.mark.parametrize('id',[1, 2, 3])
def test_delete_user(id):
    deleted = base_request.delete('users', id)
    assert deleted == 200
    base_request.logger.debug(f'Deleted user with ID {id}')

def test_get_user():
    checker = base_request.get('users', 4)
    assert checker['name'] == 'Patricia Lebsack'
    base_request.logger.debug(f'Fetched user details: {checker}')