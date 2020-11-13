import requests

from logger_settings import logging


def course_server_checker():
    response = requests.get('https://python101.online')
    logging.info(f'response.url: {response.url}')
    logging.info(f'response.status_code: {response.status_code}')
    return response.ok
